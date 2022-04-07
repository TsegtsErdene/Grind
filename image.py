import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def getIName(name):
    value = Image.open(name)
    text = tess.image_to_string(value, config='')
    return text