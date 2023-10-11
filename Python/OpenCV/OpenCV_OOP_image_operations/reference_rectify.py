import numpy as np
import cv2
import math
# https://stackoverflow.com/questions/64825835/opencv-python-how-to-warpperspective-a-large-image-based-on-transform-inferred
# read input
img = cv2.imread("/home/pcs/Documents/Python/My_Knowledge_and_Portfolio/images/rectify.png")
hh, ww = img.shape[:2]

print('hh: ',hh)
print('ww:' ,ww)


# specify input coordinates for corners of red quadrilateral in order TL, TR, BR, BL as x,
input = np.float32([[136,113], [206,130], [173,207], [132,196]])

# get top and left dimensions and set to output dimensions of red rectangle
width = round(math.hypot(input[0,0]-input[1,0], input[0,1]-input[1,1]))
height = round(math.hypot(input[0,0]-input[3,0], input[0,1]-input[3,1]))
print("width:",width, "height:",height)

# set upper left coordinates for output rectangle
x = input[0,0]
y = input[0,1]

# specify output coordinates for corners of red quadrilateral in order TL, TR, BR, BL as x,
output = np.float32([[x,y], [x+width-1,y], [x+width-1,y+height-1], [x,y+height-1]])

# compute perspective matrix
print('input:',input)
print('output:',output)

matrix = cv2.getPerspectiveTransform(input,output)
print(matrix)

# do perspective transformation setting area outside input to black
# Note that output size is the same as the input image size
imgOutput = cv2.warpPerspective(img, matrix, (ww,hh), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))

# save the warped output
cv2.imwrite("red_quadrilateral_warped.jpg", imgOutput)

# show the result
cv2.imshow("result", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

hh:  288
ww: 277 

>>> x
136.0
>>> y
113.0

input: [[136. 113.]
 [206. 130.]
 [173. 207.]
 [132. 196.]]
output: [[136. 113.]
 [207. 113.]
 [207. 195.]
 [136. 195.]]


>>> output = np.float32([[x,y], [x+width-1,y], [x+width-1,y+height-1], [x,y+height-1]])
>>> output
array([[136., 113.],
       [207., 113.],
       [207., 195.],
       [136., 195.]], dtype=float32)

>>> print(matrix)
[[ 9.09696753e-01 -4.53175060e-01  2.84742022e+01]
 [ 2.00619237e-02  2.19183670e-02  7.87007750e+01]
 [ 1.09930771e-03 -3.60154975e-03  1.00000000e+00]]
>>> 
>>> 

'''