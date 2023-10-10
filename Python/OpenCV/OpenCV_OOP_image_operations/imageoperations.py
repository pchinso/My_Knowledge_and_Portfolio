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

# For multiple monitors screens sizes
from screeninfo import get_monitors

def get_display_size():
    monitors = get_monitors()
    display_width = sum(m.width for m in monitors)
    display_height = max(m.height for m in monitors)
    
    display = [display_width, display_height]
    return (display)

def get_main_display_size():
    monitors = get_monitors()
    primary_monitor = next((m for m in monitors if m.is_primary), None)
    
    if primary_monitor:
        main_display_size = [primary_monitor.width, primary_monitor.height]
        return main_display_size
    else:
        # Return the total screen size if there is no primary monitor        
        return get_display_size()  

class ImageOperations:
  def __init__(self, path):
    '''
    path = Full image path
    '''
    if os.path.exists(path):
      self.path  = path
      self.image = cv.imread(self.path)
      self.clone = self.image.copy()
      
      #Initilize display variables 
      self.display_size = get_display_size() 
      self.main_display_size = get_main_display_size()
      
      #image size
      self.height, self.width, self.channels = self.image.shape
      
      # Fitted to screen image clone
      self.image_fit = cv.resize(self.image, (self.main_display_size))
      
    else: 
      print('Image not found!')
  
  def save_image(self, save_path='', image_name='', image_extension=''):
     
    if  save_path == '':

      save_path = self.path

      image_name, image_extension = save_path.split('.')
      image_name = image_name + '_copy'

      save_path = image_name + '.' + image_extension

    else:
      image_name = image_name + '.' + image_extension      
      save_path = os.path.join(save_path , image_name)


    try:
      os.makedirs(os.path.dirname(save_path))
    
    except FileExistsError:      
      cv.imwrite(save_path, self.image)
    
    except Exception as e: 
      print('Error: ', e)
    
    else:
      cv.imwrite(save_path, self.image)
    
    print(f'Image saved successfully at: {save_path}')

    
  def update_image_size(self):

    if len(self.image.shape) == 3:
      self.height, self.width, self.channels = self.image.shape
    else:
      self.height, self.width = self.image.shape

  def restore_image(self):

    self.image = self.clone
    self.image_fit = cv.resize(self.image, (self.main_display_size))

    self.update_image_size()
    print('**Image restored to initial values**')


  def show_image(self, promt='Title', img = np.array([])):

    if img.size == 0 \
       and self.height > self.main_display_size[0]:

      cv.imshow('Fitted Image', self.image_fit)

    elif img.size == 0:
      
      cv.imshow('Original Image', self.image)

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

      self.image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
      self.image_fit = cv.cvtColor(self.image_fit, cv.COLOR_BGR2GRAY)
      self.channels = 1

    
    except Exception as e: 

      print('Error: ', e)
    
    else: # convert image

      if show_image:

        self.show_image(promt='Image to grayscale')

  def resize_px(self, height = 0, width = 0,  interp = 1, show_image = False):
    '''
    Image size resize by absolute finel size
    Resized image keeps original aspect ratio by default providing 1 parameter,
    you could modify aspect ratio providing both height, width

    height > 0,

    width > 0,

    interp = 

    0 cv.INTER_NEAREST,

    1 cv.INTER_LINEAR,

    2 cv.INTER_CUBIC,

    4 cv.INTER_LANCZOS4,

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
      
      self.image =  cv.resize(self.image, image_shape, interpolation = interp)
      self.image_fit = cv.resize(self.image_fit, image_shape, interpolation = interp)
      self.update_image_size()

    except cv.error as e:
      if 'inv_scale_x > 0' in str(e):
        print('OpenCV error: Please provide a scale percent > 0 for resizing' )

    else:
      
      if show_image:

        print('Image resized by absolute pixels dimensions:')
        print('Original image size: ', str(self.clone.shape), ' px')
        print('Aspect ratio Width / Height: ', str(self.clone.shape[1]/self.clone.shape[0]))
        print('Resize factors: ', height, width, 'px')
        print('Resized  image size: ', str(self.image.shape), ' px')
        print('New aspect ratio: ', str(self.image.shape[1]/self.image.shape[0]))

        self.show_image(promt='Image resized by absolute pixels dimensions', )
    

  def resize_percent(self, height = 0, width = 0,  interp = 1, show_image = False):
    '''
    Percentual image size resize by percent reduce < 100 > expand
    Resized image keeps original aspect ratio by default providing 1 parameter,
    you could modify aspect ratio providing both height, width

    height > 0,

    width > 0,

    interp = 

    0 cv.INTER_NEAREST,

    1 cv.INTER_LINEAR,

    2 cv.INTER_CUBIC,

    4 cv.INTER_LANCZOS4,

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
      
      self.image =  cv.resize(self.image, image_shape, interpolation = interp)
      self.image_fit = cv.resize(self.image_fit, image_shape, interpolation = interp)
      self.update_image_size()
    
    except cv.error as e:
      if 'inv_scale_x > 0' in str(e):
        print('OpenCV error: Please provide a scale percent > 0 for resizing' )

    else:

      if show_image:

        print('Image resized by percentual values:')
        print('Original image size: ', str(self.clone.shape), ' px')
        print('Aspect ratio Width / Height: ', str(self.clone.shape[1]/self.clone.shape[0]))
        print('Resize factors: ', height, width, '%')
        print('Resized  image size: ', str(self.image.shape), ' px')
        print('New aspect ratio: ', str(self.image.shape[1]/self.image.shape[0]))


      self.show_image(promt='Image resized by percentual value')
  
  def crop_roi(self, show_roi = True):
      self.points_fit = []
      self.cropping = False

      def click_and_crop(event, x, y, flags, param):
          if event == cv.EVENT_LBUTTONDOWN:
              self.points_fit.append((x, y))
              self.cropping = True
          elif event == cv.EVENT_LBUTTONUP:
              self.points_fit.append((x, y))
              self.cropping = False

      cv.namedWindow("image")
      cv.setMouseCallback("image", click_and_crop)

      while True:
          clone_fit = self.image_fit
          if len(self.points_fit) >= 2:
              cv.polylines(clone_fit, [np.array(self.points_fit)], isClosed=True, color=(0, 255, 0), thickness=2)
          cv.imshow("image", clone_fit)
          key = cv.waitKey(1) & 0xFF

          if key == ord("r"):
              self.points_fit = []

          if key == ord("c") and len(self.points_fit) >= 3:
              # Find the minimum and maximum x and y coordinates of the polygon
              x_min, y_min = np.min(self.points_fit, axis=0)
              x_max, y_max = np.max(self.points_fit, axis=0)

              # Crop the maximum width and height region from the original image
              roi_fit = self.image_fit[y_min:y_max, x_min:x_max]

              # Scale roi_fit to roi
              roi_scaler = [self.width / self.main_display_size[0],
                            self.height / self.main_display_size[1]
                           ]
              roi = []
              for i in range(len(self.points_fit)):
                pair = (self.points_fit[i][0]*roi_scaler[0],
                        self.points_fit[i][1]*roi_scaler[1]
                       )
                roi.append(pair)

              print('ROI: \n')
              print(roi)                
                              
              # Find the minimum and maximum x and y coordinates of the polygon
              x_min, y_min = np.min(roi, axis=0)
              x_max, y_max = np.max(roi, axis=0)

              # Crop the maximum width and height region from the original image
              roi_image = self.image[int(y_min):int(y_max), 
                                     int(x_min):int(x_max)
                                    ]
              
              if show_roi:
                while True:
                  cv.imshow('Selected ROI', roi_image)  
                  key = cv.waitKey(1) & 0xFF
                  if key == 27:
                    break              

              self.image = roi_image
              self.image_fit = roi_fit

          if key == 27:  # Press Esc to exit
              break
          
      cv.destroyAllWindows()
  
  
  
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
          cv.putText(self.image_fit, text, (20, 40), font, 0.5, (255, 255, 255), 1)

          # Display the image with the GPS info
          self.show_image(promt='Image with exif GPS info')


        # Wait for a key press and then close the window
        cv.waitKey(0)
        cv.destroyAllWindows()
      
      #show exif GPS Coordinates
      print('Exif GPS coordinates ')
      print('Latitude: ', gps_dict['latitude'])
      print('Longitude:', gps_dict['longitude'])
      return gps_dict
