# Stock-Trading-App
System Requirement Specification (SRS) :
1. To run the project you must have python installed in your system (version 3 or
above)
2. To visualize the database you must have mysql workbench installed in your
system.







1. ER Diagram


![image](https://user-images.githubusercontent.com/83928126/183125482-95681cc2-66f1-4cd1-9557-78713920a477.png)



2. Schema Design
According to the project requirement we came out with a simple schema consisting of 6 tables

- Stock table
- Trader table
- Trades table
- Account table
- Login Table
- Portfolio Table

Trader table consists of all the relevant details consisting of the user who logs in to the system.
Stock table consists of all the details about companies Shares like no_of Available share
,Share price etc .
Login table consists of all the login which have been done

Trades Table consist of the transactions of type of . trade which user has done like buy,sell
no_of shares purchased etc.


3. Data Normalisation
The tables we made are all in 3NF which means that they are in 2NF , 1NF and also free from
transitive dependencies .
● Trader Table
Primary key is User_id
Using user_id we can determine the person.
And by solving the functional dependency relation we can find that the table is in 3NF




Stock Table

Primary key is StockId (which we are extracting from the google login object)
Using Stock we can determine the stock price,company name etc
And by solving the functional dependency relation we can find that the table is in 3NF.
![image](https://user-images.githubusercontent.com/83928126/183125403-788da454-2658-4b03-819c-579eaec6e8b6.png)

Trades Table
![image](https://user-images.githubusercontent.com/83928126/183125610-c3bf8a2c-24bf-4056-b70b-c8a4f3a9f936.png)


Primary key TradeID and takes references from Stock table and Traders Table

And by solving the functional dependency table we find out there are no transitive
dependencies in the table so it is in 3NF .
Similarly For Other Tables about which Can be learned by ER diagram which is attached in
this file .
Our project was made using simplification of the Trading Platform system and we made the
database in sync with the tkinter gui by connection the database so we didn’t required any
procedures and functions we did the whole of the project using simple mysql queries rather
than complex ones and made the simple gui which does the required Functionalities



Thank You
