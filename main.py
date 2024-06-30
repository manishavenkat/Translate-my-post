import os
from transformers import MarianMTModel, MarianTokenizer
from tesseract_ocr import prompt_user_for_images, perform_ocr
import torch
from tqdm import tqdm
import pandas as pd

# load the MarianMT pretrained model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-de-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_text(text, model, tokenizer):
    # tokenize input
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    # translate
    with torch.no_grad():
        outputs = model.generate(**inputs)
    
    # decode translations
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return translated_text

def translate_dictionary(ocr_results, model, tokenizer):
    translated_results = {}

    for image_file, german_text in tqdm(ocr_results.items(), desc="Translating"):
        translated_text = translate_text(german_text, model, tokenizer)
        translated_results[image_file] = {
            'original_text': german_text,
            'translated_text': translated_text
        }

    return translated_results

# prompt user to input images
image_paths = prompt_user_for_images()

# use perform_ocr func from imported module tesseract_ocr
ocr_results = perform_ocr(image_paths)

# translate OCR'd text 
translated_results = translate_dictionary(ocr_results, model, tokenizer)

# # uncomment to convert dict to df and save as csv if needed
# translated_df = pd.DataFrame.from_dict(translated_results, orient='index')
# translated_df.to_csv('translated_ocr_results.csv', index=False)

# Display translations
for image_file, texts in translated_results.items():
    print(f"Image: {image_file}")
    print(f"Original Text: {texts['original_text']}")
    print(f"Translated Text: {texts['translated_text']}")
    print()
