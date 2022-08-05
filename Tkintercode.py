from tkinter import *
import mysql.connector
from tkinter import messagebox
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="shaileshA1@",
                               database="dbms_trading")
mycursor = mydb.cursor()



def firstpage():
    fstpg = Tk()
    def myLogin():
        fstpg.destroy()
        LoginPage()
    def mySignUp():
        fstpg.destroy()
        SignUpPage()
    mybutton1=Button(fstpg,text="Login",padx=20,pady=20,command=myLogin, fg="blue", bg="red")
    mybutton2=Button(fstpg,text="Sign Up",padx=20,pady=20,command=mySignUp, fg="blue", bg="red")

    mybutton1.grid(row=0,column=0,padx=10,pady=10);
    mybutton2.grid(row=1,column=0,padx=10,pady=10);
    fstpg.mainloop()



def SignUpPage():

    mysgnpg=Tk();
    def myFourthPage():
        mysgnpg.destroy()
        fourthPage()

    e1=Entry(mysgnpg,width=35,borderwidth=5)
    e1.grid(row=0,column=1, columnspan=3, padx=10, pady=10)
    e2=Entry(mysgnpg,width=35,borderwidth=5)
    e2.grid(row=1,column=1, columnspan=3, padx=10, pady=10)
    e3=Entry(mysgnpg,width=35,borderwidth=5)
    e3.grid(row=2,column=1, columnspan=3, padx=10, pady=10)
    e4=Entry(mysgnpg,width=35,borderwidth=5)
    e4.grid(row=3,column=1, columnspan=3, padx=10, pady=10)
    e5=Entry(mysgnpg,width=35,borderwidth=5)
    e5.grid(row=4,column=1, columnspan=3, padx=10, pady=10)
    e6=Entry(mysgnpg,width=35,borderwidth=5)
    e6.grid(row=5,column=1, columnspan=3, padx=10, pady=10)
    e7=Entry(mysgnpg,width=35,borderwidth=5)
    e7.grid(row=6,column=1, columnspan=3, padx=10, pady=10)

    myLabel1=Label(mysgnpg,text="Enter your First Name")
    myLabel2=Label(mysgnpg,text="Enter your Last Name")
    myLabel3=Label(mysgnpg,text="Enter your Phone Number")
    myLabel4=Label(mysgnpg,text="Enter your Email ID")
    myLabel5=Label(mysgnpg,text="Enter your Password")
    myLabel6=Label(mysgnpg,text="Enter your State")
    myLabel7=Label(mysgnpg,text="Enter your City") 
    myLabel1.grid(row=0,column=0);
    myLabel2.grid(row=1,column=0); 
    myLabel3.grid(row=2,column=0);
    myLabel4.grid(row=3,column=0); 
    myLabel5.grid(row=4,column=0);
    myLabel6.grid(row=5,column=0); 
    myLabel7.grid(row=6,column=0);
    

    def insertDetails():
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        a6=e6.get()
        a7=e7.get()

        mycursor.execute('''(select UserId from Trader where Trader.EmailID=%s and Trader.passwd=%s) ''',(a4,a5))
        sql_qry = mycursor.fetchone()

        if (sql_qry is None):
                mycursor.execute('''insert into Trader( FirstName, LastName, PhoneNo,EmailID,Passwd,City,State) values(%s,%s,%s,%s,%s,%s,%s)''',(a1,a2,a3,a4,a5,a6,a7))
                mydb.commit()
                mycursor.execute("select UserId from Trader where Trader.EmailID = %s",(a4,))
                p2 = mycursor.fetchone()  
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("MICROSOFT",))
                p1 = mycursor.fetchone()  
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"MICROSOFT",))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("RELIANCE",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"RELIANCE",))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("HDFC BANK",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"HDFC BANK",))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("INFOSYS",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"INFOSYS"))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("BAJAJ FINANCE",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"BAJAJ FINANCE"))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("Adani Green Ene",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"Adani Green Ene"))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("Tech Mahindra",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"Tech Mahindra"))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("TITAN",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"TITAN"))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("BAJAJ AUTO",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"BAJAJ AUTO"))
                mycursor.execute("select StockID from Stock where Stock.CompName = %s",("SIEMENS",))
                p1 = mycursor.fetchone()
                mycursor.execute('''insert into Portfolio(UserId,StockID,CompName) values(%s,%s,%s) ''',(p2[0],p1[0],"SIEMENS"))
                mydb.commit()
                myFourthPage()

        else:
            messagebox.showinfo("Error", "You Already have an Account, Please Log In")
            LoginPage();
        
    
        

    mybutton=Button(mysgnpg,text="Register",padx=50,pady=50,command=insertDetails, fg="blue", bg="red")
    mybutton.grid(row=7,column=1,padx=10,pady=10);



