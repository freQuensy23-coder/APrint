# Scanner test
import glob
from Scanner import *

PDF_Folder = r"C:\Users\mamet\PycharmProjects\QRgenerator\private\PDFs\*.pdf"   #Enter your folder here
paths = (glob.glob(PDF_Folder))
print("Found {} PDFs".format(str(len(paths))))

with open("res.txt", "a") as res:
    for path in paths:
        scanner = Scanner(path)
        res.write(str(scanner))
        res.write("\n")