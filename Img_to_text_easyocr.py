import easyocr
import cv2

PATH_TO_IMAGE = r"path\to\image"

im = cv2.imread(PATH_TO_IMAGE)
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

reader = easyocr.Reader(["en"])
text = reader.readtext(im)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("output", 400, 300)
print(text)

for detection in text:
    top_Left = tuple([int(val + 35) for val in detection[0][0]])
    bottom_Right = tuple([int(val) for val in detection[0][2]])
    result = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    im = cv2.rectangle(im, top_Left, bottom_Right, (0, 0, 255), 1)
    im = cv2.putText(im, result, top_Left, font, 2, (0, 0, 255), 3)

cv2.imshow("output", im)
cv2.waitKey(0)
