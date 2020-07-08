class Display:
    #Why declared as static method ?
    @staticmethod
    def welcome():
        actions = ['Log in','Register','Help']

        for i in range(len(actions)):
            print("Please type",i,"to",actions[i])

        userInput = input("Input: ")
        return userInput

    @staticmethod
    def enterLoginInfo():
        print("Please enter the following info in order to log in")
        email = input("Email: ")
        passw = input("Password: ")
        return email, passw

    @staticmethod
    def menuLoggedInAsUser():
        actions = ['Manage Bills']
        for i in range(len(actions)):
            print("Please type", i, "to", actions[i])
        userInput = input("Input: ")
        return userInput

    @staticmethod
    def addBill():
        print("Please enter the following info for the bill")
        id = (input("ID: "))
        isPayed = input("Payed? (y or n): ")
        date = input("Date: ")
        types = ["Electricity bill", "Water bill", "Internet bill", "Phone bill"]
        for i in range(4):       
          print("Press", i, "if this is a(n)", types[i])
        inp = int(input("Type 0, 1, 2 or 3: "))
        billType = types[inp]
        amount = input("Amount: ")

        #valido te dhenat
        return id, isPayed, date, billType, amount

    @classmethod
    def enterRegisterInfo(self):
        attributes = ["ID","name","birthday","email","password"]

        print("Please enter the registration info")
        id = int(input("ID: "))
        name = input("Name: ")
        birthday = input("Birthday: ")
        email = input("Email: ")
        password = input("Password: ")
        address = input("Address: ")
        return id,name,birthday,email,password,address



