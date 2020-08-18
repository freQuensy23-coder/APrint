from Classes_and_Func.PagesFunc import *
from tkinter import *
from tkinter.ttk import *

pages_texts, images, pages_data, insert_pages_data, my_pages_data = 0, 0, 0, 0, 0
user_num = None
file_path = 0
win = Tk()
combo_var = StringVar()
ename, eperiod, eaddress, ebankid, ecost = Entry(width=40), Entry(width=40), Entry(width=40), Entry(width=40), \
                                           Entry(width=40)


def getting_data_from_pdf(file_path):
    global pages_data, pages_texts, images
    _, pages_texts = get_pages_texts_docs(file_path)

    images = get_pdf_images(file_path)

    pages_data = get_pages_data(pages_texts)


def main(fp):
    global file_path, win, combo_var
    file_path = fp

    def text_geter_in_entry(page):
        """Change temp page data varible, after geting new data from entry"""
        def geter():
            """Get data from entry (input text)"""
            dic = {}
            global ename, eperiod, eaddress, ecost, my_pages_data
            a = ecost.get()
            if ecost.get() != '':
                dic['cost'] = int(float(ecost.get().split()[0]) * 100)
                dic['period'] = eperiod.get()
                dic['name'] = ename.get()
                dic['address'] = eaddress.get()
                return dic
            else:
                return 0

        global my_pages_data
        # Обнроляем масси временной информации о людях
        tmp_page_data = []
        for i, el in enumerate(my_pages_data):
            if i != page:
                tmp_page_data.append(my_pages_data[i])
            elif i == page:
                if geter() != 0:
                    tmp_page_data.append(geter())
                else:
                    tmp_page_data.append(my_pages_data[i])
        print(tmp_page_data)

    def text_inserter_to_entry(page):
        """Change entry text after person selected"""
        global pages_data

        def recorder(name, period, adres, cost):
            """iNSERT TEXT TO ENTRY"""
            global ename, eperiod, eaddress, ecost
            ename.insert(0, name)
            eperiod.insert(0, period)
            eaddress.insert(0, adres)
            ecost.insert(0, cost)

        def cleaner():
            """clean entrys old text"""
            global ename, eperiod, eaddress, ecost
            ename.delete(0, END)
            eperiod.delete(0, END)
            eaddress.delete(0, END)
            ecost.delete(0, END)

        pd = pages_data[page]
        name = pd['name']
        period = pd['period']
        adress = pd['address']
        a = pd['cost']
        cost = '{}.{} Руб.'.format((int(a) - int(a) % 100) // 100, int(a) % 100)
        cleaner()
        recorder(name, period, adress, cost)

    def ok_bind():
        """DO this after OK clicked
            -Get filename
            -Save file (PDF)
        """
        global images, pages_data, file_path
        stamped_images = stamp_pages(images, pages_data)
        final_file_path = get_pdf_file_path(file_path)
        save_images_to_pdf(stamped_images, final_file_path)

    def defult_bind():
        """Do this after default clicked
        Reset data to defaults"""
        global my_pages_data
        my_pages_data = pages_data
        combo_bind(0)

    def combo_bind(event):
        """Do this when person selecte"""
        global combo_var, pages_data, user_num
        print(combo_var.get())
        text_geter_in_entry(user_num)

        for i, el in enumerate(pages_data):
            try:
                a = combo_var.get()
                if el['name'] == combo_var.get().split(',')[0]:
                    print('Выбранн элемент {}'.format(i))
                    user_num = i
                    # text_inserter_to_entry(i)
            except TypeError:
                pass

    def pages_data_to_insert_format(pages_data):
        """переобразует pages_data в переменную удобную для записывания в combobox
                    <name>,   <rub>.<cop> Руб
        """
        tmp = []
        for i, el in enumerate(pages_data):
            if el is None:
                pass
            else:
                a = el['cost']
                sum = '{}.{} Руб.'.format((int(a) - int(a) % 100) // 100, int(a) % 100)
                tmp.append('{},   {}'.format(el['name'], sum))
        return tmp

    getting_data_from_pdf(file_path)
    global pages_data, pages_texts, images, insert_pages_data, my_pages_data
    my_pages_data = pages_data

    insert_pages_data = pages_data_to_insert_format(pages_data)

    combo = Combobox(win, textvariable=combo_var, values=insert_pages_data, width=70)
    combo.grid(row=0, columnspan=5, pady=3)
    combo.bind('<<ComboboxSelected>>', combo_bind)

    # GUI
    global ename, eperiod, eaddress, ecost
    ename.grid(row=1, column=1)
    Label(text='ФИО').grid(row=1, column=0)
    eperiod.grid(row=2, column=1)
    Label(text='Период').grid(row=2, column=0)
    eaddress.grid(row=3, column=1)
    Label(text='Адресат').grid(row=3, column=0)
    ecost.grid(row=4, column=1)
    Label(text='Сумма').grid(row=4, column=0)
    bOK = Button(text='OK', command=ok_bind)
    bOK.grid(row=5, column=4)
    bDefult = Button(text='По Умолчанию', command=defult_bind)
    bDefult.grid(row=5, column=3)
    win.mainloop()


if __name__ == '__main__':
    # main("test.pdf")
    print(main.__doc__)
