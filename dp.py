from PIL import Image, ImageDraw

dp = Image.new('RGB', (200, 200), color=(0, 0, 0))

d = ImageDraw.Draw(dp)

d.text((32, 100), "Frustrated Programmer", fill=(255, 255, 255))

dp.show()
