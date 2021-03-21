import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import numpy as np

img = Image.open("lenna.png")
data = np.array(img)
img.show()


# размытое изображение
im1 = img.filter(ImageFilter.BLUR)
im1.save("blur_lena.png")
im1.show()

# четкие контуры
im2 = img.filter(ImageFilter.CONTOUR)
im2.save("contour_lena.png")
im2.show()

# сглаживание
img3 = img.filter(ImageFilter.SMOOTH)
img3.save("smooth_lena.png")
img3.show()

# фильтр matplotlib

img = plt.imread('lenna.png')

plt.imshow(img.mean(2), cmap='plasma')
plt.axis("off")
plt.savefig("lenna_plasma.png")
plt.show()

plt.imshow(img.mean(2), cmap='gray')
plt.axis("off")
plt.savefig("lenna_gray.png")
plt.show()