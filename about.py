from tkinter import *


back="#90BAEE"

abouts=Tk()
abouts.maxsize(300,300)
abouts.minsize(300,300)
abouts.title("About Eye Stock")
abouts.config(bg=back)

Developername=Label(abouts,text="Developer: Yuvraj Singh Yadav",bg=back).pack()
softname=Label(abouts,text="Software: Eye Stock",bg=back).pack()
Version=Label(abouts,text="Version: 0.1 (Stable)",bg=back).pack()
Language=Label(abouts,text="Language: Python3",bg=back).pack()
Api=Label(abouts,text="Api Used: YahooFinance",bg=back).pack()
Apptype=Label(abouts,text="Application type: Finance",bg=back).pack()


try:
    logo2=PhotoImage(file="graphic//eyestocksmall.png")
    logo=PhotoImage(file="graphic//logo.png")
    labellogo=Label(abouts,image=logo,bg=back)
    labellogo.pack()
    labellogo2=Label(abouts,image=logo2,bg=back)
    labellogo2.pack()
except:pass

abouts.mainloop()