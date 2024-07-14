import cv2
import numpy as np

# Load the pre-trained MobileNet SSD model and the class names
net = cv2.dnn.readNetFromCaffe('6_Object_Detection/Models/deploy.prototxt', '6_Object_Detection/Models/mobilenet_iter_73000.caffemodel')
classNames = { 0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
               5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair', 10: 'cow',
               11: 'diningtable', 12: 'dog', 13: 'horse', 14: 'motorbike', 15: 'person',
               16: 'pottedplant', 17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }

# Load an image
image = cv2.imread('6_Object_Detection/sample_Bicycle_evolution-en.svg.png')
(h, w) = image.shape[:2]

# Preprocess the image for the network
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()

# Process the detections
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.2:  # Minimum confidence threshold
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        label = f"{classNames[idx]}: {confidence:.2f}"
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(image, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with detected objects
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()