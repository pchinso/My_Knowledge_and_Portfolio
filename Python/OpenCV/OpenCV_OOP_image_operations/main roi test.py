import os
import cv2 as cv
import numpy as np
from imageoperations import ImageOperations
'''
OpenCV Show image 

'''

if __name__ =="__main__":

  cwd = os.getcwd()

  image_path = os.path.join(cwd, r'images/DJI_0449.JPG')

  print(image_path)

  image = ImageOperations(image_path)

  image.crop_roi(show_roi=True)

  image.show_image()
  image.save_image()

  print(image.original_im_ROI_points)

  # roi_scaler = [image.width / image.main_display_size[0],
  #               image.height / image.main_display_size[1]
  #              ]
  # roi = []
  # for i in range(len(points)):
  #   pair = (points[i][0]*roi_scaler[0],points[i][1]*roi_scaler[1])
  #   roi.append(pair)
  
  # print('ROI: \n')
  # print(roi)

  # # Crop the maximum width and height region from the original image
  # x_min, y_min = np.min(roi, axis=0)
  # x_max, y_max = np.max(roi, axis=0)
  # roi_fit = image.image[y_min:y_max, x_min:x_max]