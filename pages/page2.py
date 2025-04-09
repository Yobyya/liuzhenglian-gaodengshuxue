import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 导数计算器
st.header("2.1 导数计算器")
func_input = st.text_input("输入函数（例：x**2）", "x**2")
x_var = sp.symbols('x')
try:
    func = sp.sympify(func_input)
    derivative = sp.diff(func, x_var)
    st.write(f"导数结果：{sp.latex(derivative)}")
except Exception as e:
    st.error(f"公式错误：{str(e)}")

st.title("2.2 符号求导计算器")
input_function = st.text_input("请输入一个符号函数 (例如: (x**2 + 1)*(x + 2))", "(x**2 + 1)*(x + 2)")
x = sp.symbols('x')
try:
    y = sp.sympify(input_function)

    y_prime = sp.diff(y, x)

    y_prime_expanded = sp.expand(y_prime)
    # 显示结果
    st.write(f"函数 y = {y} 的导数为: {y_prime_expanded}")
except Exception as e:
    st.error(f"无法解析输入的函数: {e}")


st.title("2.3 高阶导数计算器")
# 用户输入符号函数
input_function = st.text_input("请输入一个符号函数 (例如: x**3)", "x**3")
x = sp.symbols('x')

try:
    # 使用 sympy 解析输入的函数表达式
    y = sp.sympify(input_function)
    # 计算一阶导数
    first_derivative = sp.diff(y, x)
    # 计算二阶导数
    second_derivative = sp.diff(y, x, 2)
    # 计算三阶导数
    third_derivative = sp.diff(y, x, 3)
    # 计算四阶导数
    fourth_derivative = sp.diff(y, x, 4)

    # 展开导数表达式
    first_derivative_expanded = sp.expand(first_derivative)
    second_derivative_expanded = sp.expand(second_derivative)
    third_derivative_expanded = sp.expand(third_derivative)
    fourth_derivative_expanded = sp.expand(fourth_derivative)

    # 显示结果
    st.write(f"函数 y = {y} 的一阶导数为: {first_derivative_expanded}")
    st.write(f"函数 y = {y} 的二阶导数为: {second_derivative_expanded}")
    st.write(f"函数 y = {y} 的三阶导数为: {third_derivative_expanded}")
    st.write(f"函数 y = {y} 的四阶导数为: {fourth_derivative_expanded}")
except Exception as e:
    st.error(f"无法解析输入的函数: {e}")



# 隐函数导数
st.header("2.4 隐函数导数")
eq_input = st.text_input("输入隐函数方程（例：x**2 + y**2 -25）", "x**2 + y**2 -25")
try:
    eq = sp.sympify(eq_input)
    dy_dx = sp.diff(eq, sp.Symbol('y')) / sp.diff(eq, sp.Symbol('x'))
    st.write(f"dy/dx = {sp.latex(dy_dx)}")
except Exception as e:
    st.error(f"方程错误：{str(e)}")



st.title("2.5 微分计算器")
input_function = st.text_input("请输入一个符号函数 (例如: x**2)", "x**2")
# 用户输入 x 和 Δx 值
x_value = st.number_input("请输入 x 的值", value=3)
_x = st.number_input("请输入 Δx 的值", value=0.01)
x = sp.symbols('x')

try:
    # 使用 sympy 解析输入的函数表达式
    y = sp.sympify(input_function)
    # 求函数的导数
    y_prime = sp.diff(y, x)
    # 计算 x = x_value 时的导数值
    derivative_value = y_prime.subs(x, x_value)
    # 计算微分
    dy = derivative_value * _x
    # 显示结果
    st.write(f"函数 y = {y} 的导数为: {y_prime}")
    st.write(f"在 x = {x_value} 处的导数值为: {derivative_value}")
    st.write(f"当 Δx = {_x} 时，微分 dy = {dy}")
except Exception as e:
    st.error(f"无法解析输入的函数: {e}")