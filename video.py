import cv2
import pytesseract
import matplotlib as plt
import numpy
pytesseract.pytesseract.tesseract_cmd = (r"C:\\Users\\my pc\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe")
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("output", 700, 900)
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture("video.mp4")
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot  open webcam")
cntr = 0;
while True:
    ret,frame = cap.read()
    cntr = cntr+1;
    if ((cntr%25)==0):
        imgH,imgW,_ = frame.shape
        x1,y1,w1,h1 = 0,0,imgH,imgW
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
            cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),3)
            cv2.putText(frame, imgchar, (x1 + int(w1/50),y1 + int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255),2)
            print(imgchar)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
cap.release()      
cv2.destroyAllWindows()
