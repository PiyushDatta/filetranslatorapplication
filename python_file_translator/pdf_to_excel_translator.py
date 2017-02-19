import os
import openpyxl
from io import StringIO
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\filetranslatorapplication\\Bell.2015.Annual_sample.pdf"
# path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\filetranslatorapplication\\sample_SF424_page2.pdf"


class ExcelTranslator:
    def __init__(self, path, page_number):
        self.path = path
        self.numb = page_number

        # Create the workbook and create sheets
        new_path = os.path.dirname(self.path) + "\\Testing.xlsx"
        wb = openpyxl.Workbook()
        wb.save(new_path)

        # Create sheets
        ws1 = wb.active
        ws2 = wb.create_sheet("Second sheet", 1)

        #
        # # Copy it so xlrd and xlwt can both us it
        # wb_copy = xlrd.open_workbook('.xls')
        # worksheet = wb.copy
        #
        # # Write in the sheets
        # prev_line = line = None
        #
        # ws1.write(0, 0, convert(path, 89))
        #
        # for line in convert(path, page_number):
        #     if represents_int(line):
        #         for col_num in range(0, 256):
        #             if ws1.cell(rowx=2, colx=col_num).value is None:
        #                 ws1.write(2, col_num, line)
        #             else:
        #                 pass
        #     else:
        #         pass
        # ws2.write(0, 0, "This is sheet 2")

        # Save the workbook
        wb.save(new_path)


def convert(file_name, pages):

    fp = open(file_name, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    content = ""
    for pageNumber, page in enumerate(doc.get_pages()):
        if pageNumber == pages:
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    content += lt_obj.get_text()
    return content


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(convert(path_to_your_pdf, 89))
test_sheet = ExcelTranslator(path_to_your_pdf, 89)
