from os import name
from tkinter import * 
from modules import stock_processor
from modules import stocksprices
import time



# Default font 
fontstyle="bungee"



page=Tk()
page.title("Eye Stock Pager")
page.maxsize(700,500)
page.minsize(700,500)
try:
    img =Image("photo", file="graphic//pagelogo.png")
    page.tk.call('wm','iconphoto', page._w, img)
except:pass








#Stock LIST AREA 
framlist=Frame(page,bg="#525253")
framlist.pack(side=LEFT,fill=BOTH)

storename=stock_processor.stockOpration().getNames()

try:
    titleoflist=Label(framlist,text="Your stocks",font=(fontstyle,20),bg="#525253",fg="#ea816a")
    titleoflist.pack(anchor="nw",padx=10,pady=10)
except:
    fontstyle="Helvetica"
    titleoflist=Label(framlist,text="Your stocks",font=(fontstyle,20),bg="#525253",fg="#ea816a").pack(anchor="nw",padx=10,pady=10)
    titleoflist.pack(anchor="nw",padx=10,pady=10)

stockname=Listbox(framlist ,width=15,height=21,bg="#525253",selectbackground="#00BFFF",fg="#f6f5f0",exportselection=False,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)


def addstock():
    errorlab.config(text="",fg="red")    
    name=(lavval.get()).upper()
    symbol=(symbolval.get()).upper()
    buy=buyval.get()
    date=dateval.get()
    qunt=quntval.get()


    if qunt=="":errorlab.config(text="quantity not provided")
    if date=="":errorlab.config(text="date not provided")
    if buy=="":errorlab.config(text="buyprice not provided")
    elif buy.isdigit==False:errorlab.config(text=f"Enter a valid price: ({buy} is not accepted)")
    if symbol=="":errorlab.config(text="symbol not provided")
    if name=="":errorlab.config(text="stockname not provided")
    
    
    

    if errorlab["text"]=="":
        
        
        if stocksprices.stocks("","","","","","","").existStock(symbol):
            errorlab.config(text="Done",fg="green")
            stockname.insert(END,name)
            stock_processor.stockOpration().newentry(name,symbol,buy,date,qunt)   #stockname,realstockname,buyprice,buydate,qut):
        else:
            errorlab.config(text=f"No stock with name {symbol}",fg="red")

def deletestock():
    useingstock.config(text="SELECTED: NONE")
    val = stockname.get(0,END).index(value)
    stockname.delete(val)
    stock_processor.stockOpration().deletedata(value)
    

def updaterecord():
    
    

    errorlabfornew.config(text="",fg="red")


    if newbuyy.get()=="": errorlabfornew.config(text="New buy price not provided!")
    
    if newdatee.get()=="": errorlabfornew.config(text="New date not provided!")
    elif len(newdatee.get())>10: errorlabfornew.config(text="Please Provide a valid date! it should like 09/03/2002")
    elif len(newdatee.get())<10: errorlabfornew.config(text="Please Provide a valid date! it should like 09/03/2002")
    
    if newquntt.get()=="": errorlabfornew.config(text="New quantity not provided!")
    
    if errorlabfornew["text"]=="":
        stock_processor.stockOpration().updatedata(value,newdatee.get(),newbuyy.get(),newquntt.get())#updatedata(self,stockname,newdate,newprice,newqunt):
        errorlabfornew.config(text="Done",fg="green")
        newentrybuy.delete(0, END)
        newentrydate.delete(0, END)
        newentryqunt.delete(0, END)
value=""
def CurSelet(evt):
    global value
    #value=stockname.get(stockname.curselection())
    listofbox =evt.widget
    ind=listofbox.curselection()
    value=listofbox.get(ind[0])
    
    useingstock.config(text=f"SELECTED: {value}")
    framofimg.destroy()
    # FRAMES FOR SRTOCKS ADDING OR UPDATING>>>>>>>>>>>>>>>>>>>>>

    if useingstock["text"]=="SELECTED: ADD NEW STOCK":
        updatefram.pack_forget()
        guid.config(text="It may take 5-10 second to check stock is avalabel or not! please click button one\ntime only!",fg="green")
        newfram.pack(fill=BOTH,expand=1)
        deletebuttons.pack_forget()
    else:
        

        deletebuttons.config(text=f"REMOVE {value}")
        deletebuttons.pack(side="top")
        newfram.pack_forget()
        guid.config(text="Enter your updated data!")
        updatefram.pack(fill=BOTH,expand=1)
        


stockname.bind('<<ListboxSelect>>',CurSelet)

stockname.insert(END,"ADD NEW STOCK")
for item in storename:
    stockname.insert(END,item)
stockname.pack(padx=10,pady=10,anchor="nw")
sameback="#ffffff"
#STOCK UPDATE AREA
frameinput=Frame(page,bg=sameback)
frameinput.pack(side=LEFT,expand=1,fill=BOTH)

frameofupdate=Frame(frameinput,bg="#282829")
frameofupdate.pack(fill=BOTH)

useingstock=Label(frameofupdate,text="NO STOCK SELECTED",font=(fontstyle,20),bg="#282829",fg="white")
useingstock.pack(anchor="nw",padx=10,pady=12)


