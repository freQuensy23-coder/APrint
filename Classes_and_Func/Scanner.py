import fitz
import re

from Exceptions.NotDocumentError import *

class Scanner:
    def __init__(self, page_text:str):
        self.page_text = page_text
        if page_text.find("Извещение") == -1:
            raise NotDocumentError
        self.cost = self.__get_cost()
        self.bank_id = self.__get_bank_id()
        self.period = self.__get_period() + self.__get_bank_id()
        self.name = self.__get_name()
        self.address = self.__get_address()
        self.data = {"cost": self.cost,
                     "bank_id": self.bank_id,
                     "period": self.period,
                     "name": self.name,
                     "address": self.address}

    def __str__(self):
        return "Р/с {bank_id}, Имя: {name} по адресу , Цена: {cost} за периуд {period}".format(
                bank_id=self.bank_id,
                cost=self.cost,
                period=self.period,
                name=self.name,
                add=self.address)

    def get_data_from_pdf(self, regex):
        """Get data from PDF using regex pattern"""
        match = re.search(regex, self.page_text)
        return match.group(0).replace(" ", "").replace("\n", "")

    def __get_cost(self):
        """Получает цену, указаную в платежке (прим. 	Сумма к оплате: 12 758,5)"""
        result = self.get_data_from_pdf(r"Сумма\sк\sоплате:\s([\d\s,]*)\n").replace("Суммакоплате:",
                                                                                    "").strip()  # Сумма к оплате: 12 758,5
        rub = int(result.split(",")[0])
        try:
            kop_str = result.split(",")[1]
            # kop = int(result.split(",")[1])
            if len(kop_str) == 1:
                kop = 10 * int(kop_str)
            else:
                kop = int(kop_str)
        except IndexError:
            kop = 0
            print("В платежке найденна сумма {rub} рублей и {kop} копеек!".format(rub=rub, kop='00'))
            return str(rub) + "00"
        print("В платежке найденна сумма {rub} рублей и {kop} копеек!".format(rub=rub, kop=kop))
        return str(rub * 100 + kop)

    def __get_bank_id(self):
        """Получает номер илчцегого счета (прим. № л/сч 000000048)"""
        return self.get_data_from_pdf(r"№\sл/сч\s([\d\D]*?)\s")

    def __get_period(self):
        """Получает периуд оплаты"""
        regex = re.search(
            r"Сумма\sк\sоплате:\s([\d\s,]*)\n([\s]*)за([\s]*)(Январь|Февраль|Март|Апрель|Май|Июнь|Июль|Август|Сенятябрь|Октябрь|Ноябрь|Декабрь) ([\d]*) г.",
            self.page_text)
        return regex.group(4) + " " + regex.group(5) + "г."

    def __get_name(self):
        """Получает имя платильщика"""
        return re.search(r"Плательщик: ([\w\W]*?)\n", self.page_text).group(1)

    def __get_address(self):
        """Получает адрес платильщика"""
        return re.search(r"Адрес: ([\w\W]*?)\n", self.page_text).group(1)
