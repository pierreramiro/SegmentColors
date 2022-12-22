import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
import matplotlib.pyplot as plt
import numpy as np
nemo = cv2.imread('./nemo.jpg')
nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
mask_white = cv2.inRange(hsv_nemo, light_white, dark_white)
final_mask = mask + mask_white
final_result = cv2.bitwise_and(nemo, nemo, mask=final_mask)
plt.subplot(1, 2, 1)
plt.imshow(nemo)
plt.subplot(1, 2, 2)
plt.imshow(final_result)
plt.show()
