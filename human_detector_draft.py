import cv2
import imutils

image = cv2.imread('D:\Desktop\Python\Visual Studio Code\Zaawansowane programowanie\Projekt\people1.jpg')
image = imutils.resize(image, width = min(400, image.shape[1]))
#grey = cv2.cvtColor(image, cv2.COLOR_BayerRG2GRAY)

body_classsifier = cv2.HOGDescriptor()
body_classsifier.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

(bodies, _) = body_classsifier.detectMultiScale(image, winStride = (3,3), padding = (3,3), scale = 1.01)

for (x, y, w, h) in bodies:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
cv2.imshow('PeopleDetection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Number of people: {len(bodies)}")