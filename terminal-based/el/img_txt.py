from PIL import Image

import pytesseract
def img_txt():
    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = r'environment/lib/python3.10/site-packages/tesseract'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # Simple image to string
    file=input("Enter file name with extension:")
    text=pytesseract.image_to_string(Image.open(file))
    if(text.isspace()):
        print("\nThe Image does not contain any image\n")
    else:
        print("\n",text,"\n")