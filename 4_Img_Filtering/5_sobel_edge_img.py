import cv2

# Load an image
image = cv2.imread('4_Img_Filtering/sample_yVLsd.png', cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=11) #ksize_should_be_odd_and_less_than_31
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=11) #ksize_should_be_odd_and_less_than_31

# Combine Sobel X and Y
sobel_combined = cv2.magnitude(sobelx, sobely)

# Display the Sobel edge-detected image
cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()