def LoginPage():

    lognpg = Tk()
    def myFourthPage():
        lognpg.destroy()
        fourthPage()



    e1=Entry(lognpg,width=35,borderwidth=5)
    e1.grid(row=0,column=1, columnspan=3, padx=10, pady=10)
    e2=Entry(lognpg,width=35,borderwidth=5)
    e2.grid(row=1,column=1, columnspan=3, padx=10, pady=10)
    myLabel1=Label(lognpg,text="Enter your Email")
    myLabel2=Label(lognpg,text="Enter your Password")

    def checkLogin():
        email = e1.get()
        password = e2.get()
        mycursor.execute('''(select UserId from Trader where Trader.EmailID=%s and Trader.passwd=%s) ''',(email,password))
        sql_qry = mycursor.fetchone()

        if (sql_qry is None):
                messagebox.showinfo("Error", "Invalid Credentials! \n Please Sign Up or check your password")
                lognpg.destroy()
                firstpage()

        else:
            lognpg.destroy()
            fourthPage()


    myLabel1.grid(row=0,column=0);
    myLabel2.grid(row=1,column=0); 
    mybutton=Button(lognpg,text="Next",padx=50,pady=50,command=checkLogin, fg="blue", bg="red")
    mybutton.grid(row=2,column=0,padx=10,pady=10);


def BuyPage(s1):
    bypg=Tk()

    myLabel1=Label(bypg ,text="Enter the number of shares you want to Buy  ")
    myLabel2=Label(bypg ,text="At what share price you want to buy each share?  ")
    myLabel1.grid(row=0,column=0);
    myLabel2.grid(row=1,column=0);

    e1=Entry(bypg,width=35,borderwidth=5)
    e1.grid(row=0,column=1, columnspan=3, padx=10, pady=10)
    e2=Entry(bypg,width=35,borderwidth=5)
    e2.grid(row=1,column=1, columnspan=3, padx=10, pady=10)

    

    def dothis():
        x=int(e1.get())
        mycursor.execute('''select (Stock.NO_OF_AVAIL_SHARES)  from Stock where Stock.CompName=%s ''', (s1))
        sql_query = mycursor.fetchone()
        finalShares = sql_query[0] - x
        # print(type(finalShares))
        mycursor.execute('''select (Stock.SharePrice) from Stock where Stock.CompName=%s ''', (s1))
        sql_query =  mycursor.fetchone()
        y=int(e2.get())
        parValue=  y-sql_query[0]
        if(finalShares>=0 and parValue >= 0):
            mycursor.execute("select StockID from Stock where Stock.CompName = %s",(s1))
            p1 = mycursor.fetchone()
            mycursor.execute('''UPDATE Stock SET NO_OF_AVAIL_SHARES = %s WHERE CompName=%s''', (finalShares,s1[0]))

            mycursor.execute('''UPDATE Portfolio SET MyShares = MyShares +  %s WHERE CompName=%s''', (x,s1[0]))
            # mycursor.execute('''insert into Trades( StockID, TradeType, NoOfShares, UserPrice, SharePrice, TimeStamp_, UserID) values(%s,%s,%s,%s,%s,%s,%s)''',(p1,a2,a3,a4,a5,a6,a7))
            mydb.commit()
            bypg.destroy()
            messagebox.showinfo("Congrats!", "Your Transaction is Complete")
        
        


    mybutton=Button(bypg,text="Finish",padx=50,pady=50,command=dothis, fg="blue", bg="red")
    mybutton.grid(row=2,column=0,padx=10,pady=10)



