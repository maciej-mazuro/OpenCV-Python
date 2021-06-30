import numpy as np
import cv2
from utils import CFEVideoConf, image_resize

cap = cv2.VideoCapture(0)

save_path = 'saved-media/watermark.mp4'
frames_per_seconds = 24 # taka wartosc moze nie dzialac
config = CFEVideoConf(cap, filepath=save_path, res='720p') # 720p w zaleznosci od kamery
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)

img_path = "C:\\Users\\ADMIN\\projects\\OpenCV-Python/cfe-coffee.jpg" #cala sciezka + podwojne ukosniki
logo = cv2.imread(img_path, -1) # -1 -> get raw file
watermark = image_resize(logo, height=50)
cv2.imshow('watermark', watermark)

while(True):
	ret, frame = cap.read()

	# print(frame[50, 150])
	# start_cord_x = 50
	# start_cord_y = 150
	# color = (255, 0, 0) 
	# stroke = 1 
	# w = 100
	# h = 200
	# end_cord_x = start_cord_x + w 
	# end_cord_y = start_cord_y + h 
	# cv2.rectangle(frame, (start_cord_x, start_cord_y), (end_cord_x, end_cord_y), color, stroke)
	# print(frame[start_cord_x:end_cord_x, start_cord_y:end_cord_y])

	frame_h, frame_w, frame_s = frame.shape
	print(frame.shape) #okreslenie wymiarow
	gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
	print(gray.shape)
	#stworzenie pokrycia z 4 kanałami - BGR i alfa -> przejrzystosc
	overlay = np.zeros



	#out.write(frame)
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'): #nacisnij q zeby zatrzymac nagrywanie
		break

cap.release()
out.release()
cv2.destroyAllWindows()