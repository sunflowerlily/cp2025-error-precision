#!/usr/bin/env python3

import subprocess
import sys
import pathlib
import json
import argparse
import datetime

# --- Configuration ---

# Directory structure expectations
EXPERIMENT_PREFIX = "Exp"
TEST_DIR_NAME = "tests"
AUTOGRADING_JSON_PATH = ".github/classroom/autograding.json" # Optional: Load points from here

# Default points if autograding.json isn't found or parsed
# These should ideally match the points in autograding.json, excluding setup steps
DEFAULT_POINTS_CONFIG = {
    "Exp1_QuadraticRoots": 25, # Example: sum of float64/float32 tests
    "Exp2_NumericalDifferentiation": 15,
    "Exp3_NumericalIntegration": 15,
    "Exp4_HarmonicSum": 14,
    "Exp5_SeriesComparison": 20,
    "Exp6_BesselRecursion": 20,
}

# --- Helper Functions ---

def load_points_from_autograding(json_path: pathlib.Path) -> dict:
    """
    Attempts to load test points from the autograding.json file.
    This is a simplified parser focusing on test names and points.
    It tries to map the test 'name' to an experiment directory.
    """
    points_config = {}
    total_points = 0
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        tests = data.get("tests", [])
        for test in tests:
            name = test.get("name", "")
            points = test.get("points", 0)
            run_cmd = test.get("run", "")
            
            # Try to infer the experiment directory from the name or run command
            # This is heuristic and might need adjustment based on naming conventions
            exp_name = None
            if EXPERIMENT_PREFIX in name:
                 # Example: "Exp1: Quadratic Roots Tests" -> "Exp1_QuadraticRoots" (needs mapping)
                 # Example: "Exp1_QuadraticRoots Tests" -> "Exp1_QuadraticRoots"
                 parts = name.split(':')[0].split(' ')[0] # Simplistic extraction
                 if parts.startswith(EXPERIMENT_PREFIX):
                     # This part is tricky, needs a reliable mapping from test name to dir name
                     # Let's try mapping based on the run command instead if possible
                     pass # Skip name-based for now unless very consistent

            if not exp_name and TEST_DIR_NAME in run_cmd:
                 # Example: "pytest Exp1_QuadraticRoots/tests/..."
                 path_part = run_cmd.split(TEST_DIR_NAME)[0]
                 potential_exp_name = path_part.split()[-1].strip('/').strip('\\')
                 if potential_exp_name.startswith(EXPERIMENT_PREFIX):
                     exp_name = potential_exp_name

            if exp_name and points is not None:
                 # If multiple tests run on the same experiment, sum the points
                 points_config[exp_name] = points_config.get(exp_name, 0) + points
                 print(f"  -> Found config for {exp_name} in {json_path.name}: {points} points (cumulative: {points_config[exp_name]})")

        if not points_config:
             print(f"Warning: Could not reliably parse points per experiment from {json_path.name}.")
             return None
             
        print(f"Successfully loaded points configuration from {json_path.name}")
        return points_config

    except FileNotFoundError:
        print(f"Info: {json_path.name} not found.")
        return None
    except (json.JSONDecodeError, KeyError, Exception) as e:
        print(f"Warning: Failed to parse {json_path.name}: {e}")
        return None