def SellPage(s1):

    sellpg=Tk()

    myLabel1=Label(sellpg ,text="Enter the number of shares you want to Sell")
    myLabel2=Label(sellpg,text="At what price you want to Sell each share?")

    myLabel1.grid(row=0,column=0);
    myLabel2.grid(row=1,column=0);

    e1=Entry(sellpg,width=35,borderwidth=5)
    e1.grid(row=0,column=1, columnspan=3, padx=10, pady=10)
    e2=Entry(sellpg,width=35,borderwidth=5)
    e2.grid(row=1,column=1, columnspan=3, padx=10, pady=10)


    def dothis():
        # x=int(e1.get())
        # mycursor.execute('''select (Stock.NO_OF_AVAIL_SHARES)  from Stock where Stock.CompName=%s ''', (s1))
        # sql_query = mycursor.fetchone()
        # finalShares = sql_query[0] - x

        # mycursor.execute("select StockID from Stock where Stock.CompName = %s",(s1))
        # p1 = mycursor.fetchone()
        x=e1.get()
        # mycursor.execute('''select (Portfolio.MyShares)  from Portfolio where Portfolio.UserId=%s ''', (s1))
        # sql_query =  mycursor.fetchone()
        y=int(e2.get())
        mycursor.execute('''select (Stock.SharePrice)  from Stock where Stock.CompName=%s ''', (s1))
        sql_query =  mycursor.fetchone()
        y=int(e2.get())
        value= sql_query[0] - y 

        if(value >= 0):
            mycursor.execute("select StockID from Stock where Stock.CompName = %s",(s1))
            p1 = mycursor.fetchone()

            mycursor.execute('''UPDATE Stock SET NO_OF_AVAIL_SHARES = NO_OF_AVAIL_SHARES + %s WHERE CompName=%s''', (x,s1[0]))
            mycursor.execute('''UPDATE Portfolio SET MyShares = MyShares- %s WHERE CompName=%s''', (x,s1[0]))

            # mycursor.execute('''insert into Trades( StockID, TradeType, NoOfShares, UserPrice, SharePrice, TimeStamp_, UserID) values(%s,%s,%s,%s,%s,%s,%s)''',(p1,a2,a3,a4,a5,a6,a7))
            mydb.commit()
            messagebox.showinfo("Congrats!", "Your Transaction is Completed")
            sellpg.destroy()


    mybutton=Button(sellpg,text="Finish",padx=50,pady=50,command=dothis, fg="blue", bg="red")
    mybutton.grid(row=2,column=0,padx=10,pady=10)




