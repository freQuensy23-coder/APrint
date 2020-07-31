# Scanner test
import sys
sys.path.append('/home/alex/Documents/PythonProjects/APrint/')

import glob
from Classes.Scanner import *
from Classes.QR import *
from Classes.Stamper import *
from Classes.Printer import *
import pdf2image

PDF_Folder = r"/home/alex/Documents/PythonProjects/APrint/private/PDFs/*.pdf"  # Enter your folder here
paths = (glob.glob(PDF_Folder))
print("Found {} PDFs".format(str(len(paths))))

with open("res.txt", "w") as res:
    for i, path in enumerate(paths):
        scanner = Scanner(path)
        data = scanner.data
        qr = QR(cost=data["cost"], name=data["name"], address=data["address"], period=data["period"])
        qr.qr.save("qr({}).png".format(i))

        doc_image = pdf2image.convert_from_path(path)
        stamper = Stamper(qr=qr.qr, document_image=doc_image[0])
        stamper.do_stamp()

        printer = Printer(stamper.document, path)
        printer.save()

        res.write(str(scanner))
        res.write("\n")
