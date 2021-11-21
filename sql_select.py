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
#query for income statement
query =("SELECT l_id, l_date, l_type, l_loaner, l_intamount, l_intrest, l_amount, l_reference FROM liability "
        "WHERE l_date BETWEEN %s AND %s")

start_date=input("Enter Start Date: ")
end_date=input("Enter End Date: ")

cursor.execute(query, (start_date,end_date))
print("ID date     type lender initial intrest amount(f) reference")
for (l_id,l_date,l_type,l_loaner,l_intamount,l_intrest,l_amount,l_reference) in cursor:
  print("{} {} {} {} {} {} {} {}".format(l_id,l_date,l_type,l_loaner,l_intamount,l_intrest,l_amount,l_reference))
