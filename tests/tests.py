# Scanner test
import glob
from Classes.Scanner import *
from Classes.QR import *

PDF_Folder = r"/home/alex/Documents/PythonProjects/APrint/private/PDFs/*.pdf"   #Enter your folder here
paths = (glob.glob(PDF_Folder))
print("Found {} PDFs".format(str(len(paths))))

with open("res.txt", "a") as res:
    for i, path in enumerate(paths):
        scanner = Scanner(path)
        data = scanner.data
        qr = QR(cost=data["cost"],name= data["name"],address= data["address"],period= data["period"])
        qr.qr.save("qr({}).png".format(i))
        res.write(str(scanner))
        res.write("\n")