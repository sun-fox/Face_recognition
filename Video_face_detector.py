import cv2, time

from test import face_cascade

camera_port = 0
camera = cv2.VideoCapture(camera_port)
# return_value, image = camera.read()
# cv2.imwrite("image.png", image)
a = 1
while True:
    a = a+1
    check, frame = camera.read()
    # print(check)
    print(frame)
    img = cv2.cvtColor(frame, 0)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)
    # print(type(faces))
    # print(faces)
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    # time.sleep(3)
    cv2.imshow("You", img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
print(a)
camera.release()
cv2.destroyAllWindows()