from PIL import Image 
import os

thisdir = "/Users/human/codes/milady_dl/milady_downloader/"
imgdir = "{}img/".format(thisdir)
small_img_dir = "{}small_img/".format(thisdir)

# print(len(os.listdir(imgdir)))

for img in os.listdir(imgdir):

    print(img)
    imgpath = "{}{}".format(imgdir, img)

    image = Image.open(imgpath) 
    print(image.size)

    resize = image.resize((256, 256))
    resize_loc = "{}{}".format(small_img_dir, img)

    resize.save(resize_loc)
