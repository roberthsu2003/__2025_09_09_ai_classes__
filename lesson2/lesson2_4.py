from sklearn.datasets import load_iris

# 載入Iris資料集
iris = load_iris()
#檢查資料集
print(type(iris))
#取得特徵與標籤 
X = iris.data
print("X的資料類型:", type(X))
print("X的形狀:", X.shape)
print("X的內容:\n", X)

#請使用pandas套件將X轉換成DataFrame格式，並命名欄位名稱為iris.feature_names
import pandas as pd
df_X = pd.DataFrame(X, columns=iris.feature_names)
print("轉換後的DataFrame:\n", df_X)

y = iris.target
print("y的資料類型:", type(y))
print("y的形狀:", y.shape)
print("y的內容:", y)