# Example: https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/

# import the necessary packages
import numpy as np
import cv2
import os

from imageoperations import ImageOperations



cwd = os.getcwd()

image_path = os.path.join(cwd, r'images/DJI_0449.JPG')

print(image_path)

image = ImageOperations(image_path)

image.crop_roi()

warped = image.warp()

# show the original and warped images
image.show_image('Original')
cv2.imshow("Warped", warped)
cv2.waitKey(0)