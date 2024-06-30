# Introduction
Instagram currently allows post and story caption auto-translations ('see translation' button) but does not have the same feature for text on images. If you follow foreign language content on social media for educational purposes and want to cross-check your understanding of content on images, this feature would come in handy. Note that this repo is an illustration of the feature and is not integrated with Instagram in any manner. 

# What's in the repo 
main.py : clone the repo and run this file. It will ask you to upload images for text recognition and translation. It will output the image title, original text and translated text. It currently only supports German-English translation. 
tesseract_ocr.py: imported into main.py. This file does the text recognition part using Tesseract OCR trained on German data. 
scrape.py: I tested this implementation by scraping 50 Instagram posts from 'SZ' (German news media). Replace the username in this code with another public Instagram account to scrape other content. 

# Example 
Here is what an example output looks like:

Image: C8bhaqVt1tb_2.jpg

Original Text: Käse und Wein, Sauerkraut und Schoko-
lade, Bier und Miso. Was all diese Lebens-
und Genussmittel gemein haben?
Sie sind fermentiert —- sprich: Mit der
Unterstützung von Bakterien, Pilz- oder
Zellkulturen oder durch die Beigabe von
Enzymen umgewandelt und damit länger
haltbar oder überhaupt erst genießbar
gemacht worden.
Wenn in Kürze das Gemüsebeet aus allen
Nähten platzt, ist Fermentieren eine gute
Idee, um Gemüse einzumachen.
Süddeurtsche Zeitung

Translated Text: Cheese and wine, sauerkraut and chocolate lade, beer and miso. What all these food and drink have in common? They are fermented — i.e.: with the support of bacteria, fungus or cell cultures or by the addition of enzymes converted and thus long-lasting or first edible. When the vegetable bed bursts from all seams shortly, fermenting is a good idea to make vegetables. Süddeurtsche Zeitung
