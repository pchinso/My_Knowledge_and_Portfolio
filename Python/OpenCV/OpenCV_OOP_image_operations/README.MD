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

```python

gray = image.to_gray_scale(show_image=True)

little = image.resize_px(height=40, width=50, interp=1, show_image=True)

big = image.resize_percent(height=110, width=150, interp=1, show_image=True)

```
