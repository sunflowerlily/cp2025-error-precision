# 计算物理实验 - 第八周：深入探究数值计算中的误差与精度

## 简介

欢迎参与本周的计算物理实验！本周我们将深入探讨数值计算的核心挑战之一：**误差与精度**。理论上的完美数学公式在计算机的有限精度世界中执行时，会不可避免地引入各种误差，如**截断误差**（由算法近似引起）和**舍入误差**（由有限的数字表示引起）。这些误差的累积和放大可能导致计算结果严重偏离真实值，甚至产生完全错误的结论——这就是误差的“危害”。本周的系列实验旨在通过具体案例，让大家亲身体验这些现象，理解其背后的原理，并学习评估和控制误差的方法。

## 学习目标

完成本周实验后，你应该能够：

1.  识别和区分截断误差与舍入误差的主要来源。
2.  理解并演示灾难性抵消 (Catastrophic Cancellation) 如何导致精度急剧下降。
3.  分析数值微分中步长选择对总误差的影响，找到最佳平衡点。
4.  比较不同数值积分方法的收敛速度和精度。
5.  认识到简单求和顺序的改变如何影响舍入误差的累积。
6.  理解数学上等价的表达式在数值计算中可能具有截然不同的稳定性和精度。
7.  体验递推关系中的数值不稳定性，并了解稳定计算的策略。
8.  熟练使用 Python (NumPy, Matplotlib, SciPy) 实现数值算法、进行误差分析和结果可视化。
9.  利用 Git 和 GitHub Classroom 进行代码管理、协作（如有）与提交。

## 实验内容

本周包含以下六个实验，每个实验都聚焦于误差与精度的一个特定方面：

1.  **实验一：二次方程求根的稳定性 (Exp1_QuadraticRoots)**
    *   **核心问题:** 灾难性抵消。
    *   **任务:** 实现并比较标准求根公式与数值稳定公式在特定情况下的精度差异，特别是在单精度和双精度下。

2.  **实验二：数值微分的误差权衡 (Exp2_NumericalDifferentiation)**
    *   **核心问题:** 截断误差 vs. 舍入误差。
    *   **任务:** 使用有限差分法计算导数，并通过绘制误差-步长关系图（log-log），观察并解释误差随步长变化的 V 形曲线。

3.  **实验三：数值积分的收敛性 (Exp3_NumericalIntegration)**
    *   **核心问题:** 截断误差与算法阶数。
    *   **任务:** 实现梯形法则和辛普森法则，计算已知定积分，绘制误差-步长关系图（log-log），验证不同方法的收敛阶数。

4.  **实验四：调和级数求和顺序 (Exp4_HarmonicSum)**
    *   **核心问题:** 舍入误差累积。
    *   **任务:** 计算 \(\sum_{n=1}^N \frac{1}{n}\) 和 \(\sum_{n=N}^1 \frac{1}{n}\)，比较两者在大 N 和不同精度下的结果差异，解释原因。

5.  **实验五：不同形式级数的比较 (Exp5_SeriesComparison)**
    *   **核心问题:** 数学等价与数值稳定性。
    *   **任务:** 计算三个数学上相关的级数 \(S_N^{(1)}, S_N^{(2)}, S_N^{(3)}\)，比较它们的数值结果和稳定性，理解表达式形式对计算精度的影响。

6.  **实验六：贝塞尔函数递推的不稳定性 (Exp6_BesselRecursion)**
    *   **核心问题:** 递推算法的数值稳定性。
    *   **任务:** 实现球贝塞尔函数的向上和向下递推关系，观察向上递推在特定条件下的发散现象，并验证向下递推的稳定性。

## 操作指南

