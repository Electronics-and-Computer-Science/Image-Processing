import cv2

# Load an image
image = cv2.imread('4_Img_Filtering/sample_yVLsd.png') #path_to_image

# Apply average blurring
blurred_image = cv2.blur(image, (9, 9))

# Display the blurred image
cv2.imshow('Average Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()