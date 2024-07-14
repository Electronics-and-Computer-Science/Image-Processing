import cv2

# Load an image
image = cv2.imread('4_Img_Filtering/sample_yVLsd.png') #path_to_image

# Apply Gaussian blurring
gaussian_blurred_image = cv2.GaussianBlur(image, (9, 9), 0) #always_requires_odd_parameters_to_determine_central_pixel

# Display the Gaussian blurred image
cv2.imshow('Gaussian Blurred Image', gaussian_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()