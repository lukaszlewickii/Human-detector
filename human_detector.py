import cv2
import imutils

def humanDetection(file_path):
    image = cv2.imread(file_path)
    image = imutils.resize(image, width = min(400, image.shape[1]))

    body_classsifier = cv2.HOGDescriptor()
    body_classsifier.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (bodies, _) = body_classsifier.detectMultiScale(image, winStride = (3,3), padding = (3,3), scale = 1.01)

    for (x, y, w, h) in bodies:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    print(f"Number of people: {len(bodies)}")
    return image, len(bodies)