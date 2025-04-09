import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import sympy as sp
from sympy import latex

# 页面设置
st.set_page_config(page_title="定积分的几何应用", layout="centered")
st.title("6.2 定积分在几何上的应用")


st.header("一、平面图形的面积", divider="rainbow")

st.markdown("""
### 基本概念
定积分可以用来计算平面图形的面积，主要有两种情况：
1. 由曲线 y = f(x) 与 x 轴、直线 x=a 和 x=b 围成的区域
2. 由两条曲线 y = f(x) 和 y = g(x) 围成的区域
""")


# 理论公式
with st.expander("📖 面积计算公式", expanded=True):
    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
        **情况1**：曲线与x轴之间的面积
        $$ A = \int_{a}^{b} |f(x)| \, dx $$
        """)
        # 可视化示例
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        ax1.plot(x, y, 'b-', linewidth=2)
        ax1.fill_between(x, y, where=y > 0, color='blue', alpha=0.3)
        ax1.fill_between(x, y, where=y < 0, color='red', alpha=0.3)
        ax1.set_title("曲线y=sin(x)在[0,2π]与x轴围成的面积")
        st.pyplot(fig1)

    with cols[1]:
        st.markdown("""
        **情况2**：两条曲线之间的面积
        $$ A = \int_{a}^{b} |f(x) - g(x)| \, dx $$
            """)
        # 可视化示例
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        x = np.linspace(0, 2, 100)
        y1 = x ** 2
        y2 = np.sqrt(x)
        ax2.plot(x, y1, 'b-', label='y=x²')
        ax2.plot(x, y2, 'r-', label='y=√x')
        ax2.fill_between(x, y1, y2, where=y2 > y1, color='green', alpha=0.3)
        ax2.legend()
        ax2.set_title("y=x²与y=√x之间的面积")
        st.pyplot(fig2)

# 交互式计算器
st.subheader("🔢 面积计算器")
with st.form("area_calculator"):
    col1, col2 = st.columns(2)
    with col1:
        f_expr = st.text_input("函数f(x)", "sin(x)")
        a = st.number_input("下限a", value=0.0)
    with col2:
        g_expr = st.text_input("函数g(x)(留空则为x轴)", "")
        b = st.number_input("上限b", value=np.pi)

    if st.form_submit_button("计算面积"):
        try:
            x = sp.Symbol('x')
            f = sp.sympify(f_expr)
            g = sp.sympify(g_expr) if g_expr else 0
            # 计算面积
            area = sp.integrate(abs(f - g), (x, a, b))
            # 可视化
            fig, ax = plt.subplots(figsize=(8, 4))
            x_vals = np.linspace(float(a), float(b), 100)
            f_func = sp.lambdify(x, f, 'numpy')
            g_func = sp.lambdify(x, g, 'numpy')

            y_f = f_func(x_vals)
            y_g = g_func(x_vals)

            ax.plot(x_vals, y_f, 'b-', label=f'${latex(f)}$')
            ax.plot(x_vals, y_g, 'r-', label=f'${latex(g)}$' if g_expr else 'y=0')
            ax.fill_between(x_vals, y_f, y_g, where=y_f > y_g, color='blue', alpha=0.3)
            ax.fill_between(x_vals, y_f, y_g, where=y_g > y_f, color='red', alpha=0.3)
            ax.legend()
            ax.set_title(f"面积 = {area.evalf():.4f}")
            st.pyplot(fig)

            st.success(f"计算成功！面积为: {area.evalf():.6f}")
        except Exception as e:
            st.error(f"计算错误: {str(e)}")

''
''
if True:
    st.header("二、体积计算", divider="rainbow")

    st.markdown("""
        ### 旋转体体积
        定积分可以用来计算旋转体的体积，主要有两种方法：
        1. **圆盘法**：绕x轴或y轴旋转
        2. **圆柱壳法**：适用于特定旋转情况
        """)

    with st.expander("📖 体积计算公式", expanded=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("""
                **圆盘法（绕x轴旋转）**
                $$ V = \pi \int_{a}^{b} [f(x)]^2 \, dx $$
                """)
            # 可视化示例
            fig1, ax1 = plt.subplots(figsize=(6, 4), subplot_kw={'projection': '3d'})
            x = np.linspace(0, 1, 50)
            theta = np.linspace(0, 2 * np.pi, 50)
            X, Theta = np.meshgrid(x, theta)
            Y = np.sqrt(X) * np.cos(Theta)
            Z = np.sqrt(X) * np.sin(Theta)
            ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
            ax1.set_title("y=√x绕x轴旋转")
            st.pyplot(fig1)

        with cols[1]:
            st.markdown("""
                **圆柱壳法（绕y轴旋转）**
                $$ V = 2\pi \int_{a}^{b} x |f(x)| \, dx $$
                """)
            # 可视化示例
            fig2, ax2 = plt.subplots(figsize=(6, 4), subplot_kw={'projection': '3d'})
            x = np.linspace(0, 1, 50)
            theta = np.linspace(0, 2 * np.pi, 50)
            X, Theta = np.meshgrid(x, theta)
            Y = X * np.cos(Theta)
            Z = X * np.sin(Theta) + np.sqrt(X)
            ax2.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
            ax2.set_title("y=√x绕y轴旋转")
            st.pyplot(fig2)




    # 体积计算器
    st.subheader("🔢 体积计算器")
    method = st.radio("计算方法", ["圆盘法", "圆柱壳法"])

    with st.form("volume_calculator"):
        col1, col2 = st.columns(2)
        with col1:
            f_expr = st.text_input("函数f(x)", "sqrt(x)")
            a = st.number_input("下限a", value=0.0)
        with col2:
            axis = st.selectbox("旋转轴", ["x轴", "y轴"])
            b = st.number_input("上限b", value=1.0)

        if st.form_submit_button("计算体积"):
            try:
                x = sp.Symbol('x')
                f = sp.sympify(f_expr)

                if method == "圆盘法":
                    if axis == "x轴":
                        volume = sp.pi * sp.integrate(f ** 2, (x, a, b))
                    else:
                        volume = sp.pi * sp.integrate(f ** 2, (x, a, b))
                else:  # 圆柱壳法
                    if axis == "y轴":
                        volume = 2 * sp.pi * sp.integrate(x * abs(f), (x, a, b))
                    else:
                        volume = 2 * sp.pi * sp.integrate(x * abs(f), (x, a, b))

                st.success(f"计算成功！体积为: {volume.evalf():.6f}")
            except Exception as e:
                st.error(f"计算错误: {str(e)}")
''
''
''
st.header("三、弧长计算", divider="rainbow")

st.markdown("""
    ### 平面曲线的弧长
    定积分可以用来计算平面曲线的弧长，公式为：
    $$ L = \int_{a}^{b} \sqrt{1 + [f'(x)]^2} \, dx $$
    """)

# 弧长计算示例
with st.expander("📖 弧长计算示例", expanded=True):
    cols = st.columns(2)
    with cols[0]:
        st.markdown("**示例1**：直线段")
        st.latex(r"y = 2x + 1 \quad [0,1]")
        st.latex(r"L = \int_{0}^{1} \sqrt{1 + 2^2} \, dx = \sqrt{5} \approx 2.236")

    with cols[1]:
        st.markdown("**示例2**：半圆")
        st.latex(r"y = \sqrt{1-x^2} \quad [-1,1]")
        st.latex(r"L = \pi \approx 3.1416")

# 弧长计算器
st.subheader("🔢 弧长计算器")
with st.form("arc_length_calculator"):
    col1, col2 = st.columns(2)
    with col1:
        f_expr = st.text_input("函数f(x)", "sin(x)")
        a = st.number_input("下限a", value=0.0)
    with col2:
        b = st.number_input("上限b", value=np.pi)

    if st.form_submit_button("计算弧长"):
        try:
            x = sp.Symbol('x')
            f = sp.sympify(f_expr)
            df = sp.diff(f, x)

            # 计算弧长
            arc_length = sp.integrate(sp.sqrt(1 + df ** 2), (x, a, b))

            # 可视化
            fig, ax = plt.subplots(figsize=(8, 4))
            x_vals = np.linspace(float(a), float(b), 100)
            f_func = sp.lambdify(x, f, 'numpy')
            y_vals = f_func(x_vals)

            ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'${latex(f)}$')
            ax.set_title(f"曲线弧长 = {arc_length.evalf():.4f}")
            ax.legend()
            st.pyplot(fig)

            st.success(f"计算成功！弧长为: {arc_length.evalf():.6f}")
        except Exception as e:
            st.error(f"计算错误: {str(e)}")
