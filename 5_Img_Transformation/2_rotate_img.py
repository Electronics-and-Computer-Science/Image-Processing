import cv2

# Load an image
image = cv2.imread('5_Img_Transformation/sample_monarch_in_may.jpg')

# Get the image dimensions
(h, w) = image.shape[:2]

# Define the center of the image
center = (w // 2, h // 2)

# Define the rotation matrix
angle = 90  # Rotation angle in degrees
scale = 1.0  # Scale factor
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Rotate the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Display the rotated image
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()