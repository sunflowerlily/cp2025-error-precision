import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    """
    被积函数 f(x) = sqrt(1-x^2)
    
    参数:
        x: 自变量值或数组
    
    返回:
        函数值
    """
    # 在此实现 f(x) = sqrt(1-x^2)
    pass

def rectangle_method(f, a, b, N):
    """
    矩形法（左矩形法）计算积分
    
    参数:
        f: 被积函数
        a, b: 积分区间
        N: 子区间数量
    
    返回:
        积分近似值
    """
    # 在此实现矩形法（左矩形法）计算积分
    # 1. 计算步长 h = (b-a)/N
    # 2. 对每个子区间的左端点计算函数值并求和
    pass

def trapezoid_method(f, a, b, N):
    """
    梯形法计算积分
    
    参数:
        f: 被积函数
        a, b: 积分区间
        N: 子区间数量
    
    返回:
        积分近似值
    """
    # 在此实现梯形法计算积分
    # 1. 计算步长 h = (b-a)/N
    # 2. 计算首末项 0.5 * (f(a) + f(b))
    # 3. 计算中间项之和
    # 4. 用步长h乘以总和
    pass

def calculate_errors(a, b, exact_value):
    """计算不同N值下各方法的误差"""
    N_values = [10, 100, 1000, 10000]
    h_values = [(b - a) / N for N in N_values]
    
    rect_errors = []
    trap_errors = []
    
    for N in N_values:
        # 矩形法
        rect_result = rectangle_method(f, a, b, N)
        rect_error = abs((rect_result - exact_value) / exact_value)
        rect_errors.append(rect_error)
        
        # 梯形法
        trap_result = trapezoid_method(f, a, b, N)
        trap_error = abs((trap_result - exact_value) / exact_value)
        trap_errors.append(trap_error)
    
    return N_values, h_values, rect_errors, trap_errors

def plot_errors(h_values, rect_errors, trap_errors):
    """绘制误差-步长关系图"""
    plt.figure(figsize=(10, 6))
    
    # 绘制误差曲线
    plt.loglog(h_values, rect_errors, 'o-', label='Rectangle Method', alpha=0.5)
    plt.loglog(h_values, trap_errors, 's--', label='Trapezoid Method', alpha=0.5)
    
    # 添加参考线
    plt.loglog(h_values, np.array(h_values), '--', label='O(h)')
    plt.loglog(h_values, np.array(h_values)**2, '--', label='O(h²)')
    
    # 设置图表
    plt.xlabel('Step Size (h)')
    plt.ylabel('Relative Error')
    plt.title('Error vs Step Size in Numerical Integration')
    plt.grid(True, which="both", ls="-")
    plt.legend()
    
    plt.savefig('error_vs_stepsize_integration.png', dpi=300)
    plt.show()

def print_results(N_values, rect_results, trap_results, exact_value):
    """打印计算结果表格"""
    print("N\t矩形法\t\t梯形法\t\t精确值")
    print("-" * 60)
    
    for i in range(len(N_values)):
        print(f"{N_values[i]}\t{rect_results[i]:.8f}\t{trap_results[i]:.8f}\t{exact_value:.8f}")
    
    print("\n相对误差:")
    print("N\t矩形法\t\t梯形法")
    print("-" * 40)
    
    for i in range(len(N_values)):
        rect_error = abs((rect_results[i] - exact_value) / exact_value)
        trap_error = abs((trap_results[i] - exact_value) / exact_value)
        print(f"{N_values[i]}\t{rect_error:.8e}\t{trap_error:.8e}")

def main():
    """主函数"""
    a, b = 0, 1.0  # 积分区间
    exact_value = 0.25 * np.pi  # 精确值
    
    print(f"计算积分 ∫_{a}^{b} √(1-x²) dx")
    print(f"精确值: {exact_value:.10f}")
    
    # 计算不同N值下的结果
    N_values = [10, 100, 1000, 10000]
    rect_results = []
    trap_results = []
    
    for N in N_values:
        rect_results.append(rectangle_method(f, a, b, N))
        trap_results.append(trapezoid_method(f, a, b, N))
    
    # 打印结果
    print_results(N_values, rect_results, trap_results, exact_value)
    
    # 计算误差
    _, h_values, rect_errors, trap_errors = calculate_errors(a, b, exact_value)
    
    # 绘制误差图
    plot_errors(h_values, rect_errors, trap_errors)

if __name__ == "__main__":
    main()