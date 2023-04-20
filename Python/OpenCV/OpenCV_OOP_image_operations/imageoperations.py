'''
@chinso
Feb 2023
Objects Oriented class to perform OpenCV image operations

'''
import cv2 as cv
import os 
import numpy as np

from PIL import Image
from PIL.ExifTags import TAGS


class ImageOperations:
  def __init__(self, path):
    '''
    path = Full image path
    '''
    if os.path.exists(path):
      self.path  = path
      self.image = cv.imread(self.path)
    else: 
      print('Image not found!')

  def show_image(self, promt='Title', img = np.array([])):

    if img.size == 0:

      cv.imshow(promt, self.image)

    else:

      cv.imshow(promt, img)

    cv.waitKey(0)
    cv.destroyAllWindows()


  def to_gray_scale(self, show_image = False):
    '''
    Convert an image to grayscale

    show_image = default False
    '''

    try:

      gray_image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
    
    except Exception as e: 

      print('Error: ', e)
    
    else: # convert image

      if show_image:

        self.show_image(promt='Image to grayscale', img = gray_image)

      return gray_image


  def resize_px(self, height = 0, width = 0,  interp = 1, show_image = False):
    '''
    Image size resize by absolute finel size
    Resized image keeps original aspect ratio by default providing 1 parameter,
    you could modify aspect ratio providing both height, width

    height > 0,

    width > 0,

    interp = 

    0 cv2.INTER_NEAREST,

    1 cv2.INTER_LINEAR,

    2 cv2.INTER_CUBIC,

    4 cv2.INTER_LANCZOS4,

    show_image = default False

    '''

    if height * width > 0: 

      ratio_height = height / self.image.shape[0]
      ratio_width  = width /  self.image.shape[1]
    
    else: 
      resize_px = width + height
      ratio  = resize_px  / max(self.image.shape)
      ratio_height = ratio
      ratio_width  = ratio

    image_shape = (int(self.image.shape[1] * ratio_width),
                    int(self.image.shape[0] * ratio_height) 
                  )
    try:
      
      image_resized =  cv.resize(self.image, image_shape, interpolation = interp)
    
    except cv.error as e:
      if 'inv_scale_x > 0' in str(e):
        print('OpenCV error: Please provide a scale percent > 0 for resizing' )

    else:
      
      if show_image:

        print('Image resized by absolute pixels dimensions:')
        print('Original image size: ', str(self.image.shape), ' px')
        print('Aspect ratio Width / Height: ', str(self.image.shape[1]/self.image.shape[0]))
        print('Resize factors: ', height, width, 'px')
        print('Resized  image size: ', str(image_resized.shape), ' px')
        print('New aspect ratio: ', str(image_resized.shape[1]/image_resized.shape[0]))

        self.show_image(promt='Image resized by absolute pixels dimensions', img = image_resized)
    
      return image_resized


  def resize_percent(self, height = 0, width = 0,  interp = 1, show_image = False):
    '''
    Percentual image size resize by percent reduce < 100 > expand
    Resized image keeps original aspect ratio by default providing 1 parameter,
    you could modify aspect ratio providing both height, width

    height > 0,

    width > 0,

    interp = 

    0 cv2.INTER_NEAREST,

    1 cv2.INTER_LINEAR,

    2 cv2.INTER_CUBIC,

    4 cv2.INTER_LANCZOS4,

    show_image = default False

    '''

    if height * width > 0: 

      ratio_height = height / 100
      ratio_width  = width  / 100
    
    else: 
      resize_percent = width + height
      ratio_width  = resize_percent  / 100
      ratio_height = ratio_width

    image_shape = (int(self.image.shape[1] * ratio_width),
                    int(self.image.shape[0] * ratio_height)
                  )
    try:
      
      image_resized =  cv.resize(self.image, image_shape, interpolation = interp)
    
    except cv.error as e:
      if 'inv_scale_x > 0' in str(e):
        print('OpenCV error: Please provide a scale percent > 0 for resizing' )

    else:

      if show_image:

        print('Image resized by percentual values:')
        print('Original image size: ', str(self.image.shape), ' px')
        print('Aspect ratio Width / Height: ', str(self.image.shape[1]/self.image.shape[0]))
        print('Resize factors: ', height, width, '%')
        print('Resized  image size: ', str(image_resized.shape), ' px')
        print('New aspect ratio: ', str(image_resized.shape[1]/image_resized.shape[0]))


      self.show_image(promt='Image resized by percentual value', img = image_resized)

    return image_resized
  
  def print_exif_GPS(self, show_image=False):
      '''
      Return GPSInfo as dictionary with Latitude and longitude in decimal format 
      GPSInfo
        GPSVersionID
        GPSLatitudeRef
        GPSLatitude
        GPSLongitudeRef
        GPSLongitude
        GPSAltitudeRef
        GPSAltitude
        GPSDateStamp
        GPSTimeStamp
        GPSMapDatum

      show_image = default False
      '''
      try:
        # Open the image with PIL to access Exif data
        pil_img = Image.open(self.path)
        exif_data = pil_img._getexif()

        # Define the font and text
        font = cv.FONT_HERSHEY_SIMPLEX
        text = ''

        gps_dict = {'latitude': '', "longitude": ''}

        # Get GPSInfo tag and its sub-tags
        gps_info = exif_data.get(34853, None)
        if gps_info:
          # Extract latitude and longitude information
          gps_latitude = gps_info.get(2)
          gps_latitude_ref = gps_info.get(1)
          gps_longitude = gps_info.get(4)
          gps_longitude_ref = gps_info.get(3)

          # Convert latitude and longitude to decimal format
          if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            latitude_decimal = float(gps_latitude[0]) + float(gps_latitude[1])/60 + float(gps_latitude[2])/3600

            if gps_latitude_ref == 'S':
              latitude_decimal = -latitude_decimal
            longitude_decimal = float(gps_longitude[0]) + float(gps_longitude[1])/60 + float(gps_longitude[2])/3600
            
            if gps_longitude_ref == 'W':
              longitude_decimal = -longitude_decimal

            # Add the latitude and longitude to the text
            text += f'Latitude: {latitude_decimal:.20f}\n'
            text += f'Longitude: {longitude_decimal:.20f}\n'

            # Save latitude, latitude values as dictionary
            gps_dict = {'latitude': latitude_decimal, "longitude": longitude_decimal}

      except Exception as e: 
        print('Error: ', e)
      
      else:
        if show_image:
          # Put the text on the image
          cv.putText(self.image, text, (20, 40), font, 0.5, (255, 255, 255), 1)

          # Display the image with the GPS info
          self.show_image(promt='Image with exif GPS info')


        # Wait for a key press and then close the window
        cv.waitKey(0)
        cv.destroyAllWindows()

      return gps_dict
