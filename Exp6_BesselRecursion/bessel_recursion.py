import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn

def bessel_up(x, lmax):
    """向上递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 在此实现向上递推算法
    # 1. 初始化结果数组
    # 2. 计算j_0(x)和j_1(x)作为初始值
    # 3. 使用递推公式计算高阶函数值
    pass

def bessel_down(x, lmax, m_start=None):
    """向下递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        m_start: int, 起始阶数，默认为lmax + 15
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 在此实现向下递推算法
    # 1. 设置合适的起始阶数m_start
    # 2. 初始化临时数组
    # 3. 设置初始值j_{m_start+1}和j_{m_start}
    # 4. 向下递推计算
    # 5. 使用j_0(x)进行归一化
    pass

def plot_comparison(x, lmax):
    """绘制不同方法计算结果的比较图
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
    """
    l = np.arange(lmax + 1)
    
    # 计算三种方法的结果
    j_up = bessel_up(x, lmax)
    j_down = bessel_down(x, lmax)
    j_scipy = spherical_jn(l, x)
    
    # 绘制函数值的半对数图
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.semilogy(l, np.abs(j_up), 'o-', label='Up', alpha=0.7)
    plt.semilogy(l, np.abs(j_down), 's--', label='Down', alpha=0.7)
    plt.semilogy(l, np.abs(j_scipy), 'k-', label='Scipy', alpha=0.7)
    plt.grid(True)
    plt.xlabel('l')
    plt.ylabel('|j_l(x)|')
    plt.title(f'x = {x}')
    plt.legend()
    
    # 绘制相对误差的半对数图
    plt.subplot(122)
    err_up = np.abs((j_up - j_scipy) / j_scipy)
    err_down = np.abs((j_down - j_scipy) / j_scipy)
    plt.semilogy(l, err_up, 'o-', label='Up Error', alpha=0.7)
    plt.semilogy(l, err_down, 's--', label='Down Error', alpha=0.7)
    plt.grid(True)
    plt.xlabel('l')
    plt.ylabel('Relative Error')
    plt.title(f'x = {x}')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(f'bessel_x{x}.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """主函数"""
    # 设置参数
    lmax = 25
    x_values = [0.1, 1.0, 10.0]
    
    # 对每个x值进行计算和绘图
    for x in x_values:
        plot_comparison(x, lmax)
        
        # 打印特定阶数的结果
        l_check = [3, 5, 8]
        print(f"\nx = {x}:")
        print("l\tUp\t\tDown\t\tScipy")
        print("-" * 50)
        for l in l_check:
            j_up = bessel_up(x, l)[l]
            j_down = bessel_down(x, l)[l]
            j_scipy = spherical_jn(l, x)
            print(f"{l}\t{j_up:.6e}\t{j_down:.6e}\t{j_scipy:.6e}")

if __name__ == "__main__":
    main()