import numpy as np
import cv2
import pickle


face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	#zamiana na skale szarosci
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
		#print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w] #region of interest
		roi_color = frame[y:y+h, x:x+w]

		id_, conf = recognizer.predict(roi_gray)
		if conf>=45 and conf <= 85:
			print(id_)
			print(labels[id_])

		img_item = "my_image.png"
		cv2.imwrite(img_item, roi_gray)
		#narysowanie prostokątu
		color = (255, 0, 0) #model BGR nie RGB; niebieski - zielony - czerwony; w zakresie od 0 do 255 -> niebieski prostokąt
		stroke = 1 #grubosc linii
		end_cord_x = x + w 
		end_cord_y = y + h 
		cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke) #okreslenie wspolrzednych prostokatu; x,y - start; 
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()