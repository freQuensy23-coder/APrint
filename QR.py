import qrcode
import private.config

class QR:
    """Генерирует QR код. need_divide_name - нужно ли разделять имя на имя фамилию и отчество методом .split()"""
    def __init__(self, cost, name, address, period, need_divide_name=True):
        self.cost = cost
        self.name = name
        self.address = address
        self.period = period
        self.settings = {"need_divide_name":need_divide_name}
