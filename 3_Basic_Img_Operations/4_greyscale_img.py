import cv2

# Load an image
image = cv2.imread('3_Basic_Img_Operations/sample_dog.jpg') #path_to_image

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()