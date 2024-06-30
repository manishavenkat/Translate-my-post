import os
from PIL import Image
import pytesseract
from tqdm import tqdm
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

# set tesseract path (if not added to Path in your system variables)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# use DEU (deutsch/german) config; download other languages from tesseract if needed
custom_config = r'--oem 3 --psm 6 -l deu'

def ocr_image(image_path, language='deu'):
    img = Image.open(image_path)
    
    custom_config = r'--oem 3 --psm 6 -l ' + language
    text = pytesseract.image_to_string(img, config=custom_config)
    
    return text.strip()

def prompt_user_for_images():
    root = Tk()
    root.withdraw()

    # open file upload window
    file_paths = askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    file_paths = list(file_paths)
    
    return file_paths

def perform_ocr(image_paths):
    ocr_results = {}

    with tqdm(total=len(image_paths), desc="OCR Processing") as pbar:
        for image_path in image_paths:
            text = ocr_image(image_path, language='deu')
            
            ocr_results[os.path.basename(image_path)] = text
            
            pbar.update(1)

    return ocr_results
