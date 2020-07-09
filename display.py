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
        isPaid = input("Paid? (y or n):")
        date = input("date:")
        types = ["Electricity bill", "Water bill", "Internet bill", "Phone bill"]
        for i in range(4):
          print("Press", i, "if this is a(n)", types[i])
        inp = int(input("Press 0, 1, 2 or 3:"))
        billType = types[inp]
        amount = input("Amount:")

        #valido te dhenat
        return id, isPaid, date, billType, amount

    @classmethod
    def enterRegisterInfo(self):
        attributes = ["ID","name","birthday","email","password","address","status"]
        print("Please enter the registration info")
        id = int(input("ID:"))
        name = input("name:")
        birthday = input("birthday:")
        email = input("email:")
        password = input("password:")
        address = input("address")
        statuses = ["user", "admin"]
        for i in range(2):
            print("Press", i, "if you're registering as a", statuses[i])
        inp = int(input("Press 0 or 1:"))
        status = statuses[inp]
        return id,name,birthday,email,password,address,status



