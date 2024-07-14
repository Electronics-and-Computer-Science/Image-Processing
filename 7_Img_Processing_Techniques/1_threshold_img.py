import cv2

# Load an image in grayscale
image = cv2.imread('7_Img_Processing_Techniques/sample_desktop-wallpaper-demon-slayer-high-quality-demon-slayer-demon-slayer-phone.jpg', cv2.IMREAD_GRAYSCALE)

# Apply global thresholding
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()