import collections
from functools import cmp_to_key
from tkinter import *

from Comparator import Comparator
from FileWorkClass import FileWorkClass

def main():
    window = Tk()
    window.title("Лаба 2")
    window.geometry('200x120')
    window.resizable(False, False)
    label1 = Label(text="Введи адрес входного файла",
                   width=190,
                   background="black",
                   foreground="#ccc")
    label1.pack()
    file1 = StringVar()
    editText1 = Entry(textvariable=file1,
                      width=190,
                      background="white",
                      foreground="#000")
    editText1.pack()
    label2 = Label(text="Введи адрес выходного файла",
                   width=190, background="black",
                   foreground="#ccc")
    label2.pack()
    file2 = StringVar()
    editText2 = Entry(textvariable=file2,
                      width=190,
                      background="white",
                      foreground="#000")
    editText2.pack()
    btn = Button(text="Начать",
                 background="#555",
                 foreground="#ccc",
                 padx="20", pady="8",
                 font="16",
                 width="190",
                 command=lambda : btnStartPars(file1.get(), file2.get()))
    btn.pack()
    window.mainloop()


def btnStartPars(file1, file2):
    dict = FileWorkClass.ReadFile(file1)
    d = sorted(dict.items(), key=cmp_to_key(Comparator.make_comparator(Comparator.cmpValue)), reverse = False)
    FileWorkClass.WriteFile(file2, d)



if __name__ == '__main__':
    main()
