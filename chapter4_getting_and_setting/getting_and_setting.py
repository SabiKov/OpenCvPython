# import necessary packages
from __future__ import print_function
import argparse
import cv2

# Read in CLI argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
                required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Access the first pixel of the image
(b, g, r) = image[0, 0]
print ("Default -> pixel at 0, 0 - Red: {}, Green: {}, Blue: {}"
       . format(r, g, b))

image[0:10, 0:10] = (0, 0, 255)
(b, g, r) = image[0, 0]
print ("Updated -> Pixel at 0, 0 - Red: {}, Green: {}, Blue: {}"
       . format(r, g, b))

# Manipulate and display 100 x 100 pixel region of the image
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# replace the 100 x 100 region with green colour
image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)
