import tkinter as tk
import requests
import tdapi as api

window = tk.Tk() # creates the main window interface
window.columnconfigure(2, minsize = 800, weight = 1) # number, size, and weight of columns in window
window.rowconfigure(0, minsize = 800, weight = 1) # number, size, and weight of rows in window

outputMain = tk.Text(window) # output window, which is a textbox

tD = tk.Frame(window) # first frame
eD = tk.Frame(window) # second frame

qInp = ["apikey", "ticker"]
gMInp = ["apikey", "index", "direction", "change"]
t = ["", "", "", "", "", "", "", "", ""]
out = ["", "", "", "", "", "", "", "", ""]
ent = ["", "", "", "", "", "", "", "", ""]

def qFill():
    if ent[1] != "":
        for i in range(4):
            ent[i].destroy()
            t[i].destroy()

    for i in range(2):
        t[i] = tk.Label(tD, text = qInp[i])
        t[i].grid(row = i, column = 0, sticky = "e", padx = 0, pady = 4)

        ent[i] = tk.Entry(eD)
        ent[i].grid(row = i, column = 0, sticky = "ew", padx = 2, pady = 5)
    
    depend = dArray[0]
    transit(depend)

def gMFill():
    if ent[1] != "":
        for i in range(2):
            ent[i].destroy()
            t[i].destroy()
    for i in range(4):
        t[i] = tk.Label(tD, text = gMInp[i])
        t[i].grid(row = i, column = 0, sticky = "e", padx = 0, pady = 4)

        ent[i] = tk.Entry(eD)
        ent[i].grid(row = i, column = 0, sticky = "ew", padx = 2, pady = 5)

    depend = dArray[1]
    transit(depend)

def bFill():
    for i in range(10):
            ent[i].destroy()
            t[i].destroy()

def transit(depend):
    bButton = tk.Button(eD, text = "Back", command = bFill)
    bButton.grid(row = 20, column = 0, sticky = "ew", padx = 2, pady = 5)

    sButton = tk.Button(eD, text = "Submit", command = depend)
    sButton.grid(row = 21, column = 0, sticky = "ew", padx = 2, pady = 5)

tD.grid(row = 0, column = 0, sticky = "ns")
eD.grid(row = 0, column = 1, sticky = "ns")

outputMain.grid(row = 0, column = 2, sticky = "nsew")

def qTransfer():
    for i in range(2):
        out[i] = ent[i].get()
    
    apikey = out[0]
    ticker = out[1]
    q = api.quote(ticker, apikey)

    if outputMain.get("1.0") == "":
        outputMain.insert(tk.END, q)
    else:
        outputMain.delete("1.0", tk.END)
        outputMain.insert(tk.END, q)

def gMTransfer():
    for i in range(4):
        out[i] = ent[i].get()
    
    apikey = out[0]
    index = out[1]
    direction = out[2]
    change = out[3]
    gM = api.getMovers(apikey, index, direction, change)
    print(gM)
    if outputMain.get("1.0") == "":
        outputMain.insert(tk.END, gM)
    else:
        outputMain.delete("1.0", tk.END)
        outputMain.insert(tk.END, gM)

dArray = [qTransfer, gMTransfer]

qButton = tk.Button(eD, text = "Quotes", command = qFill)
qButton.grid(row = 9, column = 0, sticky = "ew", padx = 2, pady = 5)

gMButton = tk.Button(eD, text = "Get Movers", command = gMFill)
gMButton.grid(row = 10, column = 0, sticky = "ew", padx = 2, pady = 5)

window.mainloop()