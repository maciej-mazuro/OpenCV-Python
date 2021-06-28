import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')


cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	#zamiana na skale szarosci
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
		print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w] #region of interest
		roi_color = frame[y:y+h, x:x+w]
		img_item = "my_image.png"
		cv2.imwrite(img_item, roi_gray)
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()