from sklearn.datasets import load_iris

# 載入Iris資料集
iris = load_iris()
#檢查資料集
print(type(iris))
#取得特徵與標籤 
X = iris.data
print("X")
print(X)

y = iris.target
print("y")
print(y)