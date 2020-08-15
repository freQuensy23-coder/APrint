from Classes_and_Func.PagesFunc import *
from tkinter import *
from tkinter.ttk import *

pages_texts, images, pages_data = 0, 0, 0
win = Tk()
combo_var = StringVar()


def getting_data_from_pdf(file_path):
    global pages_data, pages_texts, images
    _, pages_texts = get_pages_texts_docs(file_path)

    images = get_pdf_images(file_path)

    pages_data = get_pages_data(pages_texts)


def main(file_path):
    def combo_bind(event):
        global combo_var
        print(combo_var.get())

    getting_data_from_pdf(file_path)
    global pages_data, pages_texts, images
    global win, combo_var

    win.geometry('500x500')
    # c.set()
    combo = Combobox(win, textvariable=combo_var)
    combo.grid()
    combo.bind('<<ComboboxSelected>>', combo_bind)

    win.mainloop()



if __name__ == '__main__':
    main("test.pdf")
