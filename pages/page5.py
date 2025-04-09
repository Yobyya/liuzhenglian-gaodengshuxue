import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import latex


st.set_page_config(page_title="定积分计算器", page_icon="🧮", layout="centered")
st.title("5.1 定积分计算器")
st.markdown("""
<style>
div[data-testid="stExpander"] div[role="button"] p {
    font-size: 1.2rem;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

if 'integral_expr' not in st.session_state:
    st.session_state.integral_expr = "x**2"
if 'lower_limit' not in st.session_state:
    st.session_state.lower_limit = "0"
if 'upper_limit' not in st.session_state:
    st.session_state.upper_limit = "1"

# 侧边栏
with st.sidebar:
    st.header("📋 使用指南")
    with st.expander("点击查看说明"):
        st.markdown("""
        1. 在下方输入被积函数(关于x的表达式)
        2. 输入积分上下限
        3. 支持的功能：
           - 基本运算：+ - * / **
           - 常用函数：sin, cos, tan, exp, log, sqrt等
           - 支持π(pi)和e常数
        4. 点击"计算"按钮得到结果
        """)
    st.divider()
    st.markdown("**示例表达式**")
    cols = st.columns(2)

    with cols[1]:
        if st.button("三角函数", help="sin(x)*cos(x)"):
            st.session_state.integral_expr = "sin(x)*cos(x)"
    with cols[0]:
        if st.button("指数函数", help="exp(-x**2)"):
            st.session_state.integral_expr = "exp(-x**2)"

# 主界面
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("输入参数:")
    # 函数表达式输入
    integral_expr = st.text_input(
        "被积函数 f(x) =",
        st.session_state.integral_expr,
        key="expr_input"
    )

    # 积分限输入
    col_a, col_b = st.columns(2)
    with col_a:
        lower_limit = st.text_input("下限 a", st.session_state.lower_limit)
    with col_b:
        upper_limit = st.text_input("上限 b", st.session_state.upper_limit)

    # 计算按钮
    if st.button("🚀 计算定积分", use_container_width=True):
        st.session_state.integral_expr = integral_expr
        st.session_state.lower_limit = lower_limit
        st.session_state.upper_limit = upper_limit

with col2:
    st.subheader("📊 函数图像预览")
    try:
        x = sp.Symbol('x')
        f = sp.sympify(integral_expr)
        f_numeric = sp.lambdify(x, f, "numpy")

        a = float(sp.sympify(lower_limit).evalf())
        b = float(sp.sympify(upper_limit).evalf())
        x_vals = np.linspace(min(a, b) - 1, max(a, b) + 1, 500)
        y_vals = f_numeric(x_vals)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x_vals, y_vals, label=f"${latex(f)}$", color="#1f77b4")
        ax.fill_between(x_vals, y_vals, where=[(x >= a) & (x <= b) for x in x_vals],
                        color="#1f77b4", alpha=0.3)
        ax.axvline(x=a, color='red', linestyle='--')
        ax.axvline(x=b, color='red', linestyle='--')
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    except:
        st.warning("⚠️ 输入有效的表达式后可显示图像")


if st.session_state.integral_expr:
    try:
        st.divider()
        st.subheader("📌 计算结果")

        x = sp.Symbol('x')
        f = sp.sympify(st.session_state.integral_expr)
        a = sp.sympify(st.session_state.lower_limit)
        b = sp.sympify(st.session_state.upper_limit)

        integral_value = sp.integrate(f, (x, a, b))
        numerical_value = integral_value.evalf()

        # 显示结果 - 修复LaTeX渲染问题
        cols = st.columns(3)
        with cols[0]:
            st.markdown("**被积函数**")
            st.latex(f" {latex(f)}")
        with cols[1]:
            st.markdown("**积分区间**")
            st.latex(rf"\left[{latex(a)}, {latex(b)}\right]")
        with cols[2]:
            st.markdown("**积分结果**")
            try:
                st.latex(rf"{latex(integral_value)} \approx {numerical_value:.6f}")
            except:
                st.latex(rf"\approx {numerical_value:.6f}")

        # 显示计算步骤
        with st.expander("🔍 查看详细计算步骤", expanded=False):
            st.latex(rf"\int_{{{latex(a)}}}^{{{latex(b)}}} {latex(f)} \, dx = {latex(integral_value)}")
            st.write(f"数值结果: {numerical_value:.6f}")

    except Exception as e:
        st.error(f"计算错误: {str(e)}")

st.markdown("---")
st.header("函数图像")
plot_func = st.text_input("输入要绘制的函数", "exp(-x)*sin(x)")
x_min = st.number_input("x最小值", value=0.0)
x_max = st.number_input("x最大值", value=5.0)

try:
    if st.button("绘制图像"):
        f_plot = sp.lambdify(x, sp.sympify(plot_func), "numpy")
        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = f_plot(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True)
        st.pyplot(fig)
except:
    st.error("函数表达式有误，请检查！")