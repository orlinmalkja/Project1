import os
from os import path

class Database:
    def __init__(self,dbname,dbpath="."):
        # set the destination path for the database folder
        self.mainpath = dbpath+path.sep+dbname
        if(not path.exists(self.mainpath)):
            # if folder does not exists create a new one
            os.mkdir(self.mainpath)
        # create a dictionary that will hold tables
        self.tables = {}

    # creates a file if it does ont exists
    def createtableifnotexists(self,tname,ttype,toObject):
        # check if is created before
        if(not path.exists(self.mainpath+path.sep+tname)):
            # add specific entry into the dictionary
            self.tables[tname]=Table(self.mainpath+path.sep+tname,ttype,toObject)
            # create respective file
            fd = open(self.mainpath+path.sep+tname,"w")
            fd.close()
        else:
            # scince the file already exists just add the entry into the dictionary
            self.tables[tname]=Table(self.mainpath+path.sep+tname,ttype,toObject)

    # get a list of objects from a specific table. you can also filter by a lambda function
    def getObjectsFrom(self,tname,condition=lambda a:True):
        # find table data from the dictionary
        table = self.tables[tname]
        # open the file
        with (open(table.getpath(),"r")) as fp:
            records = []
            # read all lines
            lines = fp.readlines()
            try:
                for line in lines:
                    # construct the object by the specific function
                    record = table.toObject(line.split("\n")[0])
                    # if object fullfill the condition then add into list

                    #print("line ",line)
                    if(condition(record)):
                        records.append(record)
            except:
                print("..")
            # close the file and then return the ist of selected objects
            fp.close()
            return records
        return(101,"file not found")

    def updateUser(self,tname,condition=lambda a:True):

        #toDo
        # find table data from the dictionary
        table = self.tables[tname]
        # open the file
        with (open(table.getpath(),"r")) as fp:
            records = []
            # read all lines
            lines = fp.readlines()
            for line in lines:
                # construct the object by the specific function
                record = table.toObject(line)
                # if object fullfill the condition then add into list
                print("testing",condition(record))
                if(condition(record)):
                    records.append(record)
            # close the file and then return the ist of selected objects
            fp.close()
            return records
        return(101,"file not found")

    def updateUsers(self,tname,obj):
        pass

    def validateLogin(self,tname,email,passw):
        table = self.tables[tname]
        # open the file
        with (open(table.getpath(), "r")) as fp:
            records = []
            # read all lines
            lines = fp.readlines()
            for line in lines:
                # construct the object by the specific function
                record = table.toObject(line)
                # if object fullfill the condition then add into list
                if (condition(record)):
                    records.append(record)
            # close the file and then return the ist of selected objects
            fp.close()
            return records
        return (101, "file not found")

    # this method just adds the objects in the end of the file
    def appendObjectsInto(self,tname,records):
        table = self.tables[tname]
        # after taking table data open file
        with open(table.getpath() ,"a") as fp:
            for  record in records:
                # if object is of specififed type
                if table.checkType(record):
                    # write it into the file
                    fp.write(record.toString()+"\n")
            fp.close()

    def appendObjectInto(self,tname,obj):
        self.appendObjectsInto(tname,[obj])
    # this function deletes records specifying a specific function
    def deleteObjectsFrom(self,tname,condition=lambda x:False):
        # select the respective table from dictionary
        table = self.tables[tname]
        # read all records
        with (open(table.getpath(),"r")) as fp:
            # read all lines of data one line for one object
            lines = fp.readlines()
            fp.close()
        # write onnly those that do not fullfill the condition
        with(open(table.getpath(),"w") )as fp:
            # for each line
            for line in lines:
                # construct the apropriate object using the
                # function toObject of the respective table
                record = table.toObject(line)
                if(not condition(record)):
                    fp.write(line)
            fp.close()
        return(101,"file not found")

    # this function writes objects in a file but the
    # old data is always lost
    def overwriteObjectsInto(self,tname,newobjects):
        # select the table
        table = self.tables[tname]
        # open the file
        with open(table.getpath() ,"w") as fp:
            # for each object
            for  newobject in newobjects:
                # check if it is an apropriate type for this table
                if table.checkType(newobject):
                    # dump the record into the table
                    fp.write(newobject.toString()+"\n")
            fp.close()

