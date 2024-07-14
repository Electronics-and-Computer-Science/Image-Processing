import cv2

# Load an image
image = cv2.imread('5_Img_Transformation/sample_monarch_in_may.jpg')

# Resize the image to half of its original size
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()