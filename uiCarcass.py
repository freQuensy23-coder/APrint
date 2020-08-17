from Classes_and_Func.PagesFunc import *
from tkinter import *
from tkinter.ttk import *

pages_texts, images, pages_data, insert_pages_data = 0, 0, 0, 0
win = Tk()
combo_var = StringVar


def getting_data_from_pdf(file_path):
    global pages_data, pages_texts, images
    _, pages_texts = get_pages_texts_docs(file_path)

    images = get_pdf_images(file_path)

    pages_data = get_pages_data(pages_texts)


def main(file_path):
    getting_data_from_pdf(file_path)
    global pages_data, pages_texts, images, insert_pages_data

    def ok_bind():
        global images, pages_data, file_path
        stamped_images = stamp_pages(images, pages_data)
        final_file_path = get_pdf_file_path(file_path)
        save_images_to_pdf(stamped_images, final_file_path)

    def defult_bind():
        pass

    def combo_bind(event):
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

    def gui():
        global win, combo_var
        insert_pages_data = pages_data_to_insert_format(pages_data)
        combo = Combobox(win, textvariable=combo_var, values=insert_pages_data, width=70)
        combo.grid(row=0, columnspan=5, pady=3)
        combo.bind('<<ComboboxSelected>>', combo_bind)
        ename, eperiod, eaddress, ebankid, ecost = Entry(width=40), Entry(width=40), Entry(width=40), Entry(width=40), \
                                                   Entry(width=40)
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

    gui()


if __name__ == '__main__':
    main('test.pdf')
