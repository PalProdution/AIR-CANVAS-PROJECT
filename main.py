import numpy as np
import cv2
from collections import deque


# default called trackbar function
def setValues(x):
    print("")


# Creating the trackbars needed for
# adjusting the marker colour These
# trackbars will be used for setting
# the upper and lower ranges of the
# HSV required for particular colour
cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors",
                   153, 180, setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors",
                   255, 255, setValues)
cv2.createTrackbar("Upper Value", "Color detectors",
                   255, 255, setValues)
cv2.createTrackbar("Lower Hue", "Color detectors",
                   64, 180, setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors",
                   72, 255, setValues)
cv2.createTrackbar("Lower Value", "Color detectors",
                   49, 255, setValues)

# Giving different arrays to handle colour
# points of different colour These arrays
# will hold the points of a particular colour
# in the array which will further be used
# to draw on canvas
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]

# These indexes will be used to mark position
# of pointers in colour array
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# The kernel to be used for dilation purpose
kernel = np.ones((5, 5), np.uint8)

# The colours which will be used as ink for
# the drawing purpose
colors = [(255, 0, 0), (0, 255, 0),
          (0, 0, 255), (0, 255, 255)]
colorIndex = 0

# Here is code for Canvas setup
paintWindow = np.zeros((471, 636, 3)) + 255

cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

# Loading the default webcam of PC.
cap = cv2.VideoCapture(0)