(与上一版本类似，包括克隆、环境设置、完成实验、本地测试、撰写报告、提交步骤)
```bash
# 克隆
git clone <your-repository-url>
cd ComputationalPhysics_Errors_Precision_Assignment

# 环境 (建议使用 venv)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 本地测试 (可选)
pip install pytest
pytest Exp1_QuadraticRoots/tests/
pytest Exp2_NumericalDifferentiation/tests/
# ... etc for all experiments

# 提交
git add .
git commit -m "Completed experiments"
git push origin main
```
## 实验报告要求
建议为每个实验撰写独立的小结，或在一个总报告中为每个实验设立清晰的部分。每部分应包含：

- 目的: 简述该实验要探究的问题。
- 方法: 描述所用数值方法和关键实现细节。
- 结果: 展示计算数据、表格、图像等。
- 分析与讨论: 解释观察到的现象，与误差理论联系，讨论精度、稳定性问题。例如，解释误差来源、比较不同方法/参数/精度的优劣、说明“危害”体现在哪里。
- 结论: 总结该实验的主要发现。

## 评分
- 自动评分 (Autograding): 通过 GitHub Classroom 运行 tests/ 目录下的测试，检查代码功能和数值输出的准确性（在允许的误差范围内）。
- 手动评分: 教师/助教将审阅代码质量、实验报告的完整性、分析深度、图表清晰度及结论的合理性。

## 截止日期
[在此处填写具体的截止日期和时间]

## 资源
课堂讲义/笔记
NumPy 文档: https://numpy.org/doc/stable/
Matplotlib 文档: https://matplotlib.org/stable/contents.html
SciPy 文档 (用于参考值): https://docs.scipy.org/doc/scipy/reference/
经典教材，如 Newman 的《Computational Physics》或 Press 等人的《Numerical Recipes》。
祝大家实验顺利，在实践中掌握误差分析的精髓！

## 目录结构
```
ComputationalPhysics_Errors_Precision/
├── README.md                 # (总) 本周作业的总体说明
├── .github/
│   └── classroom/
│       └── autograding.json  # GitHub Classroom 自动评分配置文件
├── grading_script.py         # (可选) 更复杂的本地评分脚本
├── requirements.txt          # Python 依赖包 (numpy, matplotlib, scipy)
│
├── Exp1_QuadraticRoots/
│   ├── README.md             # 实验一：二次方程求根 说明
│   ├── quadratic_solver.py   # 实验一：学生代码模板
│   ├── solution/
│   │   └── quadratic_solver.py # 实验一：参考答案
│   └── tests/
│       └── test_quadratic.py # 实验一：测试代码
│
├── Exp2_NumericalDifferentiation/
│   ├── README.md             # 实验二：数值微分误差 说明
│   ├── differentiation.py    # 实验二：学生代码模板
│   ├── solution/
│   │   └── differentiation.py # 实验二：参考答案
│   └── tests/
│       └── test_differentiation.py # 实验二：测试代码
│
├── Exp3_NumericalIntegration/
│   ├── README.md             # 实验三：数值积分误差 说明
│   ├── integration.py        # 实验三：学生代码模板
│   ├── solution/
│   │   └── integration.py    # 实验三：参考答案
│   └── tests/
│       └── test_integration.py # 实验三：测试代码
│
├── Exp4_HarmonicSum/
│   ├── README.md             # 实验四：调和级数求和 说明
│   ├── harmonic_sum.py       # 实验四：学生代码模板
│   ├── solution/
│   │   └── harmonic_sum.py   # 实验四：参考答案
│   └── tests/
│       └── test_harmonic.py  # 实验四：测试代码
│
├── Exp5_SeriesComparison/
│   ├── README.md             # 实验五：不同形式级数求和 说明
│   ├── series_sum.py         # 实验五：学生代码模板
│   ├── solution/
│   │   └── series_sum.py     # 实验五：参考答案
│   └── tests/
│       └── test_series.py    # 实验五：测试代码
│
└── Exp6_BesselRecursion/
    ├── README.md             # 实验六：贝塞尔函数递推稳定性 说明
    ├── bessel_recursion.py   # 实验六：学生代码模板
    ├── solution/
    │   └── bessel_recursion.py # 实验六：参考答案
    └── tests/
        └── test_bessel.py    # 实验六：测试代码
```