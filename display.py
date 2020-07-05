class Display:
    #Why declared as static method ?
    @staticmethod
    def welcome():
        actions = ['Log in','Register','Help']

        for i in range(len(actions)):
            print("Please type",i,"to",actions[i])

        userInput = input("Input:")
        return userInput

    @staticmethod
    def enterLoginInfo():
        print("Please enter the following info in order to log in")
        email = input("email")
        passw = input("password")
        return email, passw

    @staticmethod
    def menuLoggedInAsUser():
        actions = ['Manage Bills']
        for i in range(len(actions)):
            print("Please type", i, "to", actions[i])
        userInput = input("Input:")
        return userInput

    @staticmethod
    def addBill():
        print("Please enter the following info for the bill")
        id = (input("ID:"))
        isPayed = input("Payed? (y or n):")
        date = input("date:")
        name = input("Name:")
        amount = input("Amount:")

        #valido te dhenat
        return id, isPayed, date, name, amount

    @classmethod
    def enterRegisterInfo(self):
        attributes = ["ID","name","birthday","email","password"]

        print("Please enter the registration info")
        id = int(input("ID:"))
        name = input("name:")
        birthday = input("birthday:")
        email = input("email:")
        password = input("password:")
        address = input("address")
        return id,name,birthday,email,password,address



