import os
import numpy as np
import cv2

filename = 'video.mp4' #nazwa pliku; moze tez byc w formacie .avi
frames_per_seconds = 24.0 #liczba ramek na sekunde
initial_resolution = '720p' #rozdzielczosc

def change_resolution(cap, width, height): #zmiana rozdzielczosci
	cap.set(3, width)
	cap.set(4, height)

# Standardowe wymiary video
standard_dimension = {
	"480p": (640, 480),
	"720p": (1280,720),
	"1080p": (1920,1080),
	"4K": (3840,2160),
}

def get_dimension(cap, resolution='1080p'):
	width, height = standard_dimension['480p'] #wprowadzenie blednych danych - uzycie standardu 480p
	if resolution in standard_dimension:
		width, height = standard_dimension[resolution]
	change_resolution(cap, width, height)
	return width, height


#wymagane doinstalowanie kodeków pod konkretny typ video
video_type = {
	'avi' : cv2.VideoWriter_fourcc(*'XVID'),
	'mp4' : cv2.VideoWriter_fourcc(*'XVID'),	
}

def get_video_type(filename):
	filename, ext = os.path.splitext(filename)
	if ext in video_type:
		return video_type[ext]
	return video_type['mp4']

cap = cv2.VideoCapture(0)
dimension = get_dimension(cap, resolution=initial_resolution)
video_type_cv2 = get_video_type(filename)

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