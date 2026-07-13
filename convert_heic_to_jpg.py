from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()
path = r"D:\projects\dpak-07\IMG_0934.heic"
out = r"D:\projects\dpak-07\IMG_0934.jpg"
if os.path.exists(path):
    im = Image.open(path)
    im = im.convert('RGB')
    im.save(out)
    print('saved', out)
else:
    print('HEIC source not found')
