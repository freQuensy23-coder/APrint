from Classes_and_Func.PagesFunc import *
from tkinter import *
from tkinter.ttk import *

pages_texts, images, pages_data, insert_pages_data, my_pages_data = 0, 0, 0, 0, 0
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
    global file_path
    file_path = fp
    global win, combo_var

    def text_geter_in_entry(page):
        def geter():
            dic = {}
            global ename, eperiod, eaddress, ecost, my_pages_data
            # try:
            if 1:
                a = ecost.get()
                if a != '':
                    dic['cost'] = int(float(ecost.get().split()[0]) * 100)
                    dic['period'] = eperiod.get()
                    dic['name'] = ename.get()
                    dic['address'] = eaddress.get()
                    return dic
                else:
            # except IndexError:
                    return 0

        global my_pages_data
        tmp_page_data = []
        for i, el in enumerate(my_pages_data):
            if i != page:
                tmp_page_data.append(my_pages_data[i])
            elif i == page:
                if geter() != 0:
                    tmp_page_data.append(geter())
                elif geter() == 0:
                    tmp_page_data.append(my_pages_data[i])
        print(tmp_page_data)

    def text_inserter_to_entry(page):
        global pages_data

        def recorder(name, period, adres, cost):
            global ename, eperiod, eaddress, ecost
            ename.insert(0, name)
            eperiod.insert(0, period)
            eaddress.insert(0, adres)
            ecost.insert(0, cost)

        def cleaner():
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
        global images, pages_data, file_path
        stamped_images = stamp_pages(images, pages_data)
        final_file_path = get_pdf_file_path(file_path)
        save_images_to_pdf(stamped_images, final_file_path)

    def defult_bind():
        global my_pages_data
        my_pages_data = pages_data
        combo_bind(0)

    def combo_bind(event):
        global combo_var, pages_data
        print(combo_var.get())
        for i, el in enumerate(pages_data):
            try:
                a = combo_var.get()
                if el['name'] == a.split(',')[0]:
                    print('Выбранн элемент {}'.format(i))
                    text_geter_in_entry(i)
                    text_inserter_to_entry(i)
            except TypeError:
                pass

    def pages_data_to_insert_format(pages_data):
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
    main("test.pdf")
