class stockOpration:
    '''def __init__(self,stockname,buyprice,buydate,qut):
        self.stockname=stockname
        self.buyprice=buyprice
        self.buydate=buydate
        self.qut=qut
    '''
    def __init__(self):
        self.readed=[]
        f=open("modules//Data//stockinfo.txt","r")
        for x in f:
            sd=x.split("\n")
            self.readed.append(sd[0].split(","))
        f.close()


    def readdata(self):
        return self.readed


    
    
    
    def getNames(self):
        index=0
        dat=self.readed
        length=len(dat)
        returnlst=[]
        while(index<length):
            returnlst.append(dat[index][0])
            index+=4
        return returnlst
    
    
    def needed(self,stockname,need):
        p=0
        if need=="date":
            p=1
        elif need=="price":
            p=2
        elif need=="qunt":
            p=3
        else:
            p=0
        index=0
        dat=self.readed
        length=len(dat)
        returndata=["null"]
        while(index<length):
            if stockname==dat[index][0]:
                returndata=(dat[index+p])
                break
            index+=4
        return returndata
    
    
    def exist(self,stockname):
        r=stockOpration.needed(self,stockname,"null")
        if stockname==r[0]:
            return True
        else:
            return False
    
    
    def newentry(self,stockname,realstockname,buyprice,buydate,qut):
        stockname=stockname.upper()
        if stockOpration.exist(self,stockname):
            return False
        else:
            f=open("modules//Data//stockinfo.txt","a")
            f.write("\n")
            f.write(stockname)
            f.write("\n")
            f.write(str(buydate))
            f.write("\n")
            f.write(str(buyprice))
            f.write("\n")
            f.write(str(qut))
            f.close
            f2=open("modules//Data//stocknames.txt","a")
            f2.write("\n")
            f2.write(stockname)
            f2.write("\n")
            f2.write(realstockname)
            f2.close()
            return True

    def updatedata(self,stockname,newdate,newprice,newqunt):
        f=open("modules//Data//stockinfo.txt","r+")
        readdata=f.readlines()
        uploaded=[]
        for x in readdata:
            rr=x.split("\n")
            rd=rr[0]
            uploaded.append(rd)
        f.close()
    

        for y in range(len(uploaded)-1):
            if uploaded[y]==stockname:
                dateframe=uploaded[y+1]
                priceframe=uploaded[y+2]
                quntframe=uploaded[y+3]
                newd=dateframe.split(",")
                newp=priceframe.split(",")
                newq=quntframe.split(",")
                newd.append(newdate)
                newp.append(newprice)
                newq.append(newqunt)
                break

        for item in range(len(uploaded)-1):
            if uploaded[item]==stockname:
                uploaded[item+1]=",".join(newd)
                uploaded[item+2]=",".join(newp)
                uploaded[item+3]=",".join(newq)
                break
        

        strin="\n".join(uploaded)
        f=open("modules//Data//stockinfo.txt","w")
        f.writelines(strin)
        f.close()

    def deletedata(self,stockname):
        f=open("modules//Data//stockinfo.txt","r+")
        readdata=f.readlines()
        uploaded=[]
        for x in readdata:
            rr=x.split("\n")
            rd=rr[0]
            uploaded.append(rd)
        f.close()
        for each in range(len(uploaded)-1):
            if uploaded[each]==stockname:
                uploaded.pop(each)
                uploaded.pop(each)
                uploaded.pop(each)
                uploaded.pop(each)
                break
        strin="\n".join(uploaded)
        f=open("modules//Data//stockinfo.txt","w")
        f.writelines(strin)
        f.close()

        f2=open("modules//Data//stocknames.txt","r+")
        readit=f2.readlines()
        upload=[]
        for t in readit:
            rqr=t.split("\n")
            rdq=rqr[0]
            upload.append(rdq)
        f2.close()

        for h in range(len(upload)-1):
            
            if upload[h]==stockname:
                upload.pop(h)
                upload.pop(h)
                break
        st="\n".join(upload)
        f3=open("modules//Data//stocknames.txt","w")
        f3.writelines(st)
        f3.close()
if __name__ == "__main__":
    a=stockOpration()
    print(a.needed("RPOWER","qunt"))
