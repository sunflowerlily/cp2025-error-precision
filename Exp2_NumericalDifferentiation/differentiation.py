import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    定义测试函数 f(x) = x(x-1)
    
    参数:
        x: 自变量值
    
    返回:
        函数值 f(x)
    """
    # 在此实现函数 f(x) = x(x-1)
    pass

def forward_diff(f, x, delta):
    """
    前向差分法计算导数
    
    参数:
        f: 待求导函数
        x: 求导点
        delta: 步长
    
    返回:
        在点x处的导数近似值
    """
    # 在此实现前向差分公式: (f(x+delta) - f(x))/delta
    pass

def central_diff(f, x, delta):
    """
    中心差分法计算导数
    
    参数:
        f: 待求导函数
        x: 求导点
        delta: 步长
    
    返回:
        在点x处的导数近似值
    """
    # 在此实现中心差分公式: (f(x+delta) - f(x-delta))/(2*delta)
    pass

def analytical_derivative(x):
    """
    解析导数 f'(x) = 2x - 1
    
    参数:
        x: 求导点
    
    返回:
        在点x处的导数精确值
    """
    # 在此实现解析导数 f'(x) = 2x - 1
    pass

def calculate_errors(x_point=1.0):
    """
    计算不同步长下的误差
    
    参数:
        x_point: 计算导数的点，默认为1.0
    
    返回:
        deltas: 步长数组
        forward_errors: 前向差分相对误差数组
        central_errors: 中心差分相对误差数组
    """
    # 步长序列
    deltas = np.logspace(-14, -2, 13)
    
    # 解析解
    true_value = analytical_derivative(x_point)
    
    # 存储结果
    forward_errors = []
    central_errors = []
    
    # 计算不同步长下的误差
    for delta in deltas:
        # 1. 计算前向差分近似值
        # 2. 计算前向差分相对误差
        # 3. 添加到forward_errors列表
        
        # 4. 计算中心差分近似值
        # 5. 计算中心差分相对误差
        # 6. 添加到central_errors列表
        pass
    
    return deltas, forward_errors, central_errors

def plot_errors(deltas, forward_errors, central_errors):
    """
    绘制误差-步长关系图
    
    参数:
        deltas: 步长数组
        forward_errors: 前向差分相对误差数组
        central_errors: 中心差分相对误差数组
    """
    plt.figure(figsize=(10, 6))
    
    # 绘制前向差分误差
    plt.loglog(deltas, forward_errors, 'o-', label='Forward Difference')
    
    # 绘制中心差分误差
    plt.loglog(deltas, central_errors, 's-', label='Central Difference')
    
    # 添加参考线
    plt.loglog(deltas, deltas, '--', label='First Order O(h)')
    plt.loglog(deltas, np.array(deltas)**2, '--', label='Second Order O($h^2$)')
    
    # 设置图表
    plt.xlabel('Step Size $\\delta$')
    plt.ylabel('Relative Error')
    plt.title('Error vs Step Size in Numerical Differentiation')
    plt.grid(True, which="both", ls="-")
    plt.legend()
    
    # 保存图表
    plt.savefig('error_vs_stepsize.png', dpi=300)
    plt.show()

def print_results(deltas, forward_errors, central_errors):
    """
    打印计算结果表格
    
    参数:
        deltas: 步长数组
        forward_errors: 前向差分相对误差数组
        central_errors: 中心差分相对误差数组
    """
    print("步长(δ)\t前向差分误差\t中心差分误差")
    print("-" * 50)
    
    for i in range(len(deltas)):
        print(f"{deltas[i]:.2e}\t{forward_errors[i]:.6e}\t{central_errors[i]:.6e}")

def main():
    """主函数"""
    x_point = 1.0
    
    # 计算误差
    deltas, forward_errors, central_errors = calculate_errors(x_point)
    
    # 打印结果
    print(f"函数 f(x) = x(x-1) 在 x = {x_point} 处的解析导数值: {analytical_derivative(x_point)}")
    print_results(deltas, forward_errors, central_errors)
    
    # 绘制误差图
    plot_errors(deltas, forward_errors, central_errors)
    
    # 分析最优步长
    # 提示: 使用np.argmin找到误差最小的索引
    
    # 分析收敛阶数
    # 提示: 使用对数关系计算斜率

if __name__ == "__main__":
    main()