import cv2 as cv
import sys

'''
OpenCV Show image 

'''

if __name__ =="__main__":

  img = cv.imread(cv.samples.findFile('./input/test.jpg'))


  if img is None:
    sys.exit("Could not read the image.")

  cv.imshow("Display window", img)

  k = cv.waitKey(0)

  if k == ord("s"):
    cv.imwrite("./input/test.png", img)
