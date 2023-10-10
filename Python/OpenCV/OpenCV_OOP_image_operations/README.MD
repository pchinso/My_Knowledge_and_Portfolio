# Python

## About this repositorie

Objects Oriented class to perform OpenCV image operations with built-in methods

## ImageOperations class

### Class definition

```python

image_path = r'C:\xxx\full_path_to_image\image.jpg'
image = ImageOperations(image_path)

```

### Methods

The ImageOperations class modifies a copy of the original image in memory, while leaving the original image file unchanged.

To revert any changes made to the copy, use the image.restore_image() method.

```python


  image.crop_roi(show_roi=True)

  image.show_image()
  image.save_image()
# Show image
image.show_image()

# Save image 
# save_path='', 
# image_name='', 
# image_extension='' (.jpg .jpeg .png .bmp .gif .tiff .tif)
image.save_image(save_path='/home/pcs/Documents/xxx/',
                 image_name='copy',
                 image_extension = 'png'
                 )

# To Gray
image.to_gray_scale(show_image=True)

# Restore image to revert changes
image.restore_image()

# Resize image by especific pixel size size 
image.resize_px(height=400, width=500, interp=1, show_image=True)

# Restore image to revert changes
image.restore_image()

# Resize image by percent
image.resize_percent(height=10, width=10, interp=1, show_image=True)

# Crop image ROI
image.crop_roi(show_roi=True)

# Show original image ROI crop and save ROI as new image
image.show_image() 
image.save_image() 

# Restore image to revert changes
image.restore_image()

# Get image gps coordinates as dictionarie
gps_location = image.print_exif_GPS(show_image = True)

```

### Variables

The ImageOperations class contains main variables that represent key attributes of an image.

```python

# Image file
print('Full path of image: ' , image.path)
print('Image: ' , type(image.image))
print('Original Image cloned to revert changes: ' , type(image.image))
print('Resized Image fitted to display size: ' type(image_fit))

# Image size variables
print('Image Height: ',image.height) 
print('Image Widht: ',image.width) 
print('Image Channels: ',image.channels) 

# Display variables 
print('All displays size: ', image.display_size)
print('Main diaplays size: ', image.main_display_size) 

```
