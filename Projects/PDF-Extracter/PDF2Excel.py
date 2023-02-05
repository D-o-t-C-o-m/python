import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import pandas as pd
import os
import glob

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    with open(path, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()
    device.close()
    retstr.close()
    return text

pdf_files = glob.glob("*.pdf")
if not pdf_files:
    print("No PDF files found")
    exit()
    
for i, pdf_file in enumerate(pdf_files):
    print(f"{i}. {pdf_file}")

selected_pdf = int(input("Choose a PDF file (number): "))
pdf_file = pdf_files[selected_pdf]

# Extract the text from each page of the PDF
text = convert_pdf_to_txt(pdf_file)

# Handle special characters
text = text.encode("utf-8", "ignore").decode("utf-8")

# Split the text into lines
lines = text.split("\n")

# Remove empty lines
lines = [line for line in lines if line.strip()]

# Split each line into columns
data = [line.split() for line in lines]

# Convert the data to a pandas dataframe
df = pd.DataFrame(data)

# Remove comma and single quote characters from numbers
df = df.applymap(lambda x: x.replace(',', '').strip("'") if type(x) == str and (x.endswith("'") or x.endswith(',')) else x)
df = df.applymap(lambda x: float(x) if type(x) == str and x.isdigit() else x)

# Write the dataframe to a spreadsheet
filename, ext = os.path.splitext(pdf_file)
try:
    df.to_excel(f"{filename}.xlsx", index=False)
    print(f"Data written successfully to {filename}.xlsx")
except Exception as e:
    print(f"Error writing data to {filename}.xlsx:", e)
