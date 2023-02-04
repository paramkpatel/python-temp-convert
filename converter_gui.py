"""
Author:  Param Patel

Language:  Python 3
To Run:  $ python3 converter_gui.py

Purpose: Made a temp converter by using Tkinter Library for the first time.

Bugs: 1) ValueError because of the "Entry" not clearing properly.

            If you find other bugs Let me Know! :-)
"""

import tkinter as tk

from converter import *


def main():
    # setup
    gui = tk.Tk()
    gui.title("Temperature Converter")
    gui.geometry("300x90")
    # string
    f_string = tk.StringVar()
    c_string = tk.StringVar()
    # text fields and input fields
    fahrenheit_entry = tk.Entry(gui, textvariable=f_string)
    celsius_entry = tk.Entry(gui, textvariable=c_string)
    fahrenheit_label = tk.Label(gui, text="Fahrenheit")
    celsius_label = tk.Label(gui, text="Celsius")
    # update inputs
    f_string.trace("w", lambda *args: on_fahrenheit_change(*args,
                                                           f_string=f_string,
                                                           c_string=c_string))
    c_string.trace("w", lambda *args: on_celsius_change(*args,
                                                        f_string=f_string,
                                                        c_string=c_string))
    # placements
    fahrenheit_label.place(x=50, y=10)
    fahrenheit_entry.place(x=120, y=10)
    celsius_label.place(x=50, y=50)
    celsius_entry.place(x=120, y=50)
    # run
    gui.mainloop()


def on_fahrenheit_change(*args, f_string, c_string):
    fahrenheit = f_string.get()
    if fahrenheit:
        celsius = f_to_c(float(fahrenheit))
        c_string.set("{:.2f}".format(celsius))
    return


def on_celsius_change(*args, f_string, c_string):
    celsius = c_string.get()
    if celsius:
        fahrenheit = c_to_f(float(celsius))
        f_string.set("{:.2f}".format(fahrenheit))
    return


if __name__ == '__main__':
    main()
