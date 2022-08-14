
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

root.title("Intrensic Value Calculator")

root.config(bg="#ccccca")

#import img

# bg_img = Image.open("dollar-black-circle-icon-28.png")
# bg_img2 = bg_img.resize((50,50), Image.ANTIALIAS)
# bg_img_tk = ImageTk.PhotoImage(bg_img2)


#Create frame, grid and widgets

frm = tk.Frame(root, width=400, height=500, bg="#ccccca")

frm.grid(column=0,row=0,pady=5,padx=10)

#img_label = tk.Label(image=bg_img_tk).grid(row=1,column=0)

 
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

    ticker_btn2.grid(row=8,column=2,padx=5,pady=5)

def DeleteValues():

    ticker_full_name.delete(0,END)
    ticker_price.delete(0,END)
    ticker_peratio.delete(0,END)
    ticker_52weekH.delete(0,END)
    ticker_52weekL.delete(0,END)
    
    ticker_btn2.grid_forget()
    

#Ticker Name Widget

ticker_name_label = tk.Label(frm,bg="#ccccca",text="Ticker",font="Roboto").grid(row=2,column=1,padx=5)

ticker_name = tk.Entry(frm)

ticker_name.grid(row=2,column=2)

#Ticker Full Name Widget

ticker_full_name_label = tk.Label(frm, bg='#ccccca', text='Company Name',font='Roboto',).grid(row=3,column=1,padx=5)

ticker_full_name = tk.Entry(frm,foreground='white',bg='black')

ticker_full_name.grid(row=3,column=2)

#Ticker Price Widget

ticker_price_label = tk.Label(frm,bg="#ccccca",text="Stock Price",font="Roboto").grid(row=4,column=1,padx=5)

ticker_price = tk.Entry(frm,foreground='white',bg='black')

ticker_price.grid(row=4,column=2)


#Ticker P/E Ratio

ticker_peratio_label = tk.Label(frm,bg="#ccccca",text="P/E Ratio",font="Roboto").grid(row=5,column=1,padx=5)

ticker_peratio = tk.Entry(frm,foreground='white',bg='black')

ticker_peratio.grid(row=5,column=2)

#Week 52 High

ticker_52weekH_label = tk.Label(frm,bg="#ccccca",text="52W High ",font="Roboto").grid(row=6,column=1,padx=5)

ticker_52weekH = tk.Entry(frm,foreground='white',bg='black')

ticker_52weekH.grid(row=6,column=2)

#Week 52 Low

ticker_52weekL_label = tk.Label(frm,bg="#ccccca",text="52W Low",font="Roboto").grid(row=7,column=1,padx=5)

ticker_52weekL = tk.Entry(frm,foreground='white',bg='black')

ticker_52weekL.grid(row=7,column=2)

#Command button to get info  

ticker_btn = tk.Button(frm,text="Get stock data",command=getTickerInfo) #calls the function 

ticker_btn.grid(row=8,column=1,padx=10,pady=5)

#Command button to delete info 

ticker_btn2 = tk.Button(frm, text='Delete values', command=DeleteValues)

# ticker_btn2.grid(row=8,column=2,padx=5,pady=5)

root.mainloop() #makes eveything apper




