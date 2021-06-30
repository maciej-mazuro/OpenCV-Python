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
	out.write(frame)
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'): #nacisnij q zeby zatrzymac nagrywanie
		break

cap.release()
out.release()
cv2.destroyAllWindows()