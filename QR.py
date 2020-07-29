import qrcode
from private.config import *


class QR:
    """Генерирует QR код. need_divide_name - нужно ли разделять имя на имя фамилию и отчество методом .split()"""

    def __init__(self, cost, name, address, period, divide_name=True):
        self.cost = cost
        self.name = name.strip()
        self.address = address
        self.period = period
        self.settings = {"need_to_divide_name": divide_name}
        self.text = self.__get_text()
        self.qr = self.__generate_qr()

    def __generate_qr(self):
        """Generate Pil Image class object"""
        return qrcode.make(self.text)

    def __get_text(self):
        initials = self.name.split()
        while len(initials) < 3:  #На случай если у человека не было отчество итп
              initials += ""
        if self.settings["need_to_divide_name"] == True:
            result = ("""ST00012|Name={TSZ_name}""" +
                      """|PersonalAcc={TSZ_bank_id}""" +
                      """|BankName={TSZ_bank_name}""" +
                      """|BIC={TSZ_bic}""" +
                      """|CorrespAcc={CorrespAcc}""" +
                      """|KPP={TSZ_KPP}""" +
                      """|PayeeINN={TSZ_INN}""" +
                      """|lastName={last_name}""" +
                      """|FirstName={first_name}""" +
                      """|MiddleName={middle_name}""" +
                      """|Purpose={purpose}""" +
                      """|payerAddress={address}""" +
                      """|Sum={sum}""").format(TSZ_name = TSZ_name,
                                               TSZ_bank_id = Personal_Acc,
                                               TSZ_bank_name = Bank_name,
                                               TSZ_bic = BIC,
                                               CorrespAcc = CorrespAcc,
                                               TSZ_KPP = KPP,
                                               TSZ_INN = INN,
                                               last_name = initials[0],
                                               first_name = initials[1],
                                               middle_name = initials[2],
                                               purpose = ("за ЖКУ " + self.period),
                                               address = self.address,
                                               sum = self.cost
                                               )
        else:
            result = ("""ST00012|Name={TSZ_name}""" +
                      """|PersonalAcc={TSZ_bank_id}""" +
                      """|BankName={TSZ_bank_name}""" +
                      """|BIC={TSZ_bic}""" +
                      """|CorrespAcc={CorrespAcc}""" +
                      """|KPP={TSZ_KPP}""" +
                      """|PayeeINN={TSZ_INN}""" +
                      """|lastName={last_name}""" +
                      """|Purpose={purpose}""" +
                      """|payerAddress={address}}""" +
                      """|Sum={sum}""").format(TSZ_name = TSZ_name,
                                               TSZ_bank_id = Personal_Acc,
                                               TSZ_bank_name = Bank_name,
                                               TSZ_bic = BIC,
                                               CorrespAcc = CorrespAcc,
                                               TSZ_KPP = KPP,
                                               TSZ_INN = INN,
                                               last_name = self.name,
                                               purpose = ("за ЖКУ " + self.period),
                                               sum = self.cost
                                               )
        return result