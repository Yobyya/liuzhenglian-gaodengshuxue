import streamlit as st
import sympy as sp
from sympy import latex


st.title('4.1 不定积分计算器')
st.write('''
这是一个使用SymPy计算不定积分的交互式工具。
可以输入任意关于x的函数表达式，计算其不定积分结果。
''')

if 'user_input' not in st.session_state:
    st.session_state.user_input = "2*x"

with st.sidebar:
    st.header('使用说明')
    st.markdown('''
    1. 在下方输入框中输入关于x的函数表达式
    2. 支持常见数学运算：+ - * / **
    3. 支持常见函数：sin, cos, exp, log等
    ''')

col1, col2 = st.columns(2)
with col1:
    # 使用session_state来保持输入框状态
    def update_input():
        st.session_state.func_input = st.session_state.user_input


    user_input = st.text_input(
        "输入函数f(x)的表达式:",
        st.session_state.user_input,
        key="func_input",
        on_change=update_input
    )

    def set_example(example):
        st.session_state.user_input = example
        st.session_state.func_input = example

    # 使用容器防止重复渲染
    with st.container():
        st.button('示例: 三角函数',
                  on_click=set_example,
                  args=("sin(x) + cos(2*x)",))

with col2:
    with st.container():
        st.markdown("### 输入的函数:")
        st.latex(r"f(x) = " + user_input)

# 计算结果区域
result_container = st.container()

try:
    with result_container:
        x = sp.Symbol('x')
        # 将用户输入转换为SymPy表达式
        f = sp.sympify(user_input)
        # 计算不定积分
        integral = sp.integrate(f, x)

        # 显示结果
        st.divider()
        st.subheader("📌 计算结果")
        st.latex(r"\int " + latex(f) + r"\, dx = " + latex(integral) + "+ C")


except sp.SympifyError:
    with result_container:
        st.error("错误：请输入有效的数学表达式！")
except Exception as e:
    with result_container:
        st.error(f"计算时出现错误: {str(e)}")

