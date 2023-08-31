import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        file_path = os.path.join(os.curdir, file)
        merger.append(file_path)

output_file = "combinedPDF's.pdf"
with open(output_file, "wb") as output_pdf:
    merger.write(output_pdf)

print("Merged PDF saved as", output_file)




