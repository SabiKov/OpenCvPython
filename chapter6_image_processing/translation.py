# import all necessary packages
import numpy as np
import argparse
import imutils
import cv2

# Enable CLI arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i",
                "--image",
                required=True,
                help="path to the image")
args = vars(ap.parse_args())

# image variable is signed the image
image = cv2.imread(args["image"])

# display the original image
cv2.imshow("Original", image)

# Define translation matrix (M) in floating points. [1,0,tx]
# where the tx value is the number of pixel, positive value shift the image to the right
# so shifting tx=25pixel to the right and tx=50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M,
                         (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

# so shifting tx=-50pixel to the left and tx=-90 pixels up
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M,
                         (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)