def fourthPage():
    fourpg=Tk()

    def mySell(s1):
        fourpg.destroy()
        SellPage(s1);
        return 

    def myBuy(s1):
        fourpg.destroy()
        BuyPage(s1);
        return


    myLabel1=Label(fourpg ,text="MICROSOFT")
    myLabel2=Label(fourpg ,text="RELIANCE")
    myLabel3=Label(fourpg ,text="HDFC BANK")
    myLabel4=Label(fourpg ,text="INFOSYS")
    myLabel5=Label(fourpg ,text="BAJAJ FINANCE")
    myLabel6=Label(fourpg ,text="Adani Green Ene")
    myLabel7=Label(fourpg ,text="Tech Mahindra")
    myLabel8=Label(fourpg ,text="TITAN")
    myLabel9=Label(fourpg ,text="BAJAJ AUTO")
    myLabel10=Label(fourpg ,text="SIEMENS")

    myLabel1.grid(row=0,column=0);
    myLabel2.grid(row=1,column=0); 
    myLabel3.grid(row=2,column=0);
    myLabel4.grid(row=3,column=0); 
    myLabel5.grid(row=4,column=0);
    myLabel6.grid(row=5,column=0); 
    myLabel7.grid(row=6,column=0);
    myLabel8.grid(row=7,column=0); 
    myLabel9.grid(row=8,column=0);
    myLabel10.grid(row=9,column=0); 


    mybutton1=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("MICROSOFT",)), fg="blue", bg="red")
    mybutton2=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("MICROSOFT",)), fg="blue", bg="red")

    mybutton3=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("RELIANCE",)), fg="blue", bg="red")
    mybutton4=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("RELIANCE",)), fg="blue", bg="red")

    mybutton5=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("HDFC BANK",)), fg="blue", bg="red")
    mybutton6=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("HDFC BANK",)), fg="blue", bg="red")

    mybutton7=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("INFOSYS",)), fg="blue", bg="red")
    mybutton8=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("INFOSYS",)), fg="blue", bg="red")

    mybutton9=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("BAJAJ FINANCE",)), fg="blue", bg="red")
    mybutton10=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("BAJAJ FINANCE",)), fg="blue", bg="red")

    mybutton11=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("Adani Green Ene",)), fg="blue", bg="red")
    mybutton12=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("Adani Green Ene",)), fg="blue", bg="red")

    mybutton13=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("Tech Mahindra",)), fg="blue", bg="red")
    mybutton14=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("Tech Mahindra",)), fg="blue", bg="red")

    mybutton15=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("TITAN",)), fg="blue", bg="red")
    mybutton16=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("TITAN",)), fg="blue", bg="red")

    mybutton17=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("BAJAJ AUTO",)), fg="blue", bg="red")
    mybutton18=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("BAJAJ AUTO",)), fg="blue", bg="red")

    mybutton19=Button(fourpg,text="Buy",padx=15,pady=15,command=lambda: myBuy(("SIEMENS",)), fg="blue", bg="red")
    mybutton20=Button(fourpg,text="Sell",padx=15,pady=15,command=lambda: mySell(("SIEMENS",)), fg="blue", bg="red")



    mybutton1.grid(row=0,column=1,padx=10,pady=10);
    mybutton2.grid(row=0,column=2,padx=10,pady=10);
    mybutton3.grid(row=1,column=1,padx=10,pady=10);
    mybutton4.grid(row=1,column=2,padx=10,pady=10);
    mybutton5.grid(row=2,column=1,padx=10,pady=10);
    mybutton6.grid(row=2,column=2,padx=10,pady=10);
    mybutton7.grid(row=3,column=1,padx=10,pady=10);
    mybutton8.grid(row=3,column=2,padx=10,pady=10);
    mybutton9.grid(row=4,column=1,padx=10,pady=10);
    mybutton10.grid(row=4,column=2,padx=10,pady=10);
    mybutton11.grid(row=5,column=1,padx=10,pady=10);
    mybutton12.grid(row=5,column=2,padx=10,pady=10);
    mybutton13.grid(row=6,column=1,padx=10,pady=10);
    mybutton14.grid(row=6,column=2,padx=10,pady=10);
    mybutton15.grid(row=7,column=1,padx=10,pady=10);
    mybutton16.grid(row=7,column=2,padx=10,pady=10);
    mybutton17.grid(row=8,column=1,padx=10,pady=10);
    mybutton18.grid(row=8,column=2,padx=10,pady=10);
    mybutton19.grid(row=9,column=1,padx=10,pady=10);
    mybutton20.grid(row=9,column=2,padx=10,pady=10);



firstpage()
