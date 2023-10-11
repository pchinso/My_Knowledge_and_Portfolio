import numpy as np
import cv2
import math
import os


from imageoperations import ImageOperations


# read input
img = (r'Python/OpenCV/OpenCV_OOP_image_operations/input/rectify.png')

cwd = os.getcwd()

image_path = os.path.join(cwd, r'images/rectify.png')

print(image_path)

image = ImageOperations(image_path)

image_ref  = cv2.imread(image_path)



#original img height width 
hh = image.height
ww = image.width

print('hh: ',hh)
print('ww:' ,ww)

image.crop_roi()
image.restore_image()


# specify input coordinates for corners of red quadrilateral in order TL, TR, BR, BL as x,
input = np.float32(image.original_im_ROI_points)


# get top and left dimensions and set to output dimensions of red rectangle
width = round(math.hypot(input[0,0]-input[1,0], input[0,1]-input[1,1]))
height = round(math.hypot(input[0,0]-input[3,0], input[0,1]-input[3,1]))
print("width:",width, "height:",height)

# set upper left coordinates for output rectangle
x = input[0,0]
y = input[0,1]

print('x:',x)
print('y:',y)


# specify output coordinates for corners of red quadrilateral in order TL, TR, BR, BL as x,
output = np.float32([[x,y], 
                     [x+width-1,y], 
                     [x+width-1,y+height-1], 
                     [x,y+height-1]])

print('input:',input)
print('output:',output)

output_ref = [[136., 113.], [207., 113.], [207., 195.], [136., 195.]]

print('output_ref:',output)

# compute perspective matrix
matrix = cv2.getPerspectiveTransform(input, output)

print(matrix)

# do perspective transformation setting area outside input to black
# Note that output size is the same as the input image size
imgOutput = cv2.warpPerspective(image.image, 
                                matrix, 
                                (ww,hh), 
                                cv2.INTER_LINEAR, 
                                borderMode=cv2.BORDER_CONSTANT, 
                                borderValue=(0,0,0)
                                )

# save the warped output
cv2.imwrite("red_quadrilateral_warped.jpg", imgOutput)

# show the result
cv2.imshow("result", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()
