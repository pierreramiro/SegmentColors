import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    picture1 = cv2.imread('projects/Hidrocarburos/pictures/DJI_0608_T.JPG')
    picture2 = cv2.imread('projects/Hidrocarburos/pictures/DJI_0623_T.JPG')
    picture1 = cv2.cvtColor(picture1, cv2.COLOR_BGR2RGB)
    hsv_picture1 = cv2.cvtColor(picture1, cv2.COLOR_RGB2HSV)
    picture2 = cv2.cvtColor(picture2, cv2.COLOR_BGR2RGB)
    hsv_picture2 = cv2.cvtColor(picture2, cv2.COLOR_RGB2HSV)
    
    # H: 0-80
    # S: 0-180
    # V: 200-255
        
    low_color=(0,0,200)
    high_color=(80,180,255)
    """Procesamos la primera imagen"""
    mask = cv2.inRange(hsv_picture1, low_color,high_color)
    result1 = cv2.bitwise_and(picture1, picture1, mask=mask)

    mask = cv2.inRange(hsv_picture2, low_color,high_color)
    result2 = cv2.bitwise_and(picture2, picture2, mask=mask)    
    xLen=3#(picture1.shape)[0]
    yLen=3#(picture1.shape)[1]
    plt.subplot(2, 2, 1)
    plt.imshow(picture1,extent=[-int((xLen-1)/2),int((xLen-1)/2),-int((yLen-1)/2),int((yLen-1)/2)])
    plt.subplot(2, 2, 2)
    plt.imshow(result1,extent=[-int((xLen-1)/2),int((xLen-1)/2),-int((yLen-1)/2),int((yLen-1)/2)])
    xLen=(picture2.shape)[0]
    yLen=(picture2.shape)[1]
    plt.subplot(2, 2, 3)
    plt.imshow(picture2,extent=[-int((xLen-1)/2),int((xLen-1)/2),-int((yLen-1)/2),int((yLen-1)/2)])
    plt.subplot(2, 2, 4)
    plt.imshow(result2,extent=[-int((xLen-1)/2),int((xLen-1)/2),-int((yLen-1)/2),int((yLen-1)/2)])
    plt.show()

"""
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
"""