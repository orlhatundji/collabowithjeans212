import requests
import tkinter as tk
from functools import partial


AVAILABLE_CURRENCY = "USD=Dollar,EUR=Euro,XOF=West African CFA Franc,ZAR=South-frica-Rand,CHF=Swiss Franc\nNGHS=Ghanaian Cedi,GBP=British Pound,BTC=Bitcoin"




#global variable
tempVal = "Naira"

def Naira_to_dollar():
    def convert(amount):
        result_label.config(text="IT IS DOING NOTHING ACTUALLY")
        

    txtInput1 = tk.StringVar()
    var = tk.StringVar()

    top = tk.Toplevel()
    top.title("Naira To Dollar")
    top.configure(background='#09A3BA')
    top.grid_columnconfigure(2, weight=1)
    top.grid_rowconfigure(0, weight=1)

    # label and entry field FROM
    input_label_1 = tk.Label(top, text="AMOUNT IN NAIRA", background='#09A3BA', foreground="#FFFFFF")
    input_entry_1 = tk.Entry(top, textvariable=txtInput1)
    input_label_1.grid(row=1)
    input_entry_1.grid(row=1, column=1)

        
    # result label's for showing the result
    result_label = tk.Label(top, text="result", background='#09A3BA', foreground="#FFFFFF")
    result_label.grid(row=3, columnspan=4)

    # button click
    call_convert = partial(convert, txtInput1.get())
    result_button = tk.Button(top, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
    result_button.grid(row=2, columnspan=4)




        



