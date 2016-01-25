import numpy as np
import cv2


# Translate method takes three parameters, source image, x-axis and y-axis
def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image,
                             M,
                             (image.shape[1],
                              image.shape[0]))

    return shifted
