import cv2

# Load an image
image = cv2.imread('3_Basic_Img_Operations/sample_dog.jpg') #path_to_image

# Save the image to a new file
result = cv2.imwrite('3_Basic_Img_Operations/saved_image.jpg', image) #overwrites_the_files_if_has_same_name

if result:
    print("Image saved successfully.")
else:
    print("Error: Could not save the image.")