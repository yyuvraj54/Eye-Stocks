try:
    import yfinance as yf
except (ModuleNotFoundError):
    import os
    print("Trying to Install required module: yfinance\n")
    os.system('python -m pip install yfinance')
import yfinance as yf



import threading


class stocks:
    def __init__(self,stocklabel,errorlab,stockname,realname,stockprice,stockbuydate,prev,lab,reminder,r,rprice,rlist):
        self.stockname=stockname
        self.stocklabel=stocklabel
        self.errorlab=errorlab
        self.realname=realname
        self.stockprice=stockprice
        self.stockbuydate=stockbuydate
        self.prev=prev
        self.lab=lab
        self.reminder=reminder
        self.r=r
        self.rprice=rprice
        self.rlist=rlist
    

    def existStock(self,realstockname):
        stock = yf.Ticker(realstockname)
        price =  stock.info
        if len(price)<=50:
            return False
        else:
            return True 
        


        
    def setcurrentprice(self):

        for inde in range(len(self.stockname)):
            self.stocklabel.insert(inde,self.realname[inde])
        self.stocklabel.insert(inde+1,"PORTFOLIO")
        
    
        
        for index,stocknam in enumerate(self.stockname):
            try:
                
                
                stock = yf.Ticker(stocknam)
                price =  stock.info
                closval=price.get("previousClose")
                currval=price.get("currentPrice")
                self.stockprice.insert(index,currval)
                self.prev.insert(index,closval)


                
                
                
                if closval>currval:
                    self.stockprice.itemconfig(index, {'fg':'red'})
                elif closval<currval:
                    self.stockprice.itemconfig(index,{'fg':'green'})
                else:
                    self.stockprice.itemconfig(index,{'fg':'grey'})

            
            except:
                self.errorlab.config(text="Error Casuse: From Function:> currentprice",fg="red")
        self.stockprice.insert(index+1,"NULL")
        self.prev.insert(index+1,"NULL")
        self.errorlab.config(text="Eye stock is working:(running>Loop)",fg="green")

        

    def rpriceget(self):
        for index,stocknam in enumerate(self.rprice):
            try:
                stock = yf.Ticker(stocknam)
                price =  stock.info
                var="NULL"
                try:
                    var="Last: "+str(price.get("currentPrice"))
                except:
                    pass
                try:
                    var="Last: "+str(price.get("regularMarketPrice"))
                except:
                    pass 
                if stocknam=="^NSEI":
                    prev=price.get("previousClose")
                    val=price.get("regularMarketPrice")
                    self.lab.config(text=f"NIFTY 50: {var}")
                    if prev>val:
                        self.lab.config(fg='red')
                    elif prev<val:
                        self.lab.config(fg='green')
                    else:
                        self.lab.config(fg='grey')
                
                self.rlist.insert(index,var) 
            except:
                pass
        


    def niftyprice(self):        
        for ind,y in enumerate(self.r):
            self.reminder.insert(ind,'  '+y)
        
    def run(self):
        t1 = threading.Thread(target=self.setcurrentprice)
        t2 = threading.Thread(target=self.niftyprice)
        t3 = threading.Thread(target=self.rpriceget)
        t1.start()
        t2.start()
        t3.start()
        
        
    
