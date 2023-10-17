import numpy as np 
from PIL import Image
img_l= Image.open('Lenna.png').convert('L')
first_gen = np.array(img_l)
Image.fromarray(first_gen).convert('L').save('temp/ass.bmp')
mag =np.fft.fft2(first_gen)
#mag = np.fft.fftshift(mag)
mag = np.log(np.absolute(mag))
mag = mag*255/np.amax(mag)
Image.fromarray(mag).convert('L').save('temp/aaa.bmp')
print(np.amin(mag))