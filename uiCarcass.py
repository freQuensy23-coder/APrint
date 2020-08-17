from Classes_and_Func.PagesFunc import *
from tkinter import *
from tkinter.ttk import *

# Импорт библиотек

pages_texts, images, pages_data, insert_pages_data = 0, 0, 0, 0  # Глобальные переменный для getting_data_from_pdf
win = Tk()  # Создание окна
combo_var = StringVar  # Создание переменной в которую загружается положение выпадающего окна combo


# для получение значения combo_var.get()


def getting_data_from_pdf(file_path):  # получене даных из pdf
    global pages_data, pages_texts, images
    _, pages_texts = get_pages_texts_docs(file_path)
    images = get_pdf_images(file_path)
    pages_data = get_pages_data(pages_texts)


def main(file_path):  # основная функция
    getting_data_from_pdf(file_path)  # получене даных из pdf
    global pages_data, pages_texts, images, insert_pages_data

    def ok_bind():  # Вызывается при нажатии на OK
        global images, pages_data, file_path
        stamped_images = stamp_pages(images, pages_data)
        final_file_path = get_pdf_file_path(file_path)
        save_images_to_pdf(stamped_images, final_file_path)

    def defult_bind():  # Вызывается при нажатии на По Умолчанию
        pass

    def combo_bind(event):  # Вызывается при выборе строки из combobox
        pass

    def pages_data_to_insert_format(
            pages_data):  # переобразует pages_data в переменную удобную для записывания в combobox
        tmp = []
        for i, el in enumerate(pages_data):
            if el is None:
                pass
            else:
                a = el['cost']
                sum = '{}.{} Руб.'.format((int(a) - int(a) % 100) // 100, int(a) % 100)
                tmp.append('{},   {}'.format(el['name'], sum))
        return tmp

    def gui():  # создаёт окно
        global win, combo_var  # импорт глобальных переменных
        insert_pages_data = pages_data_to_insert_format(pages_data)  # получает insert_pages_data
        combo = Combobox(win, textvariable=combo_var, values=insert_pages_data, width=70)  # создаётся выпадающий список
        combo.grid(row=0, columnspan=5, pady=3)  # выпадающий список показывается на экране
        combo.bind('<<ComboboxSelected>>', combo_bind)  # к изменению строки в выпадающем списке привязывается функция
        # combo_bind
        ename, eperiod, eaddress, ebankid, ecost = Entry(width=40), Entry(width=40), Entry(width=40), Entry(width=40), \
                                                   Entry(width=40)  # создание полей ввода
        ename.grid(row=1, column=1)  # размещение поля ввода
        Label(text='ФИО').grid(row=1, column=0)  # создание и размешение натписи
        eperiod.grid(row=2, column=1)  # размещение поля ввода
        Label(text='Период').grid(row=2, column=0)  # создание и размешение натписи
        eaddress.grid(row=3, column=1)  # размещение поля ввода
        Label(text='Адресат').grid(row=3, column=0)  # создание и размешение натписи
        ecost.grid(row=4, column=1)  # размещение поля ввода
        Label(text='Сумма').grid(row=4, column=0)  # создание и размешение натписи
        bOK = Button(text='OK', command=ok_bind)  # создание кнопки ОК
        bOK.grid(row=5, column=4)  # размещение кнопки ОК
        bDefult = Button(text='По Умолчанию', command=defult_bind)  # создание кнопки По Умолчанию
        bDefult.grid(row=5, column=3)  # размещение кнопки По Умолчанию
        # для считывание текста из поля ввода нужно a = ename.get()
        win.mainloop()  # цикл окна

    gui()  # запуск интерфейса


if __name__ == '__main__':
    main('test.pdf')  # запуск программы
