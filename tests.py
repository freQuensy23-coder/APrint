# Scanner test
import glob
from Scanner import *

PDF_Folder = "PDFs/*.pdf"
paths = (glob.glob(PDF_Folder))
print("Found {} PDFs".format(str(len(paths))))

with open("res.txt", "a") as res:
    for path in paths:
        scanner = Scanner(path)
        res.write(str(scanner))
        res.write("\n")