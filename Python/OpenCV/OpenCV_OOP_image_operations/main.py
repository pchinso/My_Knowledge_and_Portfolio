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

  # image.save_image(self, save_path='', image_name='', image_extension=''):
  # Save a image copy in same dir
  image.save_image()
  # Save a image copy in other dir
  image.save_image(save_path='/home/pcs/Documents/xxx/',
                   image_name='copy',
                   image_extension = 'png'
                   )

  # Image file
  print('Full path of image: ' , image.path)
  print('Image: ' , type(image.image))
  print('Original Image cloned to revert changes: ' , type(image.image))
  print('Resized Image fitted to display size: ', type(image.image_fit))

  # Initial Values 
  # Image size variables
  print('Image Height: ',image.height) 
  print('Image Widht: ',image.width) 
  print('Image Channels: ',image.channels) 

  # Display variables 
  print('All displays size: ', image.display_size)
  print('Main diaplays size: ', image.main_display_size) 

  image.show_image()

  # To Gray
  print('To Gray')
  image.to_gray_scale(show_image=True)

  # To gray values 
  # image size variables
  print('Image Height: ',image.height) 
  print('Image Widht: ',image.width) 
  print('Image Channels: ',image.channels)

  image.restore_image()


  # Resize image by especific pixel size
  image.resize_px(height=400, width=500, interp=1, show_image=True)

  # After Resize values 
  # image size variables
  print('Image Height: ',image.height) 
  print('Image Widht: ',image.width) 
  print('Image Channels: ',image.channels) 

  image.restore_image()
  
  # Resize image by percent
  image.resize_percent(height=10, width=10, interp=1, show_image=True)

  # After Resize values 
  # image size variables
  print('Image Height: ',image.height) 
  print('Image Widht: ',image.width) 
  print('Image Channels: ',image.channels) 

  image.restore_image()

  # Crop a ROI
  image.crop_roi(show_roi=True)

  print(image.original_im_ROI_points)

  # ROI values
  # image size variables
  print('Image Height: ',image.height) 
  print('Image Widht: ',image.width) 
  print('Image Channels: ',image.channels) 

  # image.save_image() Save ROI as image copy

  image.restore_image()

  # Get gps coordinates 
  gps_location = image.print_exif_GPS(show_image = True)

  # Original values
  # image size variables
  print('Image Height: ',image.height) 
  print('Image Widht: ',image.width) 
  print('Image Channels: ',image.channels) 