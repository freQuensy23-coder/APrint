import sys

sys.path.append(r'C:\Users\mamet\PycharmProjects\QRgenerator')
sys.path.append(r'C:\Users\mamet\PycharmProjects\QRgenerator\poppler')

from Classes_and_Func.Scanner import *
from Classes_and_Func.QR import *
from Classes_and_Func.Stamper import *
from Classes_and_Func.Printer import *
from Classes_and_Func.PDF_Opener import *
from Classes_and_Func.get_time import *
from Classes_and_Func.QRParse import one_pdf_parser

from Exceptions.NotDocumentError import *

import pdf2image
import colorama
import PyPDF2

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


def stamp_pages(pdf_pages_images, pdf_pages_texts):
    stamped_images = []
    for page_number, page_text in enumerate(pdf_pages_texts):
        try:
            scanner = Scanner(page_text)  # raise NotDocumentError If page_number page does not contains receipt data
            data = scanner.data
            qr = QR(cost=data["cost"], name=data["name"], address=data["address"], period=data["period"])
            print(data["name"])
            stamper = Stamper(qr=qr.qr, document_image=pdf_pages_images[page_number])
            stamper.do_stamp()
            stamped_images.append(stamper.document)
        except NotDocumentError:
            # If page_number page does not contains receipt data
            print("На странице {i} не найден платёжный документ.".format(i=page_number))
            stamped_images.append(pdf_pages_images[page_number])
        except:
            print(page_text)
            print(0 / 0)
    return stamped_images


def main(file_path):
    global pdf_write_object

    # Get PIL.Image of every pdf page
    pdf_pages_images = get_pdf_images(file_path)

    # List where PIL.Images of payments will be placed after Stamper "stamp" them
    stamped_pages_images = []

    #get pages data

    stamped_pages_images = stamp_pages(pdf_pages_images, pdf_pages_texts)
    # List of images: Pdf's pages with QR and warning text
    print(stamped_pages_images)
    img = stamped_pages_images[0]
    img.save(get_file_name(file_path) + "_stamped_" + get_time() + ".pdf",
             resolution=100.0,
             save_all=True,
             append_images=stamped_pages_images[1:])


def get_pdf_images(FILE_PATH):
    """Returns list of PIL.Image"""
    return pdf2image.convert_from_path(FILE_PATH)


def get_pages_data(file_path):
    """Returns dict of lists with pages (fitz?) and their text"""
    pages_info = get_pdf_pages(open_PDF(file_path))
    pages = pages_info["pdf_pages"]
    pdf_pages_texts = pages_info["pdf_text"]
    print("Найдено {num} листов".format(num=len(pdf_pages_texts)))
    return

if __name__ == '__main__':
    args = one_pdf_parser.parse_args()
    main(args.file_name)
