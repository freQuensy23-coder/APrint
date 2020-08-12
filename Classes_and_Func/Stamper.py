import config
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Stamper:
    """Класс отвечает за нанесение QR на пдф"""
    def __init__(self, qr, document_image):
        self.qr = qr.resize((config.QR_size, config.QR_size))  # изображение ресайзится до формата
        self.document = document_image  #Картинка - квитанция в формате фотографиии

    def do_stamp(self):
        """Поместить QR код на документ. Координаты из файла config.py"""
        self.__stap_qr()
        self.__stamp_waring_text()

    def __stap_qr(self):
        self.document.paste(self.qr, config.QR_left_corner)

    def __stamp_waring_text(self):
        waring_text = Image.open("C:\\Program Files (x86)\\Skver\\QRGenerator\\CheckQR.png")
        self.document.paste(waring_text, (config.QR_left_corner[0], config.QR_left_corner[1] + config.QR_size + 10))

    def show(self):
        """показать изобрадение документа используя стандартный просмотрщик фотографий"""
        self.document.show()

    def save(self, FILENAME):
        self.document.save(FILENAME=FILENAME)
