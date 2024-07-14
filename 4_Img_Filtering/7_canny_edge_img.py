import cv2

# Load an image
image = cv2.imread('4_Img_Filtering/sample_yVLsd.png', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
canny_edges = cv2.Canny(image, 100, 200)

# Display the Canny edge-detected image
cv2.imshow('Canny Edge Detection', canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()