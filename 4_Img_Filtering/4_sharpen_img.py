import cv2
import numpy as np

# Load an image
image = cv2.imread('4_Img_Filtering/sample_yVLsd.png') #path_to_image

# Create a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

# Apply the sharpening kernel to the image
sharpened_image = cv2.filter2D(image, -1, kernel)

# Display the sharpened image
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
