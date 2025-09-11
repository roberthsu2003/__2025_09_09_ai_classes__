import numpy as np

#常用來建立ndarray實體的函式    
arr1 = np.array([1, 2, 3])
print("從列表建立的陣列 arr1:", arr1)

arr2 = np.arange(0, 10, 2)
print("建立一個等差序列陣列 arr2:", arr2)

arr3 = np.zeros((2, 3))
print("建立一個2x3的全零陣列 arr3:\n", arr3)

arr4 = np.ones((3, 2))
print("建立一個3x2的全部值為1的陣列 arr4:\n", arr4)

arr5 = np.eye(3)
print("建立一個3x3的單位矩陣 arr5:\n", arr5)
arr6 = np.random.rand(2, 2)
print("建立一個2x2的隨機陣列 arr6:\n", arr6)
print("="*15)

# 3. 使用 Matplotlib 繪製函數圖形
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y_sin, label='sin(x)', color='C0')
plt.plot(x, y_cos, label='cos(x)', color='C1', linestyle='--')
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.title('sin(x) 與 cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


