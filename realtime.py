import cv2
from PIL import Image
from pytesseract import pytesseract

PATH_TO_TESSERACT = r"path\to\tesseract.exe"

def tesseract():
    image_path = "test1.jpg"
    pytesseract.tesseract_cmd = PATH_TO_TESSERACT
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])

camera=cv2.VideoCapture(0)

while True:
    _,image=camera.read()
    cv2.imshow('image',image)
    
    if cv2.waitKey(1)& 0xFF==ord('s' or 'S'):
        cv2.imwrite('test1.jpg',image)
        tesseract()
        
    elif cv2.waitKey(1)& 0xFF==ord('q' or 'Q'):
        cv2.destroyAllWindows()
        break

camera.release()
cv2.destroyAllWindows()
