import cv2

# Load an image
image = cv2.imread('5_Img_Transformation/sample_monarch_in_may.jpg')

# Define the region of interest (ROI)
x, y, w, h = 150, 0, 500, 500  # x, y, width, height
cropped_image = image[y:y+h, x:x+w]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()