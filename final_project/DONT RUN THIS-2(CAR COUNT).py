import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from openpyxl import *
import pandas as pd


im = cv2.imread('car.png')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
s=str(label.count('car'))
print(s)
print('Number of cars in the image is '+ str(label.count('car')))

