from date import Date

class Bill:
    def __init__(self,id,isPayed,date,name,amount,userName):
        self._id = id
        self._isPayed = isPayed
        self._date = date
        self._name = name
        self._amount = amount
        self._userName = userName


    def isPayed(self):
        return self._isPayed

    def getUserName(self):
        return self._userName

    def toString(self):
        return str(self._id)+","+str(self._isPayed)+","+self._date.toString()+","+str(self._name)+","+str(self._amount)+","+str(self._userName)

    @classmethod
    def fromline(cls,line):
        fields = line.split(",")
        id = int(fields[0])
        isPayed = (fields[1])
        date = Date.fromString(fields[2])
        name = fields[3]
        amount = float(fields[4])
        userName = fields[5]

        return cls(id,isPayed,date,name,amount,userName)