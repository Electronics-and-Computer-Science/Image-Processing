import cv2

# Load an image
image = cv2.imread('3_Basic_Img_Operations/sample_dog.jpg') #path_to_image

# Define the region of interest (ROI)
x, y, w, h = 250, 0, 300, 500  # x, y, width, height
cropped_image = image[y:y+h, x:x+w]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()