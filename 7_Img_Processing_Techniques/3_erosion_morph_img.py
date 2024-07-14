import cv2
import numpy as np

# Load a binary image
image = cv2.imread('7_Img_Processing_Techniques/sample_fingerprint.png', cv2.IMREAD_GRAYSCALE)

# Define a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the eroded image
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()