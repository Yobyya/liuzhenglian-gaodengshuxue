import math

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

st.title("3.1 拉格朗日中值定理计算器")
# 用户输入区间 a 和 b
a = st.number_input("请输入区间的下限 a", value=1)
b = st.number_input("请输入区间的上限 b", value=2)
# 用户输入函数 f(x)
input_function = st.text_input("请输入函数 f(x) (例如: x**2)", "x**2")
# 定义符号变量
x, xi = sp.symbols('x xi')
try:
    # 使用 sympy 解析输入的函数表达式
    f = sp.sympify(input_function)
    # 计算 f(b) - f(a)
    f_b_minus_f_a = f.subs(x, b) - f.subs(x, a)
    # 求函数 f(x) 的导数
    f_prime = sp.diff(f, x)
    # 根据拉格朗日中值定理列方程 f(b) - f(a) = f'(xi) * (b - a)
    equation = sp.Eq(f_b_minus_f_a, f_prime.subs(x, xi) * (b - a))
    # 解方程求 xi
    solutions = sp.solve(equation, xi)
    # 筛选出在区间 (a, b) 内的解
    valid_solutions = [s for s in solutions if a < s < b]
    # 显示结果
    st.write(f"函数 f(x) = {f} 在区间 [{a}, {b}] 上满足拉格朗日中值定理的 ξ 值为: {valid_solutions}")

except Exception as e:
    st.error(f"无法解析输入的函数: {e}")


st.title("3.2 洛必达法则极限计算器")
# 用户输入分子函数和分母函数
numerator_input = st.text_input("请输入分子函数 f(x) (例如: sin(x))", "sin(x)")
denominator_input = st.text_input("请输入分母函数 g(x) (例如: x)", "x")
x = sp.symbols('x')
try:
    # 使用 sympy 解析用户输入的分子和分母函数
    f = sp.sympify(numerator_input)
    g = sp.sympify(denominator_input)
    # 计算原极限
    original_limit = sp.limit(f / g, x, 0)
    # 对分子和分母分别求导
    f_prime = sp.diff(f, x)
    g_prime = sp.diff(g, x)
    # 使用洛必达法则后的极限
    lhopital_limit = sp.limit(f_prime / g_prime, x, 0)

    st.write(f"原极限 lim(x->0) {f}/{g} 的值为: {original_limit}")
    st.write(f"使用洛必达法则后极限 lim(x->0) {f_prime}/{g_prime} 的值为: {lhopital_limit}")
except Exception as e:
    st.error(f"无法解析输入的函数: {e}")

st.title("3.3 泰勒展开式计算器")
# 用户输入函数、展开点和展开阶数
function_input = st.text_input("请输入函数 f(x) (例如: exp(x))", "exp(x)")
x0_input = st.number_input("请输入展开点 x0", value=0)
n_input = st.number_input("请输入展开阶数 n", value=3, min_value=1)
# 定义符号变量
x = sp.symbols('x')
try:
    # 使用 sympy 解析用户输入的函数
    f = sp.sympify(function_input)
    # 计算泰勒展开式
    taylor_expansion = sp.series(f, x, x0_input, n_input + 1).removeO()
    # 用户输入要计算的 x 值
    x_value = st.number_input("请输入要计算的 x 值", value=0.5)
    # 计算泰勒展开式在 x = x_value 处的值
    approx_value = taylor_expansion.subs(x, x_value)
    actual_value = math.exp(x_value)
    # 显示结果
    st.write(f"函数 {f} 在 x = {x0_input} 处的 {n_input} 阶泰勒展开式为:")
    st.latex(f"{taylor_expansion}")
    st.write(f"使用泰勒展开式计算 e^{x_value} 的近似值为: {approx_value}")
    st.write(f"e^{x_value} 的实际值为: {actual_value}")

except Exception as e:
    st.error(f"无法解析输入的函数: {e}")

# 设置页面标题
st.title("高等函数凹凸性分析")
# 用户输入函
function_input = st.text_input("请输入函数 f(x) (例如: sin(x), exp(x), x**3 + x**2 + 1)", "x**3 + x**2 + 1")
# 用户输入区间
x_min = st.number_input("请输入 x 的最小值", value=-10)
x_max = st.number_input("请输入 x 的最大值", value=10)
# 用户选择采样点数
num_points = st.number_input("请输入采样点数", value=100)
# 用户选择显示的阶数（默认计算二阶导数）
compute_order = st.selectbox("选择需要计算的导数阶数", [1, 2, 3, 4])

# 定义符号变量
x = sp.symbols('x')

# 解析函数
try:
    f = sp.sympify(function_input)

    # 计算相应阶数的导数
    derivative = f
    for i in range(compute_order):
        derivative = sp.diff(derivative, x)

    # 显示导数的表达式
    st.write(f"函数的 {compute_order} 阶导数为:")
    st.latex(f"{derivative}")
    # 将导数转化为可执行的函数
    derivative_func = sp.lambdify(x, derivative, "numpy")

    # 生成 x 值并计算相应的 y 值
    x_vals = np.linspace(x_min, x_max, num_points)
    y_vals = derivative_func(x_vals)
    # 绘制图像
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'{compute_order} 阶导数的图像', color='blue')

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel(f"{compute_order} 阶导数")
    ax.set_title(f"函数 {function_input} 的 {compute_order} 阶导数图像")

    st.pyplot(fig)

    # 分析凹凸性
    if compute_order == 2:
        # 当阶数为2时，可以直接分析凹凸性
        critical_points = sp.solveset(derivative, x, domain=sp.S.Reals)
        st.write("二阶导数为零的临界点:")
        st.latex(f"{critical_points}")

        # 函数的凹凸性分析
        concave_up = "凹" if np.all(y_vals > 0) else "凸"
        concave_down = "凸" if np.all(y_vals < 0) else "凹"
        st.write(f"该函数的凹凸性在该区间内可能为: {concave_up} 或 {concave_down}")

except Exception as e:
    st.error(f"无法解析输入的函数: {e}")
