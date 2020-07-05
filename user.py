from date import Date
class User:
    def __init__(self,id,name,bdate,email,passw,address):
        self._id = id
        self._name = name
        self._bdate = bdate
        self._email = email
        self._passw = passw
        self._address = address



    def toString(self):
        return str(self._id)+","+self._name+","+self._bdate.toString()+","+str(self._email)+","+str(self._passw)+","+self._address


    @classmethod
    def fromline(cls,line):
        fields = line.split(",")
        id = int(fields[0])
        name = fields[1]
        bdate = Date.fromString(fields[2])
        email = fields[3]
        passw = fields[4]
        address = (fields[5])
        return cls(id,name,bdate,email,passw,address)


    def getName(self):
        return self._name