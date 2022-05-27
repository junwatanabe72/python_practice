import matplotlib.pyplot as plt

# # プロットする点
# X = [0, 1, 2]
# Y = [0, 1, 2]

# # figureオブジェクトを生成する
# fig = plt.figure()
# # axesオブジェクトをfigureオブジェクトに設定する
# ax = fig.add_subplot(1, 1, 1)
# # axesオブジェクトに対して散布図を設定する
# # ax.scatter(X, Y, color="b", label="test_data")
# # # axesオブジェクトに対して凡例設定
# # ax.legend(["arege"])
# # # axesオブジェクトに対してタイトルを設定
# # ax.set_title("mapTitle")
# ax.plot(X, Y)
# # 表示する
# plt.show()


# double lines
# figureを生成
# fig1 = plt.figure(1)

# # グラフ描画設定
# ax = fig1.add_subplot(1, 1, 1)
# x1 = [-2, 0, 2]
# y1 = [-2, 0, 2]
# ax.plot(x1, y1)

# x2 = [-2, 0, 2]
# y2 = [-4, 0, 4]
# ax.plot(x2, y2)

# ax.grid(True)  # grid表示ON
# ax.set_xlim(left=-2, right=2)  # x範囲
# ax.set_ylim(bottom=-2, top=2)  # y範囲
# ax.set_xlabel("x")  # x軸ラベル
# ax.set_ylabel("y")  # y軸ラベル
# ax.set_title("ax title")  # グラフタイトル
# ax.legend(["f(x)=x", "g(x)=2x"])  # 凡例を表示
# plt.show()


# deco lines
# # x、yデータ
# x = range(20)
# y = range(20)

# # 点(x, y)がもつ量
# z = range(20)

# # カラーマップ
# cm = plt.cm.get_cmap("RdYlBu")
# # figureを生成する
# fig = plt.figure()

# # axをfigureに設定する
# ax = fig.add_subplot(1, 1, 1)

# # axに散布図を描画、戻り値にPathCollectionを得る
# mappable = ax.scatter(x, y, c=z, vmin=0, vmax=20, s=35, cmap=cm)

# # カラーバーを付加
# fig.colorbar(mappable, ax=ax)

# # 表示
# plt.show()


# three dimention
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

# ランダムな点を生成する(x, y, z座標)
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = Axes3D(fig)

# axesに散布図を設定する
ax.scatter(x, y, c="b")

# 表示する
plt.show()
