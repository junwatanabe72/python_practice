import pandas as pd

import matplotlib.pyplot as plt

# import japanize_matplotlib


# import json
# from pandas import json_normalize

df = pd.read_json("./a.json", orient="index")
# json_open = open("./a.json", "r")
# json_load = json.load(json_open)
# info = json.loads(data)
# df_s = pd.read_json("./test.json")
# df = json_normalize(json_load)
df_f = df.sort_values("passenger2019", ascending=False).head(10)
# df_ff = df_f.set_index("passenger2019")  # インデックスの再定義
df_f[["passenger2019"]].plot.bar()  # 棒グラフ
plt.show()

# df_ff["passenger2017"].T.plot.barh()  # 行と列を総入れ替えして横棒グラフ
# plt.show()
# print(df_f)
