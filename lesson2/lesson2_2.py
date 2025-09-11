#numpy的基本操作,建立陣列,陣列運算
#作者: Robert Hsu
#日期: 2023/09/09
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(type(arr1))
print("從列表建立的陣列 arr1:", arr1)

print("===============")
#建立一個等差序列陣列，起始為0，終止為10(不含10)，步長為2
arr2 = np.arange(0, 10, 2)
print("建立一個等差序列陣列 arr2:", arr2)
print("="*15)


# 建立一個2x3的全零陣列
arr3 = np.zeros((2, 3))
print("建立一個2x3的全零陣列 arr3:\n", arr3)
print("="*15)

# 建立一個3x2的全部值為1的陣列
arr4 = np.ones((3, 2))
print("建立一個3x2的全部值為1的陣列 arr4:\n", arr4)

# 建立一個3x3的單位矩陣（對角線為1，其餘為0）
arr5 = np.eye(3)
print("建立一個3x3的單位矩陣 arr5:\n", arr5)