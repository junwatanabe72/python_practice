# from PIL import Image
from PIL import Image, ImageFont, ImageDraw

image = Image.open("./sample.jpeg")

# resized_image = image.resize((400, 400))
# print(image.size)  # (400, 400)
# resized_image.save("./resized.jpg")
# rotated_image = image.rotate(45)
# pasted_image.save("pasted_image.jpg")
# rotated_image.save("rotated_image.jpg")


# 画像リサイズ
# image_copy = Image.open("./copy.jpeg")
# image_copy.thumbnail((400, 400))
# print(image_copy.size)  # (225, 400)
# image_copy.save("./thumbnail.jpg")


# 画像挿入
# fliped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
# pasted_image = image.copy()
# logo_image = Image.open("./logo.png")
# pasted_image.paste(logo_image, (100, 100), logo_image)
# pasted_image.save("./copy.jpeg")


# # 文字列の書き込み
text = "Golfersfarm"
color = (255, 255, 255, 128)  # 白色
font_size = 42
font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", font_size)
draw = ImageDraw.Draw(image)
draw.text((110, 440), text, font=font, fill=color)
image.save("./written_image.jpg")
