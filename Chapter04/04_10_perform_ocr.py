import pytesseract as pt
from PIL import Image

img = Image.open("a.png")
text = pt.image_to_string(img, lang='Hangul')
print(text)