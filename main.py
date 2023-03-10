from ast import parse
import tkinter as tk
from tkinter import filedialog
import tkinter.font as font
import os
from pdf2docx import Converter


root = tk.Tk()
root.title("Pdf To Docx Converter")


def add_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select file")

    convert_file(file_path)


def convert_file(file_path):
    save_location = r"C:\Users\DELL\Desktop\ssb\Docxfile.docx"
    cv = Converter(file_path)
    cv.convert(save_location, start=0, end=None)
    cv.close()
    success_text = tk.Label(
        frame, text="Pdf has been successfully converted into docx", font=(16), bg="#422626", fg="white")
    success_text.pack()


canvas = tk.Canvas(root, height=500, width=700)
canvas.pack()

frame = tk.Frame(root, bg="black")
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)


button = tk.Button(frame, text="OPEN FILE ", padx=500,
                   pady=50, bg="yellow", fg="black", command=add_file)

button_font = font.Font(size=30)
button["font"] = button_font
button.pack()


root.mainloop()