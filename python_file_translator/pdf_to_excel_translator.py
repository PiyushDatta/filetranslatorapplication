import os
import openpyxl
# from io import StringIO
# from pdfminer.pdfparser import PDFParser, PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LAParams, LTTextBox, LTTextLine

import tensorflow as tf

sess = tf.Session()
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))
path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\filetranslatorapplication\\Bell.2015.Annual_sample.pdf"
path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\filetranslatorapplication\\sample_SF424_page2.pdf"