def run_tests_for_experiment(exp_dir: pathlib.Path, verbose: bool = False):
    """
    Runs pytest for a given experiment directory and returns results.
    """
    test_dir = exp_dir / TEST_DIR_NAME
    exp_name = exp_dir.name
    print(f"\n--- Running tests for: {exp_name} ---")

    if not exp_dir.is_dir():
        print(f"ERROR: Experiment directory '{exp_dir}' not found.")
        return False, 0, "Experiment directory missing", ""
        
    if not test_dir.is_dir():
        print(f"ERROR: Test directory '{test_dir}' not found.")
        return False, 0, "Test directory missing", ""

    # Check if there are any test files
    test_files = list(test_dir.glob('test_*.py'))
    if not test_files:
        print(f"WARNING: No test files (test_*.py) found in '{test_dir}'. Skipping.")
        # Treat as passed with 0 points? Or failed? Let's say passed but worth 0.
        return True, 0, "No test files found", "" # Success=True, but points=0

    # Ensure pytest is available
    try:
        subprocess.run([sys.executable, "-m", "pytest", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
         print("ERROR: pytest not found or not runnable. Make sure it's installed in the environment.")
         return False, 0, "pytest not found", ""

    # Construct and run the pytest command
    # Use sys.executable to ensure using the correct python environment
    cmd = [sys.executable, "-m", "pytest", "-v" if verbose else "-q", str(test_dir)]
    print(f"Executing: {' '.join(cmd)}")

    try:
        # Run pytest. We don't use check=True so we can capture failures.
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')

        success = result.returncode == 0
        exit_code = result.returncode
        stdout = result.stdout
        stderr = result.stderr

        if success:
            print(f"Result: PASSED (exit code {exit_code})")
            if verbose:
                print("--- pytest stdout ---")
                print(stdout)
        else:
            print(f"Result: FAILED (exit code {exit_code})")
            # Always print output on failure for debugging
            print("--- pytest stdout ---")
            print(stdout)
            if stderr:
                print("--- pytest stderr ---")
                print(stderr)

        return success, exit_code, stdout, stderr

    except Exception as e:
        print(f"ERROR: An unexpected error occurred while running pytest for {exp_name}: {e}")
        return False, -1, "", str(e) # Indicate failure with a special exit code maybe

# --- Main Execution ---

def main():
    parser = argparse.ArgumentParser(description="Run pytest tests for Computational Physics experiments and calculate score.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity for pytest runs.")
    parser.add_argument("--points-file", type=str, default=AUTOGRADING_JSON_PATH, help="Path to the autograding JSON file to load points from.")
    parser.add_argument("--use-defaults", action="store_true", help="Force using the default points configuration instead of the JSON file.")
    args = parser.parse_args()

    base_dir = pathlib.Path.cwd()
    print(f"Running grading script in: {base_dir}")

    # Determine points configuration
    points_config = None
    if not args.use_defaults:
        print(f"Attempting to load points from: {args.points_file}")
        points_config = load_points_from_autograding(pathlib.Path(args.points_file))
    
    if points_config is None:
        print("Using default points configuration.")
        points_config = DEFAULT_POINTS_CONFIG
        
    if not points_config:
         print("ERROR: No points configuration found or defined. Exiting.")
         sys.exit(1)

    total_possible_points = sum(points_config.values())
    print(f"Total possible points based on configuration: {total_possible_points}")

    # Discover experiment directories
    experiment_dirs = sorted([d for d in base_dir.glob(f"{EXPERIMENT_PREFIX}*") if d.is_dir()])
    if not experiment_dirs:
        print(f"ERROR: No experiment directories found matching '{EXPERIMENT_PREFIX}*'.")
        print("Make sure you are running this script from the root of the assignment directory.")
        sys.exit(1)
        
    print(f"Found experiment directories: {[d.name for d in experiment_dirs]}")

    # Run tests and collect results
    total_earned_points = 0
    results_summary = {}

    for exp_dir in experiment_dirs:
        exp_name = exp_dir.name
        
        if exp_name not in points_config:
            print(f"\n--- Skipping: {exp_name} (no points configured) ---")
            results_summary[exp_name] = {"status": "SKIPPED", "points_earned": 0, "points_possible": 0}
            continue

        points_possible = points_config[exp_name]
        success, exit_code, stdout, stderr = run_tests_for_experiment(exp_dir, args.verbose)
        
        points_earned = points_possible if success else 0
        total_earned_points += points_earned
        
        results_summary[exp_name] = {
            "status": "PASSED" if success else "FAILED",
            "points_earned": points_earned,
            "points_possible": points_possible,
            "exit_code": exit_code,
            # Optionally store stdout/stderr for later inspection
            # "stdout": stdout,
            # "stderr": stderr
        }
        print(f"Points awarded for {exp_name}: {points_earned} / {points_possible}")


    # Print final summary
    print("\n" + "="*40)
    print(" " * 12 + "GRADING SUMMARY")
    print("="*40)
    for name, result in results_summary.items():
         print(f"{name:<30}: {result['status']:<8} ({result['points_earned']:>3} / {result['points_possible']:>3} points)")
         if result['status'] == "FAILED":
              print(f"  (Pytest exit code: {result['exit_code']})")
              
    print("-"*40)
    print(f"{'TOTAL SCORE':<30}: {total_earned_points:>10} / {total_possible_points:>3} points")
    print("="*40)

    # Exit with a non-zero code if any tests failed, useful for CI
    if total_earned_points < total_possible_points:
         # Check if any test actually failed vs just being skipped or having 0 points
         any_failures = any(res['status'] == 'FAILED' for res in results_summary.values())
         if any_failures:
              # sys.exit(1) # Uncomment if you want the script to signal failure
              pass
    
    # 在打印最终摘要后添加以下代码
    print("\n" + "="*40)
    
    # 生成汇总文件
    generate_summary_file(results_summary, total_earned_points, total_possible_points)

def generate_summary_file(results, earned, possible):
    """生成测试结果汇总文件(Markdown格式)"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary_file = pathlib.Path.cwd() / "grading_summary.md"
    
    with open(summary_file, 'w') as f:
        # 写入标题和时间
        f.write(f"# 实验评分报告\n\n")
        f.write(f"**生成时间**: {timestamp}\n\n")
        f.write(f"**总分**: {earned}/{possible}\n\n")
        
        # 写入表格标题
        f.write("| 实验名称 | 状态 | 得分 | 退出代码 |\n")
        f.write("|----------|------|------|----------|\n")
        
        # 写入每个实验的结果
        for exp_name, result in results.items():
            status = "✅ 通过" if result["status"] == "PASSED" else "❌ 失败"
            score = f"{result['points_earned']}/{result['points_possible']}"
            exit_code = result["exit_code"]
            f.write(f"| {exp_name} | {status} | {score} | {exit_code} |\n")
        
        # 写入总结
        f.write(f"\n**最终得分**: {earned}/{possible} ({round(earned/possible*100, 2)}%)\n")
    
    print(f"测试结果汇总已保存到: {summary_file}")

if __name__ == "__main__":
    main()