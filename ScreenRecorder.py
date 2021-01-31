import cv2 #OpenCV
import pyautogui
import numpy as np


codec = cv2.VideoWriter_fourcc(*"MPEG")
output = cv2.VideoWriter("Recorded.mp4", codec , 60, (1920, 1080)) 

cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270) 


while True:
    img = pyautogui.screenshot() 
    frame = np.array(img) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    output.write(frame) 
    cv2.imshow('Recording', frame) 
    if cv2.waitKey(1) == ord('q'): 
        break
output.release()
cv2.destroyAllWindows()
