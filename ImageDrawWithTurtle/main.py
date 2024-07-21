import turtle
from sketchpy import canvas
import cv2

im = cv2.imread("joker.jpg")
print(im.shape)
obj = canvas.sketch_from_image("joker.jpg")
obj.draw(threshold=100)