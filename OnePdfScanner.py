import sys
from Classes_and_Func.Scanner import *
from Classes_and_Func.QR import *
from Classes_and_Func.Stamper import *
from Classes_and_Func.Printer import *
from Classes_and_Func.PDF_Opener import *
from Classes_and_Func.get_time import *
from Classes_and_Func.QRParse import one_pdf_parser

from Exceptions.NotDocumentError import *

from collections import namedtuple

from Classes_and_Func.PagesFunc import *

import pdf2image
import colorama
import PyPDF2

colorama.init()


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


def get_pdf_file_path(source_file_path):
    """Превращает путь до исходного файла в путь для конечного файла"""
    return connect(source_file_path.split(".")[:-1]) + "_stamped-" + get_time() + ".pdf"


def main(file_path):
    # Get pages texts
    _, pdf_pages_texts = get_pages_texts_docs(file_path)

    # Get PIL.Image of every pdf page
    pdf_pages_images = get_pdf_images(file_path)

    # get pages data
    pages_data = get_pages_data(pdf_pages_texts)

    stamped_pages_images = stamp_pages(pdf_pages_images, pages_data)
    # List of images: Pdf's pages with QR and warning text

    result_filename = get_pdf_file_path(source_file_path=file_path)
    save_images_to_pdf(stamped_pages_images, result_filename, quality=75)


if __name__ == '__main__':
    args = one_pdf_parser.parse_args()
    main(args.file_path)
