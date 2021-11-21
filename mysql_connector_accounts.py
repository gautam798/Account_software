from __future__ import print_function
import mysql.connector
from mysql.connector import (connection)


#config file
config = {
  'user': '',
  'password': '',
  'host': 'localhost',
  'database': 'test',
  'raise_on_warnings': True
}
#code for connecting sql databse with python for fetching and analysing it
mydb = mysql.connector.connect(**config) #auth details
cursor= mydb.cursor()  #just added variable to make code readable.
#actual program

# #add income record (is working perfect)
# add_income = ("INSERT INTO income "
#                "(i_date, i_type, i_reciever, i_sender, i_amount, i_reference) "
#                "VALUES (%s, %s, %s, %s, %s, %s);")
# data_income = ('2021-11-13','imps','gautam','ramesh',2000,'none')
# cursor.execute(add_income, data_income)

#add expense record (is working perfectly)
# add_expense = ("INSERT INTO expense "
#                "(e_date,e_type,e_exptype,e_reciever,e_sender,e_amount,e_reference) "
#                "VALUES (%s, %s, %s, %s, %s, %s, %s);")
# data_expense = ('2021-11-13', 'imps','essential','gaurav','gautam',2000,'none')
# cursor.execute(add_expense, data_expense)

#add asset record (is working perfectly)
# add_asset = ("INSERT INTO asset "
#                "(a_date,a_type,a_broker,a_taxes,a_status,a_amount,a_reference) "
#                "VALUES (%s, %s, %s, %s, %s, %s, %s);")
# data_asset = ('2021-11-13', 'stock', 'zerodha',12,'sold',2000,'none')
# cursor.execute(add_asset, data_asset)

#test data
# l_date ="2021-11-14"
# l_type ="personal"
# l_loaner ="mpocket"
# l_intamount= 3000
# l_intrest = 10
# l_amount= 3300
# l_reference = "none

l = [l_date,l_type,l_loaner,l_intamount,l_amount,l_intrest,l_reference]

#add liability record (is working perfectly)
add_liability = ("INSERT INTO liability "
               "(l_date, l_type, l_loaner, l_intamount, l_intrest, l_amount, l_reference) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s);")
data_liability = (liability[0],liability[1],liability[2],liability[3],liability[4],liability[5]liabilityl[6])
cursor.execute(add_liability, data_liability)


#ending
# Make sure data is committed to the database
mydb.commit()

cursor.close()
mydb.close()
