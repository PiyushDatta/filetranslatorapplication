import os
import PyPDF2 as pyPdf
import xlwt

path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\filetranslatorapplication\\Bell.2015.Annual_sample.pdf"

pdfFileObj = open(path_to_your_pdf, 'rb')
pdf_toread = pyPdf.PdfFileReader(path_to_your_pdf)

# 1 is the number of the page
page_one = pdf_toread.getPage(89)

# This will dump the content (unicode string)
# According to the doc, the formatting is dependent on the
# structure of the document
print(page_one.extractText())


class ExcelTranslator:
    def __init__(self, path, page_number):
        self.path = path
        self.numb = page_number

        # Create the workbook and create sheets
        wb = xlwt.Workbook()
        ws1 = wb.add_sheet("Test First Sheet")
        ws2 = wb.add_sheet("Test Second Sheet")

        # Write in the sheets
        ws1.write(0, 0, "This is sheet 1")
        ws2.write(0, 0, "This is sheet 2")

        # Save the workbook
        wb.save(os.path.dirname(path_to_your_pdf) + "\\Testing.xls")

test_sheet = ExcelTranslator(path_to_your_pdf, 52)
