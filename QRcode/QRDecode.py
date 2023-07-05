from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/manic/OneDrive/Pictures/myqrcode.png")
#image location of the encoded qrcode to decode

result = decode(img)

print(result)