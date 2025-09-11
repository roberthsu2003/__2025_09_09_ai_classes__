import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

import matplotlib.pyplot as plt

# 載入Iris資料集
iris = load_iris()

# 創建DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# 分析資料
print("資料集基本資訊:")
print(df.info())
print("\n資料集描述統計:")
print(df.describe())
print("\n各類別數量:")
print(df['species'].value_counts())

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 創建分佈圖
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Iris資料集特徵分佈圖', fontsize=16)

# 繪製各特徵的分佈圖
features = ['sepal length (cm)', 'sepal width (cm)', 
           'petal length (cm)', 'petal width (cm)']

for i, feature in enumerate(features):
    row = i // 2
    col = i % 2
    
    for species in df['species'].unique():
        species_data = df[df['species'] == species][feature]
        axes[row, col].hist(species_data, alpha=0.7, label=species, bins=15)
    
    axes[row, col].set_title(feature)
    axes[row, col].set_xlabel('值')
    axes[row, col].set_ylabel('頻率')
    axes[row, col].legend()

plt.tight_layout()
plt.show()

# 創建散佈圖矩陣
plt.figure(figsize=(12, 10))
pd.plotting.scatter_matrix(df[features], c=df['target'], 
                          figsize=(12, 10), alpha=0.7, cmap='viridis')
plt.suptitle('Iris資料集特徵散佈圖矩陣', fontsize=16)
plt.show()

# 使用seaborn創建成對圖
plt.figure(figsize=(12, 10))
sns.pairplot(df, hue='species', vars=features, diag_kind='hist')
plt.suptitle('Iris資料集成對圖', fontsize=16, y=1.02)
plt.show()