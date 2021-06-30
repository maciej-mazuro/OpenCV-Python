import numpy as np
import cv2
from utils import CFEVideoConf

cap = cv2.VideoCapture(0)
save_path = 'saved-media/watermark.mp4'
frames_per_seconds = 24
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dimension)

while(True):
	ret, frame = cap.read()
	out.write(frame)
	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'): #nacisnij q zeby zatrzymac nagrywanie
		break

cap.release()
out.release()
cv2.destroyAllWindows()