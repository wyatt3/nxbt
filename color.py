# Importing the libraries openCV & numpy
import cv2
import numpy as np
# Dark: 59,82,227
# Light: 157, 87, 157
green = np.uint8([[[92, 62, 162]]])
  
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)
