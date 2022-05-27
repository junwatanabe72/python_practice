# エンコーディング
# import chardet
# from urllib.request import urlopen

# r = urlopen("https://suumo.jp/kanto/")
# rawdata = r.read()
# print(chardet.detect(rawdata))


# import mojimoji

# text = "pｙｔｈｏｎ パイソン １０００"
# print(mojimoji.zen_to_han(text))  # python ﾊﾟｲｿﾝ 1000

# print(mojimoji.zen_to_han(text, kana=False))  # python パイソン 1000

# print(mojimoji.zen_to_han(text, digit=False))  # python ﾊﾟｲｿﾝ １０００

# print(mojimoji.zen_to_han(text, ascii=False))  # ｐｙｔｈｏｎ ﾊﾟｲｿﾝ 1000


import requests

url = "https://www.athome.co.jp/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/62.0.3202.94 Safari/537.36"
    )
}
r = requests.get(url, headers=headers)
print(r.text)
