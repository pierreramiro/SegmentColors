import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ =="__main__":
    picture = cv2.imread('projects/Hidrocarburos/pictures/DJI_0623_T.JPG')
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    hsv_picture = cv2.cvtColor(picture, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv_picture)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    pixel_colors = picture.reshape((np.shape(picture)[0]*np.shape(picture)[1], 3))/255
    hsv=np.vstack((h.flatten(), s.flatten(), v.flatten()))
    cloudColor=np.hstack((hsv.T,pixel_colors))
    pd.DataFrame(cloudColor).to_csv("HSV_cloudColor.csv",index=None)
    # axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
    # axis.set_xlabel("Hue")
    # axis.set_ylabel("Saturation")
    # axis.set_zlabel("Value")
    # plt.show()
