from display import Display
from database import *
from user import User
from date import Date
from bill import Bill

disp = Display()
db1 = Database("database")
db1.createtableifnotexists("users",User,User.fromline)
db1.createtableifnotexists("bills",Bill,Bill.fromline)

def registerUser():
    id, name, birthday, email, password, address = Display.enterRegisterInfo()
    userObj = User(id, name, Date.fromString(birthday), email, password, address)
    return userObj

def manageBills(db1,userName):
    while True:
        print(" 1 add a bill, 2-change bill status , 3-show unpayed bills 4-delete a bill 5-main menu")
        a = input("Please enter the number")
        if a=="1":
            addbill(db1,userName)
        elif a=="2":
            changeBillStatus(db1,userName)
        elif a=="3":
            showUnpayedBills(db1,userName)
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

    bills = db1.getObjectsFrom("bills",lambda x:( x.getUserName()==userName and x.isPayed()=='n' ))

    print("The Unpayed bills are the following")
    for bill in bills:
            print(bill.toString())
    return

def addbill(db1, userName):

    id, isPayed, date, billType,amount= Display.addBill()  # valido
    line = str(id) + "," + str(isPayed) + "," + str(date) + ","+str(billType)+","+str(amount)+","+str(userName)
    billObject = Bill.fromline(line)

    # add the bill into the databaze
    try:
       db1.appendObjectsInto("bills",[billObject])
    except:
        print("Error while adding a bill in the database")

def changeBillStatus(db1, email):
    # #Todo Shfaq faturat e papaguara, zgjedh njeren dhe i ndryshon statusin
    # Mund ta bejme dhe te shfaqe   ;
    # gjeje faturen sipas id , merr objektin e fatures, shfaq faturen, pyet a ta vendos te paguar
    # Nese po, set isPayed true
    # delete,append
    # nese i ben overwrite, lexo te gjitha , modifiko nje nga el e listes , overwrite te githe listes
    # bills = db.getobjectsfrom("bills",l)
        pass



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
            print("Error occured during adding a user in the database")
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

