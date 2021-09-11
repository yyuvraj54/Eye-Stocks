from os import nice
from modules import stock_processor, stocksprices
from tkinter import *   



fontstyle="bungee"  #default font
frameleft="white"
tablerow="#555555"
bottomcolumn3="#98DAEB"
bottomcolumn2="#F5F7A7"
bottomcolumn1="#FCA3C4"
niftyback="#64BFA3"
backcolor="white"
stocktitle="#525252"
recoback="#F5F7A7"
investback="#FFC3B0"
gainback="#9ADBE8"


# To get all stock avalable in txt doc ~
f=open("modules//Data//stocknames.txt","r")
stocklist=[]
stockrealname=[]
buydate=[]
a=0
for item in f:
    itemlst=item.split("\n")
    if a==0:
        stockrealname.append(itemlst[0])
        a+=1
    elif a==1:
        stocklist.append(itemlst[0])
        a=0 
f.close()

f=open("modules//Data//reminders.txt","r")
recostocklist=[]
recostockrealname=[]

ra=0
for ritem in f:
    ritemlst=ritem.split("\n")
    if ra==0:
        recostockrealname.append(ritemlst[0])
        ra+=1
    elif ra==1:
        recostocklist.append(ritemlst[0])
        ra=0 
f.close()




# MAIN GUI CODE
root=Tk()
root.config(bg=frameleft,border=0,bd=0)
root.title("Eye Stocks")
root.maxsize(900,600)
root.minsize(900,600)
try:
    img =Image("photo", file="graphic//eyestock_logo.png")
    root.tk.call('wm','iconphoto', root._w, img)
except:pass


# SCROLL BAR 



my_canvas=Canvas(root,bg=frameleft,highlightbackground=frameleft,highlightcolor=frameleft,bd=0)
my_canvas.pack(expand=1,fill=BOTH,side=LEFT)





def addstockpage():
    import os
    os.system('python3 -m Addstocker')
try:
    Nifty=Label(my_canvas,text="NIFTY 50: ....",font=(fontstyle,20),bg=niftyback)
except:
    fontstyle="Helvetica"
    Nifty=Label(my_canvas,text="NIFTY 50: ....",font=(fontstyle,20),bg=niftyback)


imag=PhotoImage(file="graphic//addbutsmall.png")
logophoto=Button(my_canvas,image=imag,bd=0,relief=FLAT,activebackground="white",borderwidth=0,highlightthickness=0,command=addstockpage)

main=Frame(my_canvas,border=0,bg=frameleft)
main.pack(expand=1,fill=BOTH)
Nifty.place(relx=0.6,rely=0.02)
logophoto.place(relx=0.86,rely=0.8)

