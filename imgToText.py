import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\droc1\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
import cv2

img = cv2.imread('istop2.png')
text = tess.image_to_string(img)
print(text)
