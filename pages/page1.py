import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 映射与函数示例
st.title("1.1 映射与函数")
st.markdown("### 映射示例：A→B")
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}
mapping = {1:'a', 2:'b', 3:'c', 4:'d'}

st.write("集合A:", set_A)
st.write("集合B:", set_B)
st.write("映射关系:", mapping)

st.write("### 函数测试")
element = st.selectbox("选择A中的元素", set_A)
result = mapping.get(element, "未定义")
st.write(f"元素 {element} 映射到 → {result}")

# 线性函数示例
st.header("1.2 线性函数示例")
x = st.slider("选择x值", -10, 10, 5)
y = 2 * x + 1
st.write(f"f({x}) = {y}")

# 极限可视化
st.header("1.3 函数极限可视化")
x_values = np.linspace(-10, 10, 400)
y_values = 1 / x_values

fig, ax = plt.subplots()
ax.plot(x_values, y_values)
ax.axhline(0, color='black', lw=1)
ax.set_title(r"$\lim_{x \to 0} \frac{1}{x}$")
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
st.pyplot(fig)


st.title("1.4 无穷小示例")
x_value = st.slider("选择接近 0 的 x 值", min_value=0.00001, max_value=0.1, step=0.00001, format="%.5f")
f_x = x_value
st.write(f"当 x = {x_value} 时，函数 f(x) = {f_x}")

st.title("无穷大示例")
x_value2 = st.slider("选择接近 0 的 x 值", min_value=0.00001, max_value=0.1, step=0.00001, format="%.5f",key = 11)
f_x = 1 / x_value2
st.write(f"当 x = {x_value2} 时，函数 f(x) = {f_x}")


# 定义函数 f(x)
def f(x):
    return 2 * x + 1

# 定义函数 g(x)
def g(x):
    return 3 * x - 2

# 创建一个 Streamlit 应用界面
st.title("1.5 极限法则模拟器")
st.write("""
    本应用模拟了极限加法法则、减法法则、乘法法则和除法法则。
    你可以查看不同接近 1 的 x 值下的计算结果。
""")

# 输入框用于选择 x 值列表
x_values = st.text_input("请输入一组 x 值（以逗号分隔）", "0.9, 0.99, 0.999, 1.001, 1.01, 1.1")
x_values = [float(x.strip()) for x in x_values.split(',')]

# 模拟极限加法法则
st.subheader("极限加法法则")
add_results = []
for x in x_values:
    sum_result = f(x) + g(x)
    add_results.append(f"当 x = {x} 时，\n"
                       f"f(x) + g(x) 的值为 {sum_result}\n")
st.write("\n".join(add_results))
''
# 模拟极限减法法则
st.subheader("极限减法法则")
sub_results = []
for x in x_values:
    sub_result = f(x) - g(x)
    sub_results.append(f"当 x = {x} 时，\n"
                       f"f(x) - g(x) 的值为 {sub_result}\n")
st.write("\n".join(sub_results))
''
# 模拟极限乘法法则
st.subheader("极限乘法法则")
mul_results = []
for x in x_values:
    mul_result = f(x) * g(x)
    mul_results.append(f"当 x = {x} 时，\n"
                       f"f(x) * g(x) 的值为 {mul_result}\n")
st.write("\n".join(mul_results))
''
# 模拟极限除法法则
st.subheader("极限除法法则")
div_results = []
for x in x_values:
    if g(x) != 0:  # 只在 g(x) 非零时执行除法
        div_result = f(x) / g(x)
        div_results.append(f"当 x = {x} 时，\n"
                           f"f(x) / g(x) 的值为 {div_result}\n")
    else:
        div_results.append(f"当 x = {x} 时，\n"
                           f"g(x) 为 0，无法计算除法")
st.write("\n".join(div_results))


# 定义加法运算的函数
def add_functions(x):
    f = 2 * x + 1
    g = 3 * x - 2
    h = f + g
    return f, g, h


# 定义乘法运算的函数
def multiply_functions(x):
    f = x
    g = x + 1
    h = f * g
    return f, g, h


# 定义复合运算的函数
def compose_functions(x):
    # 定义 f 和 g 为函数
    f = lambda x: x ** 2  # f(x) = x^2
    g = lambda x: 2 * x + 1  # g(x) = 2x + 1

    g_x = g(x)  # 计算 g(x)
    h = f(g_x)  # 复合操作 f(g(x))
    return f(x), g(x), h

# 标题
st.title("1.9 连续函数加法、乘法与复合运算示例")
st.write(
"""设函数
f(x) = 2x + 1
和
g(x) = 3x 2
，这两个函数在定义域内都是连续函数。它们的和函
数
h(x) = f(x) + g(x) = (2x + 1) + (3x 2) = 5x 1
也是连续函数。"""
)
# 用户输入
x_value = st.number_input("请输入一个值 x:", min_value=-10, max_value=10, value=1)

# 加法运算
st.header("加法运算 (f(x) + g(x))")
f_add, g_add, h_add = add_functions(x_value)
st.write(f"f(x) = 2x + 1 => f({x_value}) = {f_add}")
st.write(f"g(x) = 3x - 2 => g({x_value}) = {g_add}")
st.write(f"加法结果 h(x) = f(x) + g(x) => h({x_value}) = {h_add}")

