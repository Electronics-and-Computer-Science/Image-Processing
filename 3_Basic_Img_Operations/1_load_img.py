import cv2

# Load an image from a file
image = cv2.imread('3_Basic_Img_Operations/sample_dog.jpg') #path_to_image

# Check if the image has been loaded properly
if image is None:
    print("Error: Could not open or find the image.")
else:
    print("Image loaded successfully.")