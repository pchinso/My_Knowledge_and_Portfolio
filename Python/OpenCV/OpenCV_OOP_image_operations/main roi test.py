import os

from imageoperations import ImageOperations
'''
OpenCV Show image 

'''

if __name__ =="__main__":

  cwd = os.getcwd()

  image_path = os.path.join(cwd, r'images/DJI_0449.JPG')

  print(image_path)

  image = ImageOperations(image_path)

  
  # Image file
  print('Full path of image: ' , image.path)
  print('Image: ' , type(image.image))
  print('Original Image cloned to revert changes: ' , type(image.image))
  print('Resized Image fitted to display size: ', type(image.image_fit))

  image.crop_roi(show_roi=True)