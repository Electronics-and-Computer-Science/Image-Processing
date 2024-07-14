import cv2

# Load an image
image = cv2.imread('3_Basic_Img_Operations/sample_dog.jpg') #path_to_image

# Display the image in a window
cv2.imshow('Loaded Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Destroy all the windows created by OpenCV
cv2.destroyAllWindows()