import config


class Stamper:
    """Класс отвечает за нанесение QR на пдф"""

    def __init__(self, qr, document_image):
        self.qr = qr.resize((config.QR_size, config.QR_size))  # изображение ресайзится до формата
        self.document = document_image  #Картинка - квитанция в формате фотографиии

    def do_stamp(self):
        """Поместить QR код на документ. Координаты из файла config.py"""
        self.document.paste(self.qr, config.QR_left_corner)

    def show(self):
        """показать изобрадение документа используя стандартный просмотрщик фотографий"""
        self.document.show()

    def save(self, FILENAME):
        self.document.save(FILENAME=FILENAME)
