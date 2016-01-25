from __future__ import print_function

import argparse
import cv2

# Declare CLI arguments after the program name and 2 parameters prog.py --image imagename.jpg
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
                required=True,
                help="Path to the image")

# args is signed to the path of the source image
args = vars(ap.parse_args())

# Declare a variable for holding source image path
image = cv2.imread(args["image"])
# Display the dimension of the image
print ("width: {} pixels". format(image.shape[1]))
print ("height : {} pixels". format(image.shape[0]))
print ("channel: {} pixels". format(image.shape[2]))

# Display the image using openCV GUI
cv2.imshow("Image", image)
# Over Write out the .png image as .jpg file
cv2.imwrite("newimage.png", image)
# O value pause the execution until any key is pressed
cv2.waitKey(0)