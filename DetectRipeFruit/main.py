import cv2
import numpy as np
from matplotlib import pyplot as plt


#resmi ac
image = cv2.imread('images.jpeg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

weaker = np.array([0,0,100])
stronger = np.array([10,255,255])

mask = cv2.inRange(hsv,weaker,stronger)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(mask, cmap='gray')
plt.title('Mask')

plt.show()