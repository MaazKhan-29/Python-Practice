""" Image to pdf conversion """

""" First installment one package by command 
pip install pillow
"""
""" Code  for making 1 page pdf

from PIL import Image

img=Image.open(r'images\Notes1.jpg')
info_img=img.convert('RGB')
img.save("new_image.pdf")
"""

""" Code for many page pdf

from PIL import Image

img1 = Image.open(r'images\Notes1.jpg')
img2 Image.open(r'images\Notes2.jpg')
img3 Image.open(r'images\Notes3.jpg')

pdf_img1=img1.convert('RGB')
pdf_img2=img2.convert('RGB')
pdf_img3=img3.convert('RGB')

images_list = [pdf_img2, pdf_img3]
pdf_img1.save('new_image', save_all= True, append_images images_list)
"""

""" Code for making many pages pdf with simple way

from PIL import Image
import os

folder = "images"
files=os.listdir(folder)

img = Image.open(folder + "/" + files[0])
first=img.convert('RGB')
files.pop(0)

images_list = []

for file in files:
     img = Image.open(folder + "/" + file)
     pdf_img = img.convert('RGB')
     images_list.append(pdf_img)

first.save('notes.pdf', save_all = True, append_images = images_list)
"""