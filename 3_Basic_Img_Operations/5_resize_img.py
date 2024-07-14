import cv2

# Load an image
image = cv2.imread('3_Basic_Img_Operations/sample_dog.jpg') #path_to_image

# Resize the image
resized_image = cv2.resize(image, (500, 500)) #streches_the_image

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()