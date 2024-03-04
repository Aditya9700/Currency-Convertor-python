from tkinter import *
from tkinter import ttk

window=Tk()


from PIL import Image,ImageTk

import requests
import json

#Function to get the current currency rates from the API

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    '''if currency_1== None:
        pass'''
    currency_2 = combo2.get()
    '''if currency_2== None:
        pass'''
    
    amount = value.get()
    print("Trade_amount:",amount)

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'CAD':
        symbol = 'CA $'
    elif currency_2 == 'EUR':
        symbol ='€'
    elif currency_2 == 'JPY':
        symbol = '¥'
    elif currency_2 == 'GBP':
        symbol = '£'    
    elif currency_2 == 'AUD':
        symbol = '$'
    elif currency_2 == 'CHF':
        symbol = 'CHF'
    elif currency_2 == 'AED':
        symbol = 'AED'
    elif currency_2 == 'SAR':
        symbol ='SR'
    elif currency_2 == 'RUB':
        symbol = 'RUB'


    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result['text'] = formatted

    print("To_Currency:",converted_amount, formatted)

#Structure

window.geometry('300x320')
window.resizable(width=False,height=False)
window.title('CONVERTER')
window.configure(bg="white")

#FRAMES
top=Frame(window,width=300,height=60,bg="cyan")
top.grid(row=0,column=0)
main=Frame(window,width=300,height=260,bg="white")
main.grid(row=1,column=0)
#relief=SUNKEN

#Top frame
icon=Image.open('icon.png')
icon=icon.resize((40,40))
icon=ImageTk.PhotoImage(icon)
app_name=Label(top,image=icon,compound=LEFT,
text="Currency Converter",height=5,padx=13,pady=30,anchor=CENTER,
font=('Arial 16 bold'),bg='cyan',fg="black")
app_name.place(x=0,y=0)

#Main Frame
result=Label(main,text="",width=16,height=2,pady=7,relief="solid",anchor=CENTER,font="Ivy 15 bold",bg="white",fg="black")
result.place(x=50,y=10)


currency=['USD','CAD','BRL','INR','EUR','JPY','GBP','AUD','CHF','AED','SAR','RUB']

from_label=Label(main,text="From",width=8,height=1,pady=0,padx=0,relief="flat",
anchor=NW,font="Ivy 10 bold",bg="white",fg="black")
from_label.place(x=48,y=90)

#Dropdown boxes

combo1=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo1['values']=(currency)
combo1.place(x=50,y=115)

to_label=Label(main,text="To",width=8,height=1,pady=0,padx=0,relief="flat",
anchor=NW,font="Ivy 10 bold",bg="white",fg="black")
to_label.place(x=158,y=90)

combo2=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 12 bold"))
combo2['values']=(currency)
combo2.place(x=160,y=115)

value=Entry(main,width=22,justify=CENTER,font=("Ivy 12 bold"),relief=SOLID)
value.place(x=50,y=155)

#Convert Button
button =Button(main,text="CONVERT",width=19,padx=5,height=1,bg="red",fg="white",
font=("Ivy 12 bold"),command=convert)

button.place(x=50,y=210)
window.mainloop()




#SQL CONNECTIVEY
import mysql.connector as a 
con=a.connect(host="localhost",
user="root",
passwd="123456",
database="Project")
mycursor=con.cursor()

def previous():
    #print("To","FROM","Trade","Converted")
    print("\n")
    mycursor.execute("select * from convertor")
    x1=mycursor.fetchall()
    for row in x1:
        print(row)
    print("\n")
    main()

def convertor():
    print(currency)
    
    while True:
        c1=input("Enter From_Currency:")
        if c1 in currency:
            break
        else:
            print("Enter the correct Currency Name!!")

    while True:
        c2=input("Enter To_Currency:")
        if c2 in currency:
            break
        else:
            print("Enter the correct Currency Name!!")
    
    while True:
        try:
            c3 = int(input("Enter Trade_Amount: "))
        except ValueError:
            print("Please enter a valid integer")
            continue
        else:
            break

    while True:
        try:
            c4 = int(input("Enter Converted_Amount: "))
        except ValueError:
            print("Please enter a valid integer")
            continue
        else:
            break
    
    c5="Insert into convertor values(%s,%s,%s,%s)"
    t=(c1,c2,c3,c4)
    mycursor.execute(c5,t)
    con.commit()
    print("Query Sucessfully Executed!!!")
    main()


def main():
    t1="PLEASE SELECT YOUR QUERY IN SQL"
    print(t1.center(79,'*'))
    print('''1.To add records 
        2.To Display the Previous Records 
        3.To exit the program''')
    choice=input("Enter Task_no:")
    if(choice=="1"):
        convertor()
    elif(choice=="2"):
        previous()
    else:
        print("\n")
main()

#Date and time
q1="GOOD EVENING!!"
q2="GOOD MORNING!!"
import datetime

now=datetime.datetime.now()
if (now.strftime("%p")) == "AM":
     print(q2.center(79))
else:
     print(q1.center(79))
     
print("Current date and time is:")
print(now.strftime("%y-%m-%d %H:%M:%S\n"))

r1="Thanks for using Currency Convertor"
print(r1.center(79,"*"),"\n Made By- Aditya Rana")





