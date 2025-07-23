from docling.document_converter import DocumentConverter
import os
import json
import re
from collections import defaultdict
from datetime import datetime

# Format the date as dd.mm.yyyy
date_str = datetime.now().strftime("%d.%m.%Y.%I.%M.%S")

# # Create a dynamic file path
# output_path = fr"C:\Users\GollapalliVishnuVard\Downloads\Docling Files\Test Inputs\extracted_text_{date_str}.txt"

# # Define source PDF
# source = r"C:\Users\GollapalliVishnuVard\Downloads\Docling Files\Test Inputs\Invoice 2.pdf"
# # json_output_path = r"C:\Users\GollapalliVishnuVard\Downloads\Docling Files\Test Inputs\extracted_text.json"
# text_output_path = fr"C:\Users\GollapalliVishnuVard\Downloads\Docling Files\Test Inputs\extracted_text_{date_str}.txt"

# # Convert the document
# converter = DocumentConverter()
# result = converter.convert(source).document
# # print(result.export_to_markdown())

# with open(text_output_path,"w",encoding="utf-8") as textfile:
#     textfile.write(result.export_to_markdown())

# print("Done!!!!")


source_folder = r"C:\Users\GollapalliVishnuVard\Downloads\Docling Files\Test Inputs\Differeny Formats"
output_folder = r"C:\Users\GollapalliVishnuVard\Downloads\Docling Files\Test Inputs\Differeny Formats"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)

    if not os.path.isfile(source_path):
        continue

    converter = DocumentConverter()
    result = converter.convert(source_path).document

    base_name, _ = os.path.splitext(filename)
    text_output_path = os.path.join(output_folder, f"{base_name}_{date_str}.txt")

    with open(text_output_path, "w", encoding="utf-8") as textfile:
        textfile.write(result.export_to_markdown())

    print(f"Processed and saved: {text_output_path}")

print("All files processed!")


# # Extract text content from ConversionResult
# if isinstance(result, tuple):
#     converted_text = result[0]
# elif hasattr(result, 'text'):
#     converted_text = result.text
# else:
#     converted_text = str(result)

# # Use regex to extract all text='...' values
# raw_texts = re.findall(r"text='(.*?)'", converted_text)

# # Filter: remove entries that are only 1 character (excluding currency symbols or units if needed)
# extracted_texts = [text for text in raw_texts if len(text.strip()) > 1]

# # Paths
# txt_output_path = os.path.splitext(source)[0] + "_text_only.txt"

# # Write JSON file
# with open(json_output_path, "w", encoding="utf-8") as json_file:
#     json.dump({"extracted_text": extracted_texts}, json_file, indent=4, ensure_ascii=False)

# # Write plain text file
# with open(txt_output_path, "w", encoding="utf-8") as txt_file:
#     txt_file.write("\n".join(extracted_texts))

# print(f"Structured text JSON saved to: {json_output_path}")
# print(f"Text-only output saved to: {txt_output_path}")