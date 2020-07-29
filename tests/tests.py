# Scanner test
import glob
from Scanner import *
from QR import *

PDF_Folder = r"C:\Users\mamet\PycharmProjects\QRgenerator\private\PDFs\*.pdf"   #Enter your folder here
paths = (glob.glob(PDF_Folder))
print("Found {} PDFs".format(str(len(paths))))

with open("res.txt", "a") as res:
    for path in paths:
        scanner = Scanner(path)
        data = scanner.data
        qr = QR(cost=data["cost"],name= data["name"],address= data["address"],period= data["period"])
        qr.qr.show()
        res.write(str(scanner))
        res.write("\n")