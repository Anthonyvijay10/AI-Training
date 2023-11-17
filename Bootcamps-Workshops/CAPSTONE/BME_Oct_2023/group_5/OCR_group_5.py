# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1STGGfj5gYDjG2nf1gyMBZlLFyHbI2czG
"""

!pip install pytesseract
!sudo apt-get install tesseract-ocr
!sudo apt-get install libtesseract-dev
!pip install pdf2image
!apt-get install -y poppler-utils
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# Path to the PDF file
pdf_path = "/Patient details.pdf"

# Paths to the image files
image_paths = ["/phto list_page-0001.jpg", "/phto list_page-0002.jpg", "/phto list_page-0003.jpg"]

# Convert PDF to images
pdf_images = convert_from_path(pdf_path)

# Perform OCR on PDF images
pdf_extracted_text = []
for i, pdf_image in enumerate(pdf_images):
 pdf_image_path = f"/content/pdf_page_{i}.png"
 pdf_image.save(pdf_image_path, "PNG")
 pdf_extracted_text.append(pytesseract.image_to_string(Image.open(pdf_image_path)))

# Perform OCR on additional images
image_extracted_text = []
for image_path in image_paths:
 image_text = pytesseract.image_to_string(Image.open(image_path))
 image_extracted_text.append(image_text)

# Combined extracted text from PDF and images
all_extracted_text = pdf_extracted_text + image_extracted_text

# Print extracted text
print("Extracted Text:")
for text in all_extracted_text:
 print(text)

# Save extracted text to a text file
output_text = "\n".join(all_extracted_text)
output_file_path = "/content/extracted_text.txt"
with open(output_file_path, "w") as text_file:
 text_file.write(output_text)

print(f"Extracted text saved to: {output_file_path}")

# Create a summary from the extracted text
summary = " ".join(all_extracted_text)

# Save the summary to a summary file
summary_file_path = "/content/summary.txt"
with open(summary_file_path, "w") as summary_file:
 summary_file.write(summary)

print(f"Summary saved to: {summary_file_path}")