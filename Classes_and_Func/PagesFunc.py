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


def get_pages_texts_docs(file_path):
    """Returns dict of lists with pages (fitz?) and their text"""
    pages_data = namedtuple("data", ["pages", "text"])
    pages_info = get_pdf_pages(open_PDF(file_path))
    pages = pages_info["pdf_pages"]
    pdf_pages_texts = pages_info["pdf_text"]
    result = pages_data(pages, pdf_pages_texts)
    return result


def get_pdf_images(FILE_PATH):
    """Returns list of PIL.Image"""
    return pdf2image.convert_from_path(FILE_PATH)


def get_pages_data(pages_texts):
    pages_data = []

    def get_page_data(page_text):
        """Возвращает словарик с информацией о платежке по данному тексту.
        Если переданный текст не является платёжкой то вызывает NotDocumentError """
        scanner = Scanner(page_text)  # raise NotDocumentError If page_number page does not contains receipt data
        data = scanner.data
        return data

    for page_num, page_text in enumerate(pages_texts):
        try:
            pages_data.append(get_page_data(page_text))
        except NotDocumentError:
            pages_data.append(None)
    return pages_data


def stamp_pages(pdf_pages_images, datas):
    """datas -лист словариков с информацией, которую нужно добавить на i-ую платежку ( {"cost": self.cost,
                     "bank_id": self.bank_id,
                     "period": self.period,
                     "name": self.name,
                     "address": self.address})
        Если на i-ую платежку не нужно добавлять картинку, то datas[i] = None
                    """
    stamped_images = []
    for page_number, image in enumerate(pdf_pages_images):
        if datas[page_number] is not None:
            data = datas[page_number]
            qr = QR(cost=data["cost"], name=data["name"], address=data["address"], period=data["period"])
            stamper = Stamper(qr=qr.qr, document_image=pdf_pages_images[page_number])
            stamper.do_stamp()
            stamped_images.append(stamper.document)
        else:
            # If page_number page does not contains receipt data
            # print("На странице {i} не найден платёжный документ.".format(i=page_number))
            stamped_images.append(pdf_pages_images[page_number])
    return stamped_images


def get_pdf_file_path(source_file_path):
    """Превращает путь до исходного файла в путь для конечного файла"""
    return connect(source_file_path.split(".")[:-1]) + "_stamped-" + get_time() + ".pdf"


def save_images_to_pdf(images, filepath, quality = 75):
    """Save all PIL.Images to pdf file"""
    images[0].save(filepath,
                   resolution=100.0,
                   save_all=True,
                   append_images=images[1:],
                   quality=quality
                   )
