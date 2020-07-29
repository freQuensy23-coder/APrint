import config


class Stamper:
    """Класс отвечает за нанесение QR на пдф"""

    def __init__(self, qr, document):
        self.qr = qr.resize((config.QR_size, config.QR_size))  # изображение ресайзится до формата
        self.document = document

    def do_stamp(self):
        """Поместить QR код на документ. Координаты из файла config.py"""
        self.document.paste(self.qr, config.QR_left_corner)

    def show(self):
        self.document.show()

    def save(self, FILENAME):
        self.document.save(FILENAME=FILENAME)
