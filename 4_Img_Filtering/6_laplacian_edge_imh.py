import cv2

# Load an image
image = cv2.imread('4_Img_Filtering/sample_yVLsd.png', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian edge detection
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Display the Laplacian edge-detected image
cv2.imshow('Laplacian Edge Detection', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()