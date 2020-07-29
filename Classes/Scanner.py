import fitz
import re


class Scanner(object):
    """Клас отвечает за получение текста из PDF документа"""

    def __init__(self, path):
        self.path = path
        self.document = doc = fitz.open(self.path)
        self.page_text = self.__scan()
        self.cost = self.__get_cost()
        self.bank_id = self.__get_bank_id()
        self.period = self.__get_period()
        self.name = self.__get_name()
        self.address = self.__get_address()
        self.data = {"path":self.path,
                     "cost":self.cost,
                     "bank_id":self.bank_id,
                     "period":self.period,
                     "name":self.name,
                     "address":self.address}

    def __str__(self):
        return "PDF {pdf}  :  Р/с {bank_id}, Имя: {name} по адресу {add}, Цена: {cost} за периуд {period}".format(
            bank_id = self.bank_id,
            cost = self.cost,
            period = self.period,
            name = self.name,
            pdf = self.path,
            add = self.address)

    def __scan(self):
        """Получает весь текст из пдф -ки"""
        page = self.document.loadPage(0)
        page_text = page.getText("text")
        return page_text

    def get_data_from_pdf(self, regex):
        """Get data from PDF using regex pattern"""
        match = re.search(regex, self.page_text)
        return match.group(0).replace(" ", "").replace("\n", "")

    def __get_cost(self):
        """Получает цену, указаную в платежке (прим. 	Сумма к оплате: 12 758,5)"""
        result = self.get_data_from_pdf(r"Сумма\sк\sоплате:\s([\d\s,]*)\n") # Сумма к оплате: 12 758,5
        return result.replace("Суммакоплате:", "")

    def __get_bank_id(self):
        """Получает номер илчцегого счета (прим. № л/сч 000000048)"""
        return self.get_data_from_pdf(r"№\sл/сч\s([\d\s\w]*?)\n").replace("№л/сч","")

    def __get_period(self):
        """Получает периуд оплаты"""
        regex = re.search(r"Сумма\sк\sоплате:\s([\d\s,]*)\n([\s]*)за([\s]*)(Январь|Февраль|Март|Апрель|Май|Июнь|Июль|Август|Сенятябрь|Октябрь|Ноябрь|Декабрь) ([\d]*) г.", self.page_text)
        return regex.group(4) + " " + regex.group(5) + "г."

    def __get_name(self):
        """Получает имя платильщика"""
        return re.search(r"Плательщик: ([\w\W]*?)\n", self.page_text).group(1)

    def __get_address(self):
        """Получает адрес платильщика"""
        return re.search(r"Адрес: ([\w\W]*?)\n", self.page_text).group(1)