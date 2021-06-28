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

cap = cv2.VideoCapture(0)
dimension = get_dimension(cap, resolution=initial_resolution)
while(True):

	ret, frame = cap.read()


	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'): #nacisnij q zeby zatrzymac nagrywanie
		break


cap.release()
cv2.destroyAllWindows()