newfram=Frame(frameinput,bg=sameback)
# ADDNEW DATA ------------------------------>>>>>>>>
    
newstockentry=Label(newfram,text="New Detalis",bg=sameback,fg="black",font=(fontstyle,30),anchor="nw")
newstockentry.pack(pady=10)
framentry=Frame(newfram,bg=sameback)
namelab=Label(framentry,text="Stockname:",font=(fontstyle,20))
symbol=Label(framentry,text="Stock Symbol:",font=(fontstyle,20))
buyprice=Label(framentry,text="Buy Price:",font=(fontstyle,20))
buydate=Label(framentry,text="Date(DD/MM/YYYY):",font=(fontstyle,20))
buyqunt=Label(framentry,text="Buy Quantity:",font=(fontstyle,20))
    

lavval=StringVar()
symbolval=StringVar()
buyval=StringVar()
dateval=StringVar()
quntval=StringVar()
entrylab=Entry(framentry,textvariable=lavval,bg="#778899",fg=sameback)
entrysymbol=Entry(framentry,textvariable=symbolval,bg="#778899",fg=sameback)
entrybuy=Entry(framentry,textvariable=buyval,bg="#778899",fg=sameback)
entrydate=Entry(framentry,textvariable=dateval,bg="#778899",fg=sameback)
entryqunt=Entry(framentry,textvariable=quntval,bg="#778899",fg=sameback)
namelab.grid(row=0,column=0,pady=10,padx=10)
symbol.grid(row=1,column=0,pady=10,padx=10)
buyprice.grid(row=2,column=0,pady=10,padx=10)
buydate.grid(row=3,column=0,pady=10,padx=10)
buyqunt.grid(row=4,column=0,pady=10,padx=10)

entrylab.grid(row=0,column=1)
entrysymbol.grid(row=1,column=1)
entrybuy.grid(row=2,column=1)
entrydate.grid(row=3,column=1)
entryqunt.grid(row=4,column=1)

errorlab=Label(newfram,bg=sameback)
errorlab.pack()
addbuton=Button(newfram,text="ADD STOCK",font=(fontstyle,20),bd=0,command=addstock,highlightbackground="#6495ED")


framentry.pack(expand=1,fill=BOTH)
addbuton.pack()
#------------------------------------------------>>>>>>>>>  



updatefram=Frame(frameinput,bg=sameback)


# UPDATINGSTARTS------------------------------->>>>>>>>>>>>>>>>
updatestockentry=Label(updatefram,text="UPDATE RECORDS",font=(fontstyle,30),fg="black",bg=sameback,anchor="nw")
updatestockentry.pack(pady=10)
framupdate=Frame(updatefram,bg=sameback)
errorlabfornew=Label(updatefram,fg="red",bg=sameback)
newbuyprice=Label(framupdate,text="Buy Price:",font=(fontstyle,20))
newbuydate=Label(framupdate,text="Date(DD/MM/YYYY):",font=(fontstyle,20))
newbuyqunt=Label(framupdate,text="Buy Quantity:",font=(fontstyle,20))

newbuyy=StringVar()
newdatee=StringVar()
newquntt=StringVar()
newentrybuy=Entry(framupdate,textvariable=newbuyy,bg="#778899",fg=sameback)
newentrydate=Entry(framupdate,textvariable=newdatee,bg="#778899",fg=sameback)
newentryqunt=Entry(framupdate,textvariable=newquntt,bg="#778899",fg=sameback)



newbuyprice.grid(row=0,column=0,pady=10,padx=10)
newbuydate.grid(row=1,column=0,pady=10,padx=10)
newbuyqunt.grid(row=2,column=0,pady=10,padx=10)


newentrybuy.grid(row=0,column=1)
newentrydate.grid(row=1,column=1)
newentryqunt.grid(row=2,column=1)




updatebutton=Button(updatefram,text="UPDATE DATA",font=(fontstyle,20),bd=0,command=updaterecord,relief=RAISED,highlightbackground="#6495ED")
framupdate.pack(expand=1,fill=BOTH)
updatebutton.pack(side=BOTTOM)
errorlabfornew.pack(side=BOTTOM,pady=10)
#--------------------------------------->>>>>>>>>>>>>>>>



#>>>>>>DON'T LOOK
img=PhotoImage(file="graphic//pagelogo.png")
framofimg=Frame(frameinput,bg="white")
imagelabel=Label(framofimg,image=img,bd=0,relief=FLAT).pack()
imglbel=Label(framofimg,text="Eye Stock").pack()
framofimg.pack(pady=90)
#>>>>>>>>

meassageframe=Frame(frameinput)
meassageframe.pack(side="bottom",fill=X)
deletebuttons=Button(framlist,text="Remove Stock",relief=RAISED,highlightbackground="#CD5C5C",command=deletestock)
guid=Label(meassageframe, text="Please Select a stock from stocklist to make update or else Add a new stock",height=0,font=("ArialRoundedMT...",12),relief=FLAT,fg="black")
guid.pack(anchor="nw",padx=5,pady=12)




    

page.mainloop()