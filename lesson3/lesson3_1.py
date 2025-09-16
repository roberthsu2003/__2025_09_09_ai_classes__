import wget
import os
import mglearn
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 讓 mglearn 使用中文字型
font_path = "ChineseFont.ttf"
if not os.path.exists(font_path):
    wget.download("https://github.com/roberthsu2003/machine_learning/raw/refs/heads/main/source_data/ChineseFont.ttf")

# 設定中文字型
chinese_font = FontProperties(fname=font_path)

# 產生資料集
X, y = mglearn.datasets.make_forge()

# 建立散點圖
plt.figure(figsize=(8, 6))
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)

# 設定圖表標題和軸標籤 (使用中文)
plt.title("Forge 資料集散點圖", fontproperties=chinese_font)
plt.xlabel("第一個特徵", fontproperties=chinese_font)
plt.ylabel("第二個特徵", fontproperties=chinese_font)
plt.legend(["類別 0", "類別 1"], prop=chinese_font)

# 顯示圖表
plt.show()