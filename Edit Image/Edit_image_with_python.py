## Installation of pillow library
## change the image extension
## resize image files
## resize multiple image using for loop
## sharpness
## brightness
## color
## contrast
## image blue , Gaussian Blur
from PIL import Image, ImageEnhance, ImageFilter
import os

img1 = Image.open('pic1.jpg')
# img1.save('Pic1.png') ## save 
# img1.show() ## show
# # resize
# max_size = (25,250)
# img1.thumbnail(max_size)
# img1.save('repic1.jpg')

###
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension=os.path.splitext(item)
#         img1.save(f"{filename}.png")


#### sharpness
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(10).show()
# # 0 --> Blurry
# # 1 --> Original image
# # 2 ---> Image with increased sharpness
 
#### --- color ---
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(19).show()

##### ---- Brightness---
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(2).show()


#### Contrast ----##

#enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1).show()


##### ---- Image blur----###