class Table :
    # a table is an instance that is defined by
    # a path where the objects are stored (lines)
    # a type stating types of objects stored in file
    # a toObject method that converts a line into an object
    # of specified type
    def __init__(self,tpath,ttype,toObject):
        self.__tpath = tpath
        self.__type = ttype
        self.__toObject = toObject

    # table destination in file system
    def getpath(self):return self.__tpath
    # checks if an object is of table specified type
    def checkType(self,ttype):return self.__type==type(ttype)
    # returns a line into an object of specified type of table
    def toObject(self,line):return self.__toObject(line)


# simple base object
class BaseObject:
    def __init__(self,ID):
        self._ID = ID
    def setID(self,newID):self._ID = newID

    def getID(self):return self._ID

    # mandatory method for each class storable to be created
    # returns a line holding information for a specific object
    def toString(self):
        # all fields separated by comma ending the line with \n
        return str(self._ID)

    #gets a line  of string and from that line the object is constructed
    # methods toString and fromLine are inverse of each other as
    #  class.fromString(a.toString()).toString() =  a.toString()
    @classmethod
    def fromLine(cls,line):
        tokens = line.split(",")
        return cls(tokens[0])

# create three simple objects
# Obj1 = BaseObject(1)
# Obj2 = BaseObject(2)
# Obj3 = BaseObject(3)

# # create the database object
# db = Database(dbname="database1")
#
# # create table if not exists pass as argument table name, object type to sav
# # and the function to convert a line into an object
# db.createtableifnotexists("baseobjects",BaseObject,BaseObject.fromLine)
# # append the objects in the table. you can append one or more objects
# db.appendObjectsInto("baseobjects",[Obj1,Obj2,Obj3])
# # table state  1\n2\n3\n
#
# db.overwriteObjectsInto("baseobjects",[BaseObject(1),BaseObject(3),BaseObject(7)])
# # table state 1\n2\n7\n
# # get the objects
# a = db.getObjectsFrom("baseobjects",lambda c:True)
# print(a)



class Bill:
    def __init__(self,id,isPayed,date,name,amount):
        self._id = id
        self._isPayed = isPayed
        self._date = date
        self._name = name
        self._amount = amount


    def toString(self):
        return str(self._id)+","+self._isPayed+","+self._date.toString()+","+str(self._name)+","+str(self._amount)

    @classmethod
    def fromline(cls,line):
        fields = line.split(",")
        id = int(fields[0])
        isPayed = (fields[1])
        date = Date.fromString(fields[2])
        name = fields[3]
        amount = float(fields[4])
        return cls(id,isPayed,date,name,amount)



#print("test 1")
# bill1 = Bill(1,Date.fromString("2020/12/1"),"Fature Dritash",20.5)
# bill2 = Bill(2,Date.fromString("2020/11/1"),"Fature Uji",17.5)
# bill3 = Bill(3,Date.fromString("2020/10/1"),"Fature Telefoni",13.5)

#user1 = User(1,"Orlin Malkja",Date.fromString("2020/12/10"),"omalkja17@epoka.edu.al","0123")


#db1 = Database("database")
#db1.createtableifnotexists("bill",Bill,Bill.fromline)
#
#db1.createtableifnotexists("users",User,User.fromline)
#
#db1.appendObjectsInto("users",[user1])
#
#db1.appendObjectsInto("bill",[bill1, bill2, bill3])
#
#db1.deleteObjectsFrom("bill",lambda x:x._id==1)

#db1.overwriteObjectsInto("storebill",[bill4, bill5])

#records = db1.getObjectsFrom("bill")

# for record in records:
#      print(record._id,record._date.toString())



#bills = [bill1,bill2,bill3]

def ofilter(obj):
    if obj._id==2:
        return True
    else:
        return False


# #TODO 16.06 -
#
# #Krijoni klasat perkatese ku pervec metodave te tjera , te JENE  metoda toString dhe metoda fromLine(qe kthen nga nje rresht ne nje objekt)
#
# #Testoni metodat
# #1 createtableifnotexists()
# #2 getObjectsFrom()
# #3 appendObjectsInto()
# #4 deleteObjectsFrom()
#
# records = db1.getObjectsFrom('bill')
# print("-------")
# for record in records:
#     print(record.toString())

#
#faturat = db1.deleteObjectsFrom("bill",ofilter)





#
# for fatura in faturat:
#     print("Faturat ",fatura.toString())
#
