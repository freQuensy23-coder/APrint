import argparse

parser = argparse.ArgumentParser(description='QR Generator')

parser.add_argument('folder_path', action = 'store', help = 'Path to folder with PDFs')
parser.add_argument("-s",action = 'store_true', dest= "sQR", help = "Сохранять картинки QR")
parser.add_argument("-m",action = 'store_true', dest = "MergePDF", help = "Open image in default viewer")

one_pdf_parser = argparse.ArgumentParser(description='Scan and generate QRs in one PDF')
one_pdf_parser.add_argument('file_path', action = 'store', help = 'Path PDF file')