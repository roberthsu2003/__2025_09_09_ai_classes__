# 步驟 1: 匯入必要的程式庫
# - 匯入 wget 用於從網路下載檔案。
# - 匯入 os 用於與作業系統互動，例如檢查檔案是否存在。
# - 匯入 mglearn，這是一個用於機器學習視覺化和資料集生成的輔助函式庫。
# - 匯入 matplotlib.pyplot，這是 Python 中用於繪圖的主要函式庫，並將其別名為 plt。
# - 從 matplotlib.font_manager 匯入 FontProperties，用於處理自訂字型。
import wget
import os
import mglearn
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 步驟 2: 準備中文字型
# - 設定字型檔案的路徑為 "ChineseFont.ttf"。
# - 檢查該字型檔案是否已存在於目前目錄中。
# - 如果字型檔案不存在，則從指定的 URL 下載它。
#   URL: "https://github.com/roberthsu2003/machine_learning/raw/refs/heads/main/source_data/ChineseFont.ttf"
font_path = "ChineseFont.ttf"
if not os.path.exists(font_path):
    wget.download("https://github.com/roberthsu2003/machine_learning/raw/refs/heads/main/source_data/ChineseFont.ttf")

# 步驟 3: 設定 Matplotlib 的中文字型
# - 使用下載的字型檔案路徑建立一個 FontProperties 物件。
chinese_font = FontProperties(fname=font_path)

# 步驟 4: 生成並載入 Forge 資料集
# - 使用 mglearn.datasets.make_forge() 函式建立一個用於二元分類的合成資料集。
# - 將回傳的特徵資料指派給變數 X。
# - 將回傳的標籤資料指派給變數 y。
X, y = mglearn.datasets.make_forge()

# 步驟 5: 繪製資料集的散點圖
# - 建立一個新的圖表，設定其大小為 8x6 英吋。
# - 使用 mglearn.discrete_scatter 函式來繪製散點圖。
#   - X[:, 0] 是所有資料點的第一個特徵（x 座標）。
#   - X[:, 1] 是所有資料點的第二個特徵（y 座標）。
#   - y 是每個點的類別標籤，用於著色。
plt.figure(figsize=(8, 6))
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)

# 步驟 6: 設定圖表的標題、軸標籤和圖例
# - 使用 plt.title() 設定圖表的標題為 "Forge 資料集散點圖"，並套用中文字型。
# - 使用 plt.xlabel() 設定 x 軸的標籤為 "第一個特徵"，並套用中文字型。
# - 使用 plt.ylabel() 設定 y 軸的標籤為 "第二個特徵"，並套用中文字型。
# - 使用 plt.legend() 為圖表新增圖例，標示 "類別 0" 和 "類別 1"，並套用中文字型。
plt.title("Forge 資料集散點圖", fontproperties=chinese_font)
plt.xlabel("第一個特徵", fontproperties=chinese_font)
plt.ylabel("第二個特徵", fontproperties=chinese_font)
plt.legend(["類別 0", "類別 1"], prop=chinese_font)

# 步驟 7: 顯示圖表
# - 使用 plt.show() 將繪製好的圖表顯示出來。
plt.show()
