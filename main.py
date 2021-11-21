from __future__ import print_function
import mysql.connector
from mysql.connector import (connection)
import hashlib
#Note

#welcome msg
print("**********************Welcome to Private's network:**********************")
print("You are currently in Accounts section:")
print("#Note:-production Server:ACCOUNTS ")
print("Basic Authentication:")
#User Details
version = "V2.1"
user_name="Anonymous"
access_key=""
hash_value = "81dc9bdb52d04dc20036dbd8313ed055";
config = {
  'user': '',
  'password': '',
  'host': 'localhost',
#  'database': 'test',
  'database': 'accounts',
  'raise_on_warnings': True
}


#sql databse configuration
#code for connecting sql databse with python for fetching and analysing it
mydb = mysql.connector.connect(**config) #auth details
cursor= mydb.cursor()  #just added variable to make code readable.

#authintication(variable passchk)
def auth():
    global passwd
    passchk1 =(input("Please Enter your password:"))
    passchk2 =(hashlib.md5(passchk1.encode()))
    passwd =str(passchk2.hexdigest())
#password for Authentication(md5)
#md5 authentication is enabled
auth()
while passwd != hash_value:
    print("Wrong password : Try Again")
    auth()
print("--------------------------------------------------------------------------")
print("****************Hey gautam ! You are logged in sucessfully****************")
print("--------------------------------------------------------------------------")

#heart of program
def heart():
    print("Select Any Option(1/2):")
    print("1:For adding another entry")
    print("2:Show other option")
    global check
    check = int(input("Enter Any option Number:"))
heart()
#Updating records code start from here
while check == 1:
    print("------------------------------------------------------------------")
    print("*************Update statement section*****************************")
    print("------------------------------------------------------------------")
    print("Select From the below statement")
    print("1:Update income statement")
    print("2:Update expense statement")
    print("3:Update asset statement")
    print("4:update liability statement")
    option = int(input("Enter any one option(1/2/3/4): "))
    if option ==1:
        #income statement function
        def income():
            print("**************Your are currently updating income record**************")
            print("Enter the following details for income statement:")
            i_date=input("Date: ")
            i_type=input("Transaction Type(upi/neft/imps/cash): ")
            i_reciever=input("Reciever(To participant): ")
            i_sender=input("Sender(on account of): ")
            i_amount=input("Ammount: RS ")
            i_reference=input("Reference Details: ")
            global income
            income = [i_date,i_type,i_reciever,i_sender,i_amount,i_reference]
        income()
        #add income record (is working perfect)
        add_income = ("INSERT INTO income "
                       "(i_date, i_type, i_reciever, i_sender, i_amount, i_reference) "
                       "VALUES (%s, %s, %s, %s, %s, %s);")
        data_income = (income[0],income[1],income[2],income[3],income[4],income[5])
        cursor.execute(add_income, data_income)

        print("------------------------------------------------------")
        print("****(Data updated sucessfully inside income table*****")
        print("------------------------------------------------------")
        print (data_income)
    elif option ==2:
        #expense statement function
        def expense():
            print("**************Your are currently updating expense record**************")
            print("Enter the following details for expense statement: ")
            e_date=input("Date(YYYY-MM-DD): ")
            e_type=input("Transaction Type: ")
            e_exptype=input("Expense Type:(party/essential/urgent/debt/others/assets): ")
            e_reciever=input("reciever(To participant): ")
            e_sender=input("Sender(on account of): ")
            e_amount=input("Ammount: ")
            e_reference=input("reference Details: ")
            global expense
            expense = [e_date,e_type,e_exptype,e_reciever,e_sender,e_amount,e_reference]
        expense()
        add_expense = ("INSERT INTO expense "
                       "(e_date,e_type,e_exptype,e_reciever,e_sender,e_amount,e_reference) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s);")
        data_expense = (expense[0],expense[1],expense[2],expense[3],expense[4],expense[5],expense[6])
        cursor.execute(add_expense, data_expense)

        print("********************Data updated sucessfully inside expense table***************")
        print(data_expense)
    elif option ==3:
        def asset():
            print("**************Your are currently updating assets record**************")
            print("Enter the following details for asset statement:")
            a_date=input("Date of purchase(YYYY-MM-DD): ")
            a_type=input("Type(gold/stock/mf/etc): ")
            a_broker=input("Broker: ")
            a_taxes=input("Taxes paid: ")
            a_status=input("Status(holding/sold): ")
            a_amount=input("Ammount: ")
            a_reference=input("reference Details: ")
            global asset
            asset = [a_date,a_type,a_broker,a_taxes,a_status,a_amount,a_reference]
        #asset statement function
        asset()
        add_asset = ("INSERT INTO asset "
                      "(a_date,a_type,a_broker,a_taxes,a_status,a_amount,a_reference) "
                      "VALUES (%s, %s, %s, %s, %s, %s, %s);")
        data_asset = (asset[0],asset[1],asset[2],asset[3],asset[4],asset[5],asset[6])
        cursor.execute(add_asset, data_asset)

        print("*********Data updated sucessfully inside asset table*****************")
        print(data_asset)
        #sql query
    elif option ==4:
        #liability statement function
        def liability():
            print("**************Your are currently updating liability record**************")
            print("Enter the following details for liabiliy statement:")
            l_date=input("Date of Execution(YYYY-MM-DD): ")
            l_type=input("Type of loan: ")
            l_loaner=input("Loan provider Name: ")
            l_intamount=input("Principle Ammount: ")
            l_intrest=input("Intrest to be  paid: ")
            l_amount= input("Final amount to be paid: ")
            l_reference=input("reference Details: ")
            global liability
            liability = [l_date,l_type,l_loaner,l_intamount,l_intrest,l_amount,l_reference]
        liability()
        add_liability = ("INSERT INTO liability "
                         "(l_date, l_type, l_loaner, l_intamount, l_intrest, l_amount, l_reference) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s);")
        data_liability = (liability[0],liability[1],liability[2],liability[3],liability[4],liability[5],liability[6])
        cursor.execute(add_liability, data_liability)

        print("********************Data updated sucessfully inside liability table****************")
        print(data_liability)

    #commit code
    mydb.commit()
