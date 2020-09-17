from PIL import Image,ImageFilter
import os

size = (725,480)
for i in os.listdir('.'):
    if i.endswith('.jfif'):
        image = Image.open(i)
        fileName, File_ext = os.path.splitext(i)
        print('{} and {}'.format(fileName,File_ext))
        image.thumbnail(size)  #this will helps to resize the image into 500,500 pixel
        image.save('Kohli png/{}.png'.format(fileName))
       
show_image = Image.open('kohli1.jpg')                   #show image
show_image.show()

rotate_image = Image.open('kohli2.jpg')                 #see the current directory(rotate an image into 90 deg)
rotate_image.rotate(90).save('kohli2_90.jpg')  

bw_image = Image.open('kohli3.jpg')                     #grayscale image
bw_image.convert(mode="L").save('kohli3_b&w.jpg')      

blur_image = Image.open('kohli4.jpg')                     #blur image
blur_image.filter(ImageFilter.GaussianBlur(2)).save('kohli4_blur.jpg')      










	