framerecomen=Frame(my_canvas,bg=tablerow)
recolabel=Label(framerecomen,text="Reminder stocks",font=fontstyle,bg=tablerow,fg="white")
recolabelprice=Label(framerecomen,text="stocks price",font=fontstyle,bg=tablerow,fg="white")
recomendation=Listbox(framerecomen,width=15,bg=recoback,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
recomendationprice=Listbox(framerecomen,width=15,bg=recoback,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
recomendation.bindtags((recomendation, root, "all"))
recomendationprice.bindtags((recomendationprice, root, "all"))


recolabel.grid(row=0,column=0)
recolabelprice.grid(row=0,column=1)
recomendation.grid(row=1,column=0)
recomendationprice.grid(row=1,column=1)

framerecomen.place(relx=0.6,rely=0.1)

'''
imag=PhotoImage(file="graphic//eyestock_logo.png")
logophoto=Label(my_canvas,image=imag)
logophoto.pack(side=BOTTOM,anchor="se")
'''

my_canvas.create_window((0,0),window=main,anchor="nw")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







# TITLE IN FRAM
titlename=Label(main,text="REAL TIME STOCK DATA",font=(fontstyle,20),bg="#FFE284").pack(anchor="nw",pady=10)

#Error meassage in window if happen!
error=Label(my_canvas,text="Eye stock is working:(running>On Multithread)",fg="green")
error.place(relx=0.6,rely=0.48)

#This the frame of stocks



stockmain=Frame(main,bg=tablerow)  
                                                                                                                 
stockframe=Frame(stockmain,bg=bottomcolumn1)
rowtitle_name=Label(stockframe,bg=tablerow,fg="white",font=(fontstyle,13),text="Stockname\n",width=15)
rowtitle_price=Label(stockframe,bg=tablerow,fg="white",font=(fontstyle,13),text="Current Price\n",width=15)
prevlab=Label(stockframe,bg=tablerow,font=(fontstyle,13),fg="white",text="Pre ClosedPrice\n",width=15)
rowtitle_name.pack(side=LEFT)
prevlab.pack(side=LEFT)
rowtitle_price.pack(side=LEFT)


stockframe.pack()

value="Selected: OverAlL State"
def CurSelet(evt):
    global value
    #value=stockname.get(stockname.curselection())
    listofbox =evt.widget
    ind=listofbox.curselection()
    value=listofbox.get(ind[0])

    Selectedlab.config(text=f"Selected stock: {value}",bg=stocktitle,fg="white")
    cu=stockprice.get(ind)
    pr=prev.get(ind)

    


    
    if cu>pr:
        sta="Today up about: +"
        reval=f"{sta}{cu-pr:.2f}"
        
        profitloss1lab.config(fg="green",text=reval)
    elif cu<pr:
        sta="Today Down about: -"
        reval=f"{sta}{pr-cu:.2f}"
        profitloss1lab.config(text=reval,fg="red")
    else:
        profitloss1lab.config(text="Stock set to Balance",fg="grey")

    

    
    if value=="PORTFOLIO":
        wait.pack(pady=20)
        stockbest.delete(0,END)
        stockpricebest.delete(0,END)
        

        stockpricevalues=[]

        totalprice=0
        try:

            grossvalue.config(text="")
            for _ in allnames:
                bup=stock_processor.stockOpration().needed(_,"price")
                buq=stock_processor.stockOpration().needed(_,"qunt")
                lp=0
                runit=0
                inx = stockname.get(0, "end").index(_)
                ele=stockprice.get(inx)
                for ea in bup:
                    ea=float(ea)
                    if ele<ea:
                        lp=lp+((ele-ea)*int(buq[runit]))
                    elif ele>ea:
                        lp=lp+((ele-ea)*int(buq[runit]))
                    else:lp=lp+0
                    runit+=1

                stockbest.insert(END,_)
                if lp<0:
                    stockpricebest.insert(END,f"{lp:.2f}")
                    stockpricebest.itemconfig(END, {'fg':'red'})
                elif lp>0:
                    stockpricebest.insert(END,f"{lp:.2f}")
                    stockpricebest.itemconfig(END, {'fg':'green'})
                else:
                    stockpricebest.insert(END,f"{lp:.2f}")
                    stockpricebest.itemconfig(END, {'fg':'grey'})
                
            
                
                totalprice=totalprice+lp
            grossans=overalltotalprice+totalprice




            beststock.pack(padx=10,pady=15)
            wait.pack_forget()
            if overalltotalprice>grossans:
                grossvalue.config(text=f"Gross Down value: {grossans}",fg="red",bg="#95C4A4")
                profitloss1lab.config(text=f"OverAll Down :{totalprice}",fg="red")
            elif overalltotalprice<grossans:
                grossvalue.config(text=f"Gross Profit value: +{grossans}",fg="green",bg="#95C4A4")
                profitloss1lab.config(text=f"OverAll Profit : +{totalprice}",fg="green")
            else:
                grossvalue.config(text=f"Gross Down value: Balance",fg="grey",bg="#95C4A4")
                profitloss1lab.config(text=f"OverAll Down : Balance",fg="red")
        except(TypeError):
            grossvalue.config(text="Total Gross value: Loading... ",fg="white",bg="#F47694")

        


            


        

        datequntprice.pack_forget()
        infostock.place_forget()
        overallframe.place(relx=0.6,rely=0.68)




    else:
        wait.pack_forget()
        beststock.pack_forget()
        overallframe.place_forget()
        infostock.place(relx=0.6,rely=0.64)
        datequntprice.pack(anchor="nw",pady=20,padx=10)
        singledate.delete(0,END)
        singlebuy.delete(0,END)
        singlequantity.delete(0,END)
        d=stock_processor.stockOpration().needed(value,"date")
        p=stock_processor.stockOpration().needed(value,"price")
        q=stock_processor.stockOpration().needed(value,"qunt")
        
        totalinvested=0
        totalq=0
        bit=0
        gainamount=0
        try:
            for i in range(len(d)):
                pf=float(p[i-1])
                qf=int(q[i-1])
                totalinvested=totalinvested+float(p[i-1])
                totalq=totalq+int(q[i-1])
        
                singledate.insert(END,d[i-1])
                singlebuy.insert(END,p[i-1])
                
                
                    
                if cu=="":
                    singlequantity.insert(END,f"{q[i-1]}")
                else:
                    if cu>pf:
                        bit=(cu-pf)*qf
                        gainamount=gainamount+bit
                        singlequantity.insert(END,f"{q[i-1]} UP: {bit:.2f}")
                        singlequantity.itemconfig(i, {'fg':'green'})
                        
                    elif cu<pf:
                        bit=(pf-cu)*qf
                        gainamount=gainamount-bit
                        singlequantity.insert(END,f"{q[i-1]}  Down: {bit:.2f}")
                        singlequantity.itemconfig(i, {'fg':'red'})
                        
                    else:
                        bit="Balance"
                        gainamount=gainamount+0
                        singlequantity.insert(END,f"{q[i-1]}  {bit}")
                        singlequantity.itemconfig(i, {'fg':'grey'})
                
            totalqunt.config(text=f"Total Qty: {totalq}")
            amountinvested.config(text=f"Amount Invested({value}): {totalinvested}~",bg=investback,fg="black")

            if gainamount>totalinvested:
                gain.config(text=f"Portfolio Amount({value}): +{gainamount:.2f} ~",fg="green",bg=gainback)
            elif gainamount<totalinvested:
                gain.config(text=f"Portfolio Amount({value}): {gainamount:.2f} ~",fg="red",bg=gainback)
            else:
                gain.config(text=f"Portfolio Amount({value}): {gainamount:.2f}",fg="grey",bg=gainback)
        except(TypeError):
            error.config(text="Restart needed:Check Connection or try again(line-301)",bg="#F47694",fg="white")

        



stockframe2=Frame(stockmain,bg=tablerow)
stockname=Listbox(stockframe2 ,width=15,bg=bottomcolumn1,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
stockprice=Listbox(stockframe2,width=15,bg=bottomcolumn3,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
prev=Listbox(stockframe2,width=15,bg=bottomcolumn2,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)


stockname.bind('<<ListboxSelect>>',CurSelet)
stockprice.bindtags((stockprice, root, "all"))
prev.bindtags((prev, root, "all"))

stockname.pack(side=LEFT)
prev.pack(side=LEFT)
stockprice.pack(side=LEFT)

singleportfolio=Frame(my_canvas,bg=backcolor)
singleportfolio.place(relx=0.6,rely=0.55)
Selectedlab=Label(singleportfolio,text=value)
profitloss1lab=Label(singleportfolio,text="Profit/Loss (Today): ---")


Selectedlab.pack(anchor="nw")
profitloss1lab.pack(anchor="nw")

stockframe2.pack()
stockmain.pack()

datequntprice=Frame(main,bg=tablerow)

#>>>>>>
sd1=Label(datequntprice,text="All buy dates",font=fontstyle,bg=tablerow,fg="white")
sd2=Label(datequntprice,text="All buy prices",font=fontstyle,bg=tablerow,fg="white")
sd3=Label(datequntprice,text="All quantity ",font=fontstyle,bg=tablerow,fg="white")
singledate=Listbox(datequntprice,width=15,bg=bottomcolumn1,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
singlebuy=Listbox(datequntprice,width=15,bg=bottomcolumn2,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
singlequantity=Listbox(datequntprice,width=15,bg=bottomcolumn3,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
singledate.bindtags((singledate, root, "all"))
singlebuy.bindtags((singlebuy, root, "all"))
singlequantity.bindtags((singlequantity, root, "all"))




sd1.grid(row=0,column=0)
sd2.grid(row=0,column=1)
sd3.grid(row=0,column=2)

singledate.grid(row=1,column=0)
singlebuy.grid(row=1,column=1)
singlequantity.grid(row=1,column=2)



infostock=Frame(my_canvas,bg=backcolor)
amountinvested=Label(infostock)
amountinvested.pack(anchor="nw",pady=5)
gain=Label(infostock,fg="orange")
gain.pack(anchor="nw")

totalqunt=Label(infostock,fg="#7D55C7")
totalqunt.pack(anchor="nw")



overallframe=Frame(my_canvas)
grosslab=Label(overallframe,text="PortFolio",font=(fontstyle,25))
grosslab.pack(anchor="nw")

grossInvested=Label(overallframe,text="Gross Invested",bg="#C2DEAE")
grossInvested.pack(anchor="nw",pady=5)

grossvalue=Label(overallframe,text="Gross value Now",bg="#95C4A4")
grossvalue.pack(anchor="nw")






allnames=stock_processor.stockOpration().getNames()
overalltotalprice=0
for total in allnames:
    qut=stock_processor.stockOpration().needed(total,"qunt")
    run=0
    for price in stock_processor.stockOpration().needed(total,"price"):
        overalltotalprice=overalltotalprice+(float(price)*int(qut[run]))
        run+=1
grossInvested.config(text=f"Gross Invested In Trade: {overalltotalprice:.2f}")



wait=Label(main,text="More info loading...\nPlease wait till all current prices load ",font=fontstyle)
beststock=Frame(main,bg=tablerow)

bestlab=Label(beststock,text="stockname",font=fontstyle,bg=tablerow,fg="white")
bestpricelab=Label(beststock,text="Overall profit/loss price",font=fontstyle,bg=tablerow,fg="white")
stockbest=Listbox(beststock,width=21,bg=bottomcolumn1,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)
stockpricebest=Listbox(beststock,width=21,bg=bottomcolumn3,activestyle = 'dotbox',relief=FLAT,font = (fontstyle,15),border=0)


stockbest.bindtags((stockbest, root, "all"))
stockpricebest.bindtags((stockpricebest, root, "all"))

bestlab.grid(row=0,column=0)
bestpricelab.grid(row=0,column=1)
stockbest.grid(row=1,column=0)
stockpricebest.grid(row=1,column=1)

def aboutpage():
    import about
aboutbutton=Button(my_canvas,text="About",font=fontstyle,command=aboutpage)
aboutbutton.place(relx=0.7,rely=0.9)

# setting up page with stocks info in Multithread!!
pagesetter=stocksprices.stocks(stockname,error,stocklist,stockrealname,stockprice,buydate,prev,Nifty,recomendation,recostockrealname,recostocklist,recomendationprice)
pagesetter.run()










root.mainloop()
