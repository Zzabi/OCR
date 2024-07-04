import cv2
import pytesseract

PATH_TO_IMAGE = r"path\to\image"
PATH_TO_TESSERACT = r"path\to\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = (PATH_TO_TESSERACT)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("output", 400, 300)
img = cv2.imread(PATH_TO_IMAGE)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 99, 1)
hImg, wImg, = img.shape

boxes = pytesseract.image_to_boxes(img)
text = pytesseract.image_to_string(img)
print(text)

for b in boxes.splitlines():
    b = b.split()
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y + 35), (w, hImg - h), (0, 0, 255), 2)
    cv2.putText(img, b[0], (x, hImg - y + 35), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("output", img)
cv2.waitKey(0)
