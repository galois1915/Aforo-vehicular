import sys
import cv2
import json
import torch
from models.yolo import Model
from models.experimental import attempt_load

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
 
cap = cv2.VideoCapture('../data/videos/video1.mp4')
#annotations = json.load(open("./data/FineTuned_YOLO/annotations/instances_default.json"))

model = Model("yolov7-tiny.yaml")
weights = "yolov7-tiny.pt"

model = attempt_load(weights, map_location=device)
model.eval()

cv2.waitKey(0)
cv2.destroyAllWindows()

## VIDEO
#count = 0
#while(cap.isOpened() or count < 1000):
#  ret, frame = cap.read()

#  if ret == True:
#    cv2.imshow('Frame',frame)
#    if cv2.waitKey(25) & 0xFF == ord('q'):
#      break
#  else: 
#    break
#  count=+1
 
#cap.release()
#cv2.destroyAllWindows()



https://www.youtube.com/watch?v=zoic7UYo60M