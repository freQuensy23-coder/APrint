from Classes_and_Func.PagesFunc import *
from tkinter import *
from tkinter.ttk import *

pages_texts, images, pages_data, insert_pages_data = 0, 0, 0, 0
win = Tk()
combo_var = StringVar()


def getting_data_from_pdf(file_path):
    global pages_data, pages_texts, images
    _, pages_texts = get_pages_texts_docs(file_path)

    images = get_pdf_images(file_path)

    pages_data = get_pages_data(pages_texts)


def main(file_path):
    def combo_bind(event):
        global combo_var, insert_pages_data
        print(combo_var.get())
        for i, el in enumerate(insert_pages_data):
            if el == combo_var.get():
                print('Выбранн элемент {}'.format(i))

    def pages_data_to_insert_format(pages_data):
        tmp = []
        for i, el in enumerate(pages_data):
            if el is None:
                pass
            else:
                a = el['cost']
                sum = '{},{} Руб.'.format((int(a) - int(a) % 100) // 100, int(a) % 100)
                tmp.append('{},   {}'.format(el['name'], sum))
        return tmp

    getting_data_from_pdf(file_path)
    global pages_data, pages_texts, images, insert_pages_data
    global win, combo_var

    insert_pages_data = pages_data_to_insert_format(pages_data)
    win.geometry('500x500')
    combo_var.set(insert_pages_data[1])
    combo = Combobox(win, textvariable=combo_var, values=insert_pages_data, width=60)
    combo.grid(row=0, columnspan=5, pady=3)
    combo.bind('<<ComboboxSelected>>', combo_bind)
    win.mainloop()


if __name__ == '__main__':
    main("test.pdf")