#    heart()
    print("------------------------------------------------------------------")
    print("***************Record sucessfully updated*************************")
    print("------------------------------------------------------------------")

    heart()
#Show records code start from here
else:
    print("-----------------------------------------------------------------------------------")
    print("|*********************ADMIN PERMISSION REQUIRED***********************************|")
    print("-----------------------------------------------------------------------------------")
    print("Show records By date ")
    print("1:income statement")
    print("2:expense statement")
    print("3:asset statement")
    print("4:liability statement")
    option = int(input("Enter Your Option: "))
    if option ==1:
        #sql query
        print("**********************Income Data************************************")
        query =("SELECT i_id, i_date, i_type, i_sender, i_amount,i_reference FROM income "
                "WHERE i_date BETWEEN %s AND %s")
        start_date=input("Enter Start Date: ")
        end_date=input("Enter End Date: ")
        cursor.execute(query, (start_date,end_date))
        print("ID date    type sender amount reference")
        for (i_id, i_date, i_type, i_sender, i_amount,i_reference) in cursor:
          print("{} {} {} {} {} {}".format(i_id, i_date, i_type, i_sender, i_amount,i_reference))

    elif option ==2:
        #sql query
        print("**********************Expense Data************************************")
        query =("SELECT e_id, e_date, e_type, e_exptype, e_reciever, e_amount, e_reference FROM expense "
                "WHERE e_date BETWEEN %s AND %s")
        start_date=input("Enter Start Date: ")
        end_date=input("Enter End Date: ")
        cursor.execute(query, (start_date,end_date))
        print("ID date    type expnese-type reciever amount reference")
        for (e_id,e_date,e_type,e_exptype,e_reciever,e_amount,e_reference) in cursor:
          print("{} {} {} {} {} {} {}".format(e_id,e_date,e_type,e_exptype,e_reciever,e_amount,e_reference))
    elif option ==3:
        #sql query
        print("**********************Asset Data************************************")
        query =("SELECT a_id, a_date, a_type, a_broker, a_taxes, a_status, a_amount, a_reference FROM asset "
                "WHERE a_date BETWEEN %s AND %s")
        start_date=input("Enter Start Date: ")
        end_date=input("Enter End Date: ")
        cursor.execute(query, (start_date,end_date))
        print("ID date     type broker taxes Status amount reference")
        for (a_id,a_date,a_type,a_broker,a_taxes,a_status,a_amount,a_reference) in cursor:
          print("{} {} {} {} {} {} {} {}".format(a_id,a_date,a_type,a_broker,a_taxes,a_status,a_amount,a_reference))
    elif option ==4:
        #sql query
        print("**********************Liability Data************************************")
        query =("SELECT l_id, l_date, l_type, l_loaner, l_intamount, l_intrest, l_amount, l_reference FROM liability "
                "WHERE l_date BETWEEN %s AND %s")
        start_date=input("Enter Start Date: ")
        end_date=input("Enter End Date: ")
        cursor.execute(query, (start_date,end_date))
        print("ID date     type lender initial intrest amount(f) reference")
        for (l_id,l_date,l_type,l_loaner,l_intamount,l_intrest,l_amount,l_reference) in cursor:
          print("{} {} {} {} {} {} {} {}".format(l_id,l_date,l_type,l_loaner,l_intamount,l_intrest,l_amount,l_reference))
    else:
        print("Invalid option.Exiting")
# Make sure data is committed to the database
mydb.commit()
cursor.close()
mydb.close()
#remember data will only reflect when data is commited
print("**********************Thank You************************************")
