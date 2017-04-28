import os
from io import StringIO
import openpyxl
import tensorflow as tf

path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\filetranslatorapplication\\Bell.2015.Annual_sample.pdf"
path_to_your_pdf = "G:\\Piyush\\aaSelf_Programming\\aaPython\\filetranslatorapplication\\sample_SF424_page2.pdf"


sess = tf.Session()
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))