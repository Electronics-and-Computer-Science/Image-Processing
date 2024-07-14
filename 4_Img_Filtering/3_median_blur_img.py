import cv2

# Load an image
image = cv2.imread('4_Img_Filtering/sample_yVLsd.png') #path_to_image

# Apply median blurring
median_blurred_image = cv2.medianBlur(image, 9) #always_requires_odd_parameters_to_determine_central_pixel

# Display the median blurred image
cv2.imshow('Median Blurred Image', median_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()