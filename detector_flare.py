# USAGE
# python2.7 match1.py --image directory/image
import cv2 as cv
import numpy as np
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input directory of images")
args = vars(ap.parse_args())


print('\t\t\t'"#################################################")
print('\t\t\t'"#   1   ---->     means the image is flare      #")
print('\t\t\t'"#   0   ---->     means the image is Not flare  #")
print('\t\t\t'"#################################################")
# Read input image and convert it to grayscale
img_rgb = cv.imread(args["image"])
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('small.JPG',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

#Debugging--> produce the image with the specified
#lens flare.

#for pt in zip(*loc[::-1]):
#    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#print pt,pt[0],pt[1]
if len(loc[0]) != 0.0:
        print('\t\t'"1")
elif len(loc[0]) == 0.0:
          print('\t\t'"0")
#Debugging
#cv.imwrite('res.png',img_rgb)