# 乘法运算
st.header("乘法运算 (f(x) * g(x))")
f_mult, g_mult, h_mult = multiply_functions(x_value)
st.write(f"f(x) = x => f({x_value}) = {f_mult}")
st.write(f"g(x) = x + 1 => g({x_value}) = {g_mult}")
st.write(f"乘法结果 h(x) = f(x) * g(x) => h({x_value}) = {h_mult}")

# 复合运算
st.header("复合运算 (f(g(x)))")
f_comp, g_comp, h_comp = compose_functions(x_value)
st.write(f"f(x) = x^2 => f({x_value}) = {f_comp}")
st.write(f"g(x) = 2x + 1 => g({x_value}) = {g_comp}")
st.write(f"复合结果 h(x) = f(g(x)) => h({x_value}) = {h_comp}")



def f(x):
    return x**2 - 2*x + 2

# 页面标题
st.title('1.10 最值定理示例：函数 f(x) 在闭区间上的最值')

# 用户输入区间端点
a = st.number_input('请输入区间的左端点 a:', value=-1)
b = st.number_input('请输入区间的右端点 b:', value=3)

# 生成区间内的大量点用于绘图
x_values = np.linspace(a, b, 400)
y_values = f(x_values)

# 计算函数在区间端点和对称轴处的值
y_a = f(a)
y_b = f(b)
x_vertex = 1  # 对称轴在 x = 1
y_vertex = f(x_vertex)

# 确定最大值和最小值
min_value = min(y_a, y_b, y_vertex)
max_value = max(y_a, y_b, y_vertex)

# 显示最值
st.write(f"函数 f(x) 在闭区间 [{a}, {b}] 上的最小值为 {min_value}")
st.write(f"函数 f(x) 在闭区间 [{a}, {b}] 上的最大值为 {max_value}")

# 绘制函数图像
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$f(x)=x^2 - 2x + 2$', color='b')
plt.scatter([a, b, x_vertex], [y_a, y_b, y_vertex], color='red', zorder=5)
plt.title(f'函数 f(x) 在闭区间 [{a}, {b}] 上的图像')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# 显示图像
st.pyplot(plt)




def f(x):
    return x**3 - 2*x + 1
def bisection_method(a, b, C, tol=1e-6, max_iter=100):
    if f(a) > f(b):
        a, b = b, a
    if C < f(a) or C > f(b):
        raise ValueError("C is not in the range of f(a) and f(b).")
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        midpoint = (a + b) / 2
        if f(midpoint) == C:
            return midpoint
        elif f(midpoint) < C:
            a = midpoint
        else:
            b = midpoint
        iter_count += 1
    return (a + b) / 2

# 设置页面标题
st.title("\n介值定理可视化")

# 创建输入框，允许用户设置区间和目标值
a = st.number_input("请输入区间左端点a:", value=-2)
b = st.number_input("请输入区间右端点b:", value=2)
C = st.number_input("请输入目标值C:", value=0)

# 计算区间端点的函数值
A = f(a)
B = f(b)

# 生成区间内的大量点用于绘图
x_values = np.linspace(a, b, 400)
y_values = f(x_values)

# 绘制函数图像
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, y_values, label=r'$f(x)=x^3 - 2x + 1$')
ax.axhline(y=C, color='r', linestyle='--', label=f'C = {C}')
ax.scatter([a, b], [A, B], color='green', zorder=5, label='Endpoints')
ax.set_title(f'Function f(x) on the interval [{a}, {b}]')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True)

# 显示图像
st.pyplot(fig)

# 调用二分法函数并显示结果
try:
    root = bisection_method(a, b, C)
    st.write(f"在开区间 ({a}, {b}) 内找到使得 f(x) = {C} 的近似点 x = {root}，此时 f(x) = {f(root)}")
except ValueError as e:
    st.write(str(e))



def f(x):
    return x**2 - 2
def bisection_method(a, b, tol=1e-6, max_iter=100):
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(midpoint) * f(a) < 0:
            b = midpoint
        else:
            a = midpoint
        iter_count += 1
    return (a + b) / 2

# Streamlit 界面
st.title("零点定理演示")

# 用户输入区间
a = st.number_input("输入区间的左端点 (a)", value=1.0)
b = st.number_input("输入区间的右端点 (b)", value=2.0)

# 计算区间端点的函数值
fa = f(a)
fb = f(b)

# 检查零点定理条件
if fa * fb < 0:
    st.write(f"满足零点定理的条件，函数在开区间 ({a}, {b}) 内至少有一个零点。")
else:
    st.write(f"不满足零点定理的条件。")

# 绘制函数图像
x_values = np.linspace(a, b, 400)
y_values = f(x_values)

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, y_values, label=r'$f(x) = x^2 - 2$', color='b')
ax.axhline(y=0, color='r', linestyle='--', label='y = 0')
ax.scatter([a, b], [fa, fb], color='green', zorder=5, label='Endpoints')

ax.set_title('Function f(x) on the closed interval [{}, {}]'.format(a, b))
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(True)

# 显示图像
st.pyplot(fig)

# 调用二分法找到零点
root = bisection_method(a, b)
st.write(f"在开区间 ({a}, {b}) 内找到的近似零点为 x = {root}，此时 f(x) = {f(root)}")
