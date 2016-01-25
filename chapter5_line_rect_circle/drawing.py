# import necessary packages
import numpy as np
import cv2

# 300 x 300 pixel image with 3 channels(as each represents R G B (8bits))
canvas = np.zeros((300, 300, 3), dtype="uint8")

# declare the colour of the line
green = (0, 255, 0)
# the first parameter represents the x axis, the second represents the y axis
# draw line on canvas, starting coordinate 0,0 finish at 300,300 and green
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# declare the colour of the line
red = (0, 0, 255)
# draw line the last parameter is a thickness of the line
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (10, 10), (60, 60), blue, 4)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centreX, centreY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centreX, centreY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)