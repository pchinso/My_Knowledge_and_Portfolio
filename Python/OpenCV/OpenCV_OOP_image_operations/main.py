import os

from imageoperations import ImageOperations
'''
OpenCV Show image 

'''

if __name__ =="__main__":

  cwd = os.getcwd()

  image_path = os.path.join(cwd, r'input\DJI_0449.JPG')
  # image_path = os.path.join(cwd, r'input\test.jpg')

  print(image_path)

  image = ImageOperations(image_path)

  image.show_image('Original Image')

  gray = image.to_gray_scale(show_image=True)

  little = image.resize_px(height=40, width=50, interp=1, show_image=True)

  big = image.resize_percent(height=110, width=150, interp=1, show_image=True)

  gps_location = image.print_exif_GPS(show_image = False)
