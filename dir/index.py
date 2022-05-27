# . .venv/bin/activate
# deactivate
import pandas as pd

df = pd.read_csv("./index.csv")
# print(df)  # データの中身
# print(len(df))  # データの件数
# print(df.columns.values)  # ヘッダー（項目名一覧）
# print(df.index.values)  # インデックス一覧
# print(df["年齢"])
# print(df.loc[1]["名前"])
# print(df["1"]["名前"])
# df = df[df["年齢"] >= 30]
# print(df)

# df1 = pd.DataFrame(index=[], columns=["名前", "年齢", "趣味"])
# df = df.append({"名前": "ままま", "年齢": 22, "趣味": "ゴルフ"}, ignore_index=True)
# df = df.append({"名前": "ぱぱぱ", "年齢": 50, "趣味": "ゴルフ"}, ignore_index=True)
# df1 = df.drop(0, axis=0)
print(df.mean()["年齢"])
# print(df1["年齢"].min())
# df1.to_csv("test.csv")

# print(df1)
