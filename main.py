from display import Display
from database import *
from user import User
from date import Date
from bill import Bill
import matplotlib.pyplot as plt

disp = Display()
db1 = Database("database")
db1.createtableifnotexists("users",User,User.fromline)
db1.createtableifnotexists("bills",Bill,Bill.fromline)

def registerUser():
    id, name, birthday, email, password, address, status = Display.enterRegisterInfo()
    userObj = User(id, name, Date.fromString(birthday), email, password, address, status)
    return userObj

def viewExpenses(db1, userName):
    user_input = input("Press 0 to view expenses by year, 1 to view expenses by month: ")

    if user_input == "0":
        start_year = int(input("Please enter the starting year that you want to view the total expenses: "))
        end_year = int(input("Please enter the end year that you want to view the total expenses: "))
        num_years = end_year - start_year +1
        years = []
        total_expenses = []

        for i in range(num_years):
            years.append(start_year+i)

        for i in range(num_years):
            year = str(years[i])
            bills = db1.getObjectsFrom("bills",
                                       lambda x: (x.getUserName() == userName and x.getDate().getYear() == year))
            single_year_expense = 0
            for i in range(len(bills)):
                single_year_expense += bills[i].getAmount()
            total_expenses.append(single_year_expense)

        plt.plot(years, total_expenses)

        print("years ",years)

        print("expenses",total_expenses)
        # naming the x axis
        plt.xlabel('Years')
        # naming the y axis
        plt.ylabel('Total Expenses')

        # giving a title to my graph
        plt.title('Total Expenses graph')

        # function to show the plot
        plt.show()

def manageBills(db1,userName):
     while True:
        print("Press 1 to add a bill, press 2 to change bill status, press 3 to show unpaid bills, press 4 to delete a bill, press 5 to view expenses, press 6 to return to Main Menu.")
        a = input("Please enter a number: ")
        if a == "1":
            addbill(db1, userName)
        elif a == "2":
            changeBillStatus(db1, userName)
        elif a == "3":
            showUnpayedBills(db1, userName)
        elif a == "4":
            deleteBill(db1, email)
        elif a == "5":
            viewExpenses(db1, userName)
        else:
            return
#
# def filterUnpayedBills(obj,userName,status):
#     if obj._userName==userName and obj._isPayed == status:
#         return True
#     else:
#         return False
#
#
# bills = db1.getObjectsFrom("bills",filterUnpayedBills(Bill,"Orlin Malkja",'n'))

#print(len(bills))

def showUnpayedBills(db1,userName):

    bills = db1.getObjectsFrom("bills",lambda x:( x.getUserName()==userName and x.isPaid()=='n' ))

    print("The Unpaid bills are the following:")
    if len(bills) ==0:
      print("There are no unpaid bills.")
    else:
      for bill in bills:
            print(bill.toString())
    #shto gjendjen e bill qe do ndryshuar, shto ndryshimin nga y ne n
    return

def addbill(db1, userName):

    id, isPaid, date, billType,amount= Display.addBill()  # valido
    line = str(id) + "," + str(isPaid) + "," + str(date) + ","+str(billType)+","+str(amount)+","+str(userName)
    billObject = Bill.fromline(line)

    # add the bill into the databaze
    try:
       db1.appendObjectsInto("bills",[billObject])
    except:
        print("Error while adding a bill in the database.")

def changeBillStatus(db1, userName):
    bills = db1.getObjectsFrom("bills", lambda x: (x.getUserName() == userName and x.isPaid() == 'n'))

    print("The unpaid bills are the following: ")
    for bill in bills:
        print(bill.toString())
    chosenbill = str(input("Enter the ID of the bill you have paid: "))
    bills1 = db1.getObjectsFrom("bills", lambda x: (x.getUserName() == userName and x.isPaid() == 'n' and x.findid() == chosenbill))
    for bill in bills1:
        bill.setPaid("y")
        db1.deleteObjectsFrom("bills",lambda x: (x.findid() == chosenbill ))
        db1.appendObjectsInto("bills",[bill])

    return

def deleteBill(db1, email):
  bills = db1.getObjectsFrom("bills", lambda x: (x.getUserName() == userName))
  print("Your registered bills are the following: ")
  for bill in bills:
    print(bill.toString())
  chosenbill = str(input("Enter the ID of the bill you wish to delete: "))
  bills1 = db1.getObjectsFrom("bills", lambda x: (x.getUserName() == userName and x.findid() == chosenbill))
  for bill1 in bills1:
    print("You are deleting the following bill: ")
    print(bill1.toString())
    db1.deleteObjectsFrom("bills", lambda x: (x.getUserName() == userName and x.findid() == chosenbill))


# create tables which are not created yet

#NOTE: the bill class should have a username (which refers to the person who is creating the bill)
#In the User class remove the bills[] attribute , since it would require some changes in the database

def start_session(db1,userName):
    #since we will do some actions with a certain user , we are "passing the parameters db and username (in order to keep track of the info of the current user in this function
    # and other functions to come"
    # TODO the main fonctionalities are implemented here after the user logs in
    # display menu , welcome message
    while True:
        choice = Display.menuLoggedInAsUser()

        if choice=="0":
            manageBills(db1, userName)
            # TODO Action to take when chosen 1
            pass
        if choice=="1":
            #TODO Action to take when chosen 2
            #manage Bills will be followed by a menu , which will display a menu (add a bill, update status of bill (unpayed->payed)
            #delete a certain bill)
            updateAccount(db1,userName)
            pass
        else :
            break


def updateAccount(db,user):
    # display current data
    # get new data
    # ask user if he/she is sure to save the changes (commit)
    # inform for status
    # return
    pass





while True:

    #Check if there are no registered users

    if len(db1.getObjectsFrom("users")) == 0:
        #id,name,birthday,email,password,address = disp.enterRegisterInfo()
        userObj =registerUser()
        try:
            # check if username exists

            db1.appendObjectsInto('users', [userObj])
        except:
            print("Error occured during adding a user in the database.")
        continue

    else:
        userInput = Display.welcome()

        if userInput == "0":
            email,password = Display.enterLoginInfo()

            obj = db1.getObjectsFrom("users",lambda x:( x._email==email and x._passw==password ))

            if len(obj)>0:
                userName = obj[0].getName()
                print("successful login")
                start_session(db1,userName)

            else:
                print("no such user exists")
                continue

        elif userInput == "1":
            #id, name, birthday, email, password, address = disp.enterRegisterInfo()
            userObj = registerUser()
            try:
                # check if username exists
                db1.appendObjectsInto('users', [userObj])
            except:
                print("Error occured during adding a user in the database")
            continue

        else:
            pass
            #users = db1.getObjectsFrom("users")

