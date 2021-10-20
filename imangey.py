#!/bin/python3
import cv2
import numpy as np
import urllib.request
import screeninfo
import random
import json

# get screen info
MAX_WIDTH = 0
MAX_HEIGHT = 0
for m in screeninfo.get_monitors():
	if m.is_primary:
		MAX_WIDTH = m.width
		MAX_HEIGHT = m.height
		break

# show cat pics
for i in range(20):
	cv2.namedWindow(str(i))
	try:
		img = cv2.imdecode(np.asarray(bytearray(urllib.request.urlopen("https://cataas.com/cat").read()), dtype="uint8"), cv2.IMREAD_COLOR)
		cv2.imshow(str(i), img)
		cv2.moveWindow(str(i), random.randint(0, MAX_HEIGHT), random.randint(0, MAX_WIDTH))
	except urllib.error.HTTPError as e:
		print(e)
	

cv2.waitKey(0)
