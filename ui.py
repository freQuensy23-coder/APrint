from tkinter import *
from tkinter import filedialog as fd
import subprocess
from UIpars import parser

args = parser.parse_args()

directory = str
cvar1, cvar2 = str, str
file_name = args.input_filename


def main():
    global directory, cvar1, cvar2, file_name

    def dir():
        global directory
        global file_name
        file_name = fd.askdirectory()
        directory.config(text=file_name)

    def cancel():
        exit('cancel')

    def generate():
        global cvar1, cvar2, file_name
        run = 'qrgen.exe'
        run += ' {}'.format(file_name)
        if cvar1.get():
            run += ' -m'
        if cvar2.get():
            run += ' -s'
        output = subprocess.check_output(run)
        print(run)
        exit()

    win = Tk()
    win.resizable(False, False)
    win.geometry('500x500')

    opendir = Frame(win)
    directory = Label(opendir, text=file_name, width=50, bg='white')
    directory.grid(row=0, column=0, padx=5)
    bopen = Button(opendir, text='Обзор..', command=dir)
    bopen.grid(row=0, column=1)
    opendir.grid(row=0, column=0)

    cvar1 = BooleanVar()
    cvar1.set(0)
    c1 = Checkbutton(text="Соеденить в PDF", variable=cvar1, onvalue=1, offvalue=0)
    c1.grid(row=1, sticky=W)

    cvar2 = BooleanVar()
    cvar2.set(0)
    c2 = Checkbutton(text="Сохранить QR", variable=cvar2, onvalue=1, offvalue=0)
    c2.grid(row=2, sticky=W)

    but = Frame(win)
    bt1 = Button(but, text='Отмена', command=cancel)
    bt1.grid(row=0, column=0, padx=50)

    bt2 = Button(but, text='Сгенерировать', command=generate)
    bt2.grid(column=1, row=0, padx=50)
    but.grid(row=3)

    win.mainloop()


if __name__ == '__main__':
    main()
