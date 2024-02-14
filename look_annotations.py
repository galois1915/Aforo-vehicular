import cv2

cap = cv2.VideoCapture('./videos/video1_low.mp4')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

count = 0
while(cap.isOpened() or count < 1000):
  ret, frame = cap.read()

  if ret == True:
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break
  count=+1
 
cap.release()
cv2.destroyAllWindows()

#https://www.youtube.com/watch?v=zoic7UYo60M