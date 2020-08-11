import sys

sys.path.append(r'C:\Users\mamet\PycharmProjects\QRgenerator')
sys.path.append(r'C:\Users\mamet\PycharmProjects\QRgenerator\poppler')

import glob
from Classes.Scanner import *
from Classes.QR import *
from Classes.Stamper import *
from Classes.Printer import *
import pdf2image
import argparse
import os
import termcolor
import colorama
import PyPDF2
import config
from QRParse import parser
import time

colorama.init()

pdf_write_object = PyPDF2.PdfFileWriter()

def get_file_path(args):
    return sys.argv[1]

def connect(str_list):
    """Connect all strings of array"""
    res = ""
    for el in str_list:
        res += el
    return res

def get_file_name(filename):
    """Returns filename without extension"""
    dot_array = filename.split(".")
    res = ""
    for el in dot_array[:-1]:
        res += el
    return res

def main(args):
    global pdf_write_object

    FILE_PATH = args.file_path
    NEED_SAVE_QR = args.sQR
    MERGE_PDFS = args.MergePDF

    print(str(args))

    f
