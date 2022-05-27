import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize

dt_now = datetime.datetime.now()

path = f"./content/{dt_now.month}_{dt_now.day}/"
prefectures = {
    "tokyoMetro": "東京23区",
    "tokyo": "東京都市部",
    "saitama": "埼玉県",
    "chiba": "千葉県",
    "kanagawaMetro": "横浜市内",
    "kanagawa": "神奈川県",
    "osakaMetro": "大阪市内",
    "osaka": "大阪市外",
    "hyogoMetro": "神戸市",
    "hyogo": "神戸市外",
    "kyoto": "京都区外",
    "kyotoMetro": "京都区内",
}
total_number = 0
total_price = 0
x = []
y = []
target_col = ["area", "price", "agent", "title", "prefecture"]
array = [
    "tokyoMetro",
    "tokyo",
    "kanagawaMetro",
    "kanagawa",
    "saitama",
    "chiba",
    "osakaMetro",
    "osaka",
    "hyogoMetro",
    "hyogo",
    "kyotoMetro",
    "kyoto",
]

nearStation = "nearStation"
df = pd.read_json(f"{path}/tmp.json", orient="values")
# df_f = df[df["prefecture"] == "tokyo"]
df_w = df.loc[:, target_col]
df_items = json_normalize(df.to_dict("records"), nearStation)
df_f = pd.concat([df_w, df_items], axis=1)
# print("5/7 投資対象エリア土地新着物件")
for prefecture in array:
    target_df = df_f[df_f["prefecture"] == prefecture]
    print(prefecture)
    print(len(target_df))
    if len(target_df) == 0:
        continue
    mean_price = target_df["price"].mean()
    mean_area = target_df["area"].mean()
    # print(mean_price / 10000)
    # print(mean_area / 3.305785)
    integ = int((mean_price / 10000) / (mean_area / 3.305785))
    x.append(integ)
    y.append(prefectures[prefecture])
    total_number = total_number + len(target_df)
    total_price = total_price + integ

# fig = plt.figure()
plt.bar(y, x)
plt.xticks(rotation=25)
plt.ylabel("平均土地単価(万円/坪)")
plt.xlabel("各エリア")
plt.title(f"{str(dt_now.month)}/{str(dt_now.day)} 投資対象エリア土地新着物件")  # 売上推移
# plt.text(1, 100, "test", horizontalalignment="center", color="black")
[plt.text(i, 20, str(value), horizontalalignment="center", color="black") for i, value in enumerate(x)]
# plt.show()
plt.savefig(f"{path}/img.png")
