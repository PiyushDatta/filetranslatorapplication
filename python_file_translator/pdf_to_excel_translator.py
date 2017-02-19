import os
import PyPDF2 as pyPdf

path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\sample_SF424_page2.pdf"
pdfFileObj = open(path_to_your_pdf, 'rb')
pdf_toread = pyPdf.PdfFileReader(path_to_your_pdf)

# 1 is the number of the page
page_one = pdf_toread.getPage(0)

# This will dump the content (unicode string)
# According to the doc, the formatting is dependent on the
# structure of the document
print(page_one.extractText())
