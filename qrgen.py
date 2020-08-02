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


def add_pdf_to_merging(pdf_filename, pdf_write_object):
    pdf_read_object = PyPDF2.PdfFileReader(get_file_name(pdf_filename) + "_withQR.pdf")
    for page in range(pdf_read_object.numPages):
        pdf_write_object.addPage(pdf_read_object.getPage(page))
    return pdf_write_object


def main(args):
    global pdf_write_object
    # PATH_to_folder = '/home/alex/Documents/PythonProjects/APrint/private/PDFs/'
    # NEED_SAVE_QR = False
    # MERGE_PDFS = True
    #
    PATH_to_folder = args.folder_path
    NEED_SAVE_QR = args.sQR
    MERGE_PDFS = args.MergePDF

    print(str(args))

    paths = (glob.glob(PATH_to_folder + "\*.pdf"))
    print("Найдено {} PDF".format(str(len(paths))))

    for i, path in enumerate(paths):
        print(termcolor.colored(path, "green"))
        scanner = Scanner(path)
        data = scanner.data  # Информация о i-ой платёжке

        qr = QR(cost=data["cost"], name=data["name"], address=data["address"], period=data["period"])
        if NEED_SAVE_QR:
            qr.qr.save("qr({}).png".format(i))

        doc_image = pdf2image.convert_from_path(path)
        stamper = Stamper(qr=qr.qr, document_image=doc_image[0])
        stamper.do_stamp()

        try:
            printer = Printer(stamper.document, os.path.dirname(path) + '\\QR\\' + path.split("\\")[-1])
            printer.save()
        except FileNotFoundError as e:
            print(PATH_to_folder)
            os.mkdir(PATH_to_folder + "\\QR\\")
            print(termcolor.colored("Создал новую папку в " + str(PATH_to_folder + "\\QR\\"), "yellow"))
            result_filename = os.path.dirname(path) + "\\QR\\" + path.split("\\")[-1]
            stamper.document, os.path.dirname(path) + "\\QR\\"
            printer = Printer(stamper.document, result_filename)
            printer.save()

            # Merging pdfs
            if MERGE_PDFS:
                pdf_write_object = add_pdf_to_merging(result_filename, pdf_write_object)

        # except Exception as e:
        #     print(a)
        #     # print(termcolor.colored("Ошибка при сохранении файла" + str(path) + str(e), "red"))

        if MERGE_PDFS:
            merged_pdf = open(PATH_to_folder + "Merged.pdf", 'wb')
            pdf_write_object.write(merged_pdf)
            merged_pdf.close()


if __name__ == '__main__':

    args = parser.parse_args()
    main(args)
    print()
    print("Готого")
    pass

for i  in range(10):
    pass
