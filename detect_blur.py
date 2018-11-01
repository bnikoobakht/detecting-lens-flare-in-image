# USAGE
# python2.7 detect_blur.py --image directory/image

# import the necessary packages
from imutils import paths
import argparse
import cv2

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=208.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())
print('\t\t\t'"#################################################")
print('\t\t\t'"#   1   ---->     means the image is Blurry     #")
print('\t\t\t'"#   0   ---->     means the image is Not Blurry #")
print('\t\t\t'"#################################################")

# load the image, convert it to grayscale, and compute the
# focus measure of the image using the Variance of Laplacian
# method
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
#text = "Not Blurry"

# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < args["threshold"]:
	#text = "Blurry"
        #print("Variance of laplacian=",fm)
        print('\t\t'"1")
elif fm > args["threshold"]:
          print('\t\t'"0")
#Debugging information
# show the image
#cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
#	cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
#cv2.imshow("Image", image)
#key = cv2.waitKey(0)
