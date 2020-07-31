import sys

sys.path.append('/home/alex/Documents/PythonProjects/APrint/')

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

def main(args):
    PATH_to_folder = '/home/alex/Documents/PythonProjects/APrint/private/PDFs/'
    NEED_SAVE_QR = False

    paths = (glob.glob(PATH_to_folder + "*.pdf"))
    print("Найдено {} PDF".format(str(len(paths))))

    for i, path in enumerate(paths):
        print(path)
        scanner = Scanner(path)
        data = scanner.data  # Информация о i-ой платёжке
        qr = QR(cost=data["cost"], name=data["name"], address=data["address"], period=data["period"])
        if NEED_SAVE_QR:
            qr.qr.save("qr({}).png".format(i))
        doc_image = pdf2image.convert_from_path(path)
        stamper = Stamper(qr=qr.qr, document_image=doc_image[0])
        stamper.do_stamp()
        try:
            printer = Printer(stamper.document, os.path.dirname(path)+ "/QR/" + path.split("/")[-1])
            printer.save()
        except FileNotFoundError:
            os.mkdir(PATH_to_folder + "QR")
            print("Создал новую папку в ", (PATH_to_folder + "QR"))
            stamper.document, os.path.dirname(path) + "/QR/"
            printer = Printer(stamper.document, os.path.dirname(path) + "/QR/" + path.split("/")[-1])
            printer.save()
        except Exception as e:
            print(termcolor.colored("Ошибка при сохранении файла" + str(path) + str(e), "red"))

if __name__ == '__main__':
    main("")