import matplotlib.pyplot as plt

# 対象データ
left = [1, 2, 3, 4, 5]  # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]  # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesに棒グラフを設定する
ax.bar(left, height)
# 表示する
plt.show()
