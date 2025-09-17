# WARP.md

此檔案為 WARP (warp.dev) 在此程式庫中工作時提供指引。

## 程式庫概覽

此程式庫包含以繁體中文教學的 AI 和程式設計教育材料，涵蓋基礎 Python 程式設計、NumPy 運算、matplotlib 視覺化以及機器學習概念。課程結構透過編號的課程目錄依序組織。

## 開發環境

### Python 環境設定
```bash
# 安裝必要套件
pip install -r requirements.txt

# 必要套件：
# - numpy: 數值運算和陣列操作
# - mglearn: 機器學習工具和資料集
# - matplotlib: 資料視覺化和繪圖
# - wget: 檔案和資料集下載
```

### Jupyter Notebook 設定
筆記本配置使用「machine_learning」核心，搭配 Python 3.10.18。使用筆記本時：

```bash
# 安裝和設定 Jupyter
pip install jupyter

# 啟動 Jupyter 進行互動式開發
jupyter notebook

# 或使用 Jupyter Lab
jupyter lab
```

## 課程架構

### 課程結構
- **lesson1/**: Python 基礎入門
  - `lesson1_1.py`: 基本「Hello Python」腳本
  - `snake_game.html`: 互動式 JavaScript 貪食蛇遊戲
  
- **lesson2/**: NumPy 基礎和陣列運算
  - `lesson2_1.ipynb`: 機器學習概念介紹（Jupyter 筆記本）
  - `lesson2_2.py`: 核心 NumPy 陣列建立和基本運算
  - `lesson2_3.py`: 進階 NumPy 運算與 matplotlib 視覺化
  - `lesson2_4.py` 和 `lesson2_5.py`: 額外的 NumPy 練習

- **lesson3/**: 進階概念和視覺化
  - `lesson3_1.ipynb`: Jupyter 中的 Markdown 格式範例
  - `lesson3_1.py`: 進階主題的 Python 腳本
  - `tetris.html`: 互動式 JavaScript 俄羅斯方塊遊戲
  - `ChineseFont.ttf`: 中文字型檔案，用於正確的文字呈現

- **link/**: 課程影片錄製和資源
  - 包含實況教學的 YouTube 連結

## 常用開發指令

### 執行 Python 腳本
```bash
# 執行個別課程腳本
python lesson1/lesson1_1.py
python lesson2/lesson2_2.py
python lesson2/lesson2_3.py

# 對於顯示圖表的 matplotlib 腳本
python -c "import matplotlib.pyplot as plt; exec(open('lesson2/lesson2_3.py').read()); plt.show(block=True)"
```

### 使用 Jupyter Notebooks
```bash
# 啟動 Jupyter 並開啟特定筆記本
jupyter notebook lesson2/lesson2_1.ipynb
jupyter notebook lesson3/lesson3_1.ipynb

# 將筆記本轉換為 Python 腳本
jupyter nbconvert --to python lesson2/lesson2_1.ipynb
```

### 檢視 HTML 遊戲
```bash
# 在預設瀏覽器中開啟 HTML 遊戲（macOS）
open lesson1/snake_game.html
open lesson3/tetris.html

# 或本地端伺服器以提高相容性
python -m http.server 8000
# 然後造訪 http://localhost:8000/lesson1/snake_game.html
```

## 程式碼模式和教學風格

### 語言和註解
- 所有程式碼註解和文件都使用繁體中文
- 教育程式碼包含給初學者的詳細說明
- 課程檔案中出現作者標註：「作者: Robert Hsu」

### NumPy 教學進度
1. **基本陣列建立**: `np.array()`、`np.arange()`、`np.zeros()`、`np.ones()`
2. **矩陣運算**: 元素運算、廣播
3. **視覺化整合**: 與 matplotlib 結合以提供即時視覺回饋

### 互動元素
- HTML 遊戲提供程式概念的實作示範
- Jupyter 筆記本結合理論與可執行程式碼
- 從基礎概念到實際應用的逐步進展

## 檔案組織原則

- 循序漸進的課程編號提供結構化學習路徑
- 混合檔案類型（`.py`、`.ipynb`、`.html`）展示不同程式設計方法
- 理論（筆記本）與實作（Python 腳本）的分離
- 外部資源（字型、連結）組織在專門目錄中

## 開發注意事項

- 課程使用 Python 3.10.18，如筆記本 metadata 所示
- Matplotlib 圖表在獨立腳本中可能需要 GUI 後端顯示
- 包含中文字型檔案以確保視覺化中的正確文字呈現
- HTML 遊戲是內嵌 JavaScript 的獨立檔案
