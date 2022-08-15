
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image  
import requests
import pyEX as p

#API

token = "pk_4086bd94147b46e78abc8d392892e305"
auth  = p.Client(api_token=token, version='stable')

#create root window

root = Tk() 

root.geometry('300x300')

root.title("Intrensic Value Calculator")

root.config(bg="#ccccca")

#import img

# bg_img = Image.open("dollar-black-circle-icon-28.png")
# bg_img2 = bg_img.resize((50,50), Image.ANTIALIAS)
# bg_img_tk = ImageTk.PhotoImage(bg_img2)



#Create start frame with buttons for the other menus
frm_start = tk.Frame(root, width=400, height=500, bg='#ccccca')
frm_start.grid(row=0,column=0)

#Create frame, grid and widgets
frm = tk.Frame(root, width=400, height=500, bg="#ccccca",pady=50)

frm.grid(column=0,row=0,pady=5,padx=10)

#img_label = tk.Label(image=bg_img_tk).grid(row=1,column=0)

#Functie care face get request pentru datele de pe site 
def getTickerInfo():
    client = p.Client(api_token=token, version='stable') 
    ticker_symbol = ticker_name.get().lower()
    stock_info = client.quote(symbol=ticker_symbol)

    #get data from json dictionary 

    ticker_full_name.insert(0, stock_info['companyName'])
    ticker_price.insert(0, (str(stock_info['latestPrice'])+'$'))
    ticker_peratio.insert(0, stock_info['peRatio'])
    ticker_52weekH.insert(0, (str(stock_info['week52High'])+'$'))
    ticker_52weekL.insert(0, (str(stock_info['week52Low'])+'$'))

    if float(ticker_peratio.get()) > 20:
        ticker_peratio.config(bg ='red')
    else:
        ticker_peratio.config(bg='green')

    ticker_btn2.grid(row=8,column=2,padx=5,pady=5)

#Functie care sterge valorile din campurile alese

def DeleteValues():

    ticker_full_name.delete(0,END)
    ticker_price.delete(0,END)
    ticker_peratio.delete(0,END)
    ticker_52weekH.delete(0,END)
    ticker_52weekL.delete(0,END)
    

    ticker_peratio.config(bg= 'black')
    ticker_btn2.grid_forget()

def backToMenu():
    frm.grid_forget()
    frm_start.grid()
    
    
def SwitchStockInfo():
    frm_start.grid_forget()
    frm.grid()


#start page buttons
start_label = tk.Label(frm_start,bg="#ccccca",text="Welcome to my app :)",font="Roboto").grid(row=1,column=2,padx=75,pady=25)

basic_info = tk.Button(frm_start,bg="#ccccca",text="Stock Info",font="Roboto", command=SwitchStockInfo)
basic_info.grid(row=2,column=2,pady=5)

calculator = tk.Button(frm_start,bg="#ccccca",text="Calculator",font="Roboto", command=SwitchStockInfo)
calculator.grid(row=3,column=2,pady=5)

help_btn = tk.Button(frm_start,bg="#ccccca",text="Help",font="Roboto", command=SwitchStockInfo)
help_btn.grid(row=4,column=2,pady=5)



#Ticker Name Widget

ticker_name_label = tk.Label(frm,bg="#ccccca",text="Ticker",font="Roboto").grid(row=2,column=1,padx=5)

ticker_name = tk.Entry(frm)

ticker_name.grid(row=2,column=2)

#Ticker Full Name Widget

ticker_full_name_label = tk.Label(frm, bg='#ccccca', text='Company Name',font='Roboto',).grid(row=3,column=1,padx=5)

ticker_full_name = tk.Entry(frm,foreground='white',bg='black',justify=CENTER)

ticker_full_name.grid(row=3,column=2)

#Ticker Price Widget

ticker_price_label = tk.Label(frm,bg="#ccccca",text="Stock Price",font="Roboto").grid(row=4,column=1,padx=5)

ticker_price = tk.Entry(frm,foreground='white',bg='black',justify=CENTER)

ticker_price.grid(row=4,column=2)


#Ticker P/E Ratio

ticker_peratio_label = tk.Label(frm,bg="#ccccca",text="P/E Ratio",font="Roboto").grid(row=5,column=1,padx=5)

ticker_peratio = tk.Entry(frm,foreground='white',bg='black',justify=CENTER)

ticker_peratio.grid(row=5,column=2)

#Week 52 High

ticker_52weekH_label = tk.Label(frm,bg="#ccccca",text="52W High ",font="Roboto").grid(row=6,column=1,padx=5)

ticker_52weekH = tk.Entry(frm,foreground='white',bg='black',justify=CENTER)

ticker_52weekH.grid(row=6,column=2)

#Week 52 Low

ticker_52weekL_label = tk.Label(frm,bg="#ccccca",text="52W Low",font="Roboto").grid(row=7,column=1,padx=5)

ticker_52weekL = tk.Entry(frm,foreground='white',bg='black',justify=CENTER)

ticker_52weekL.grid(row=7,column=2)

#Command button to get info  

ticker_btn = tk.Button(frm,text="Get stock data",command=getTickerInfo) #calls the function 

ticker_btn.grid(row=8,column=1,padx=10,pady=5)

#Command button to delete info 

ticker_btn2 = tk.Button(frm, text='Delete values', command=DeleteValues)

#button to go back 

back_btn =tk.Button(frm,text='Back',command=backToMenu)
back_btn.grid(row=9,column=1,padx=5,pady=5)

frm.grid_forget()
root.mainloop() #makes eveything apper





