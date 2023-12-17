import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
from matplotlib import rcParams

#顯示負號
matplotlib.rcParams['axes.unicode_minus']=False
# 設定中文字型檔案路徑
font_path = "C:/Windows/Fonts/msjh.ttc"

# 設定中文字型
font_prop = fm.FontProperties(fname=font_path, size=14)
rcParams['font.family'] = font_prop.get_name()

# 提供的 CSV 檔案路徑
csv_path = "C:/Users/user/Desktop/ytdownload/Hualien.csv"

# 讀取 CSV 檔案
df = pd.read_csv(csv_path)

# 取得 x 和 y 的數據
x = df['Area']
y = df['Total net migration']

# plot
fig, ax = plt.subplots()

# 在 y=0 處添加一條黑色水平線
ax.axhline(y=0, color='black', linestyle='-', linewidth=1)

# 設置背景顏色
ax.set_facecolor('#B15BFF')

# 繪製長條圖，使用橙色填充，邊緣顏色為黑色，邊緣寬度為0.7
ax.bar(x, y, width=0.8, color='orange', edgecolor="black", linewidth=0.7)

# 設置 x 和 y 軸的範圍
ax.set(xlim=(-0.5, len(x) - 0.5), ylim=(-1000, max(y) + 600),
       xlabel='區域', ylabel='淨遷徒人口')

# 旋轉 x 軸標籤，避免重疊
plt.xticks(rotation=30, ha="right")

# 自動調整布局
plt.tight_layout()

# 在圖表上標示花蓮淨遷徒人口 112/10
plt.text(5, 112/10+600, '花蓮淨遷徒人口 112/10', color='blue', fontsize=14, ha='center', va='bottom', fontproperties=font_prop)

# 顯示圖形
plt.show()
