from date import Date

class Bill:
    def __init__(self,id,isPaid,date,billType,amount,userName):
        self._id = id
        self._isPaid = isPaid
        self._date = date
        self._billType = billType
        self._amount = amount
        self._userName = userName

    def findid(self):
        return str(self._id)

    def isPaid(self):
        return self._isPaid

    def setPaid(self, x):
        self._isPaid = x

    def getUserName(self):
        return self._userName

    def getDate(self):
        return self._date

    def getAmount(self):
        return float(self._amount)

    def toString(self):
        return str(self._id)+","+str(self._isPaid)+","+self._date.toString()+","+str(self._billType)+","+str(self._amount)+","+str(self._userName)

    @classmethod
    def fromline(cls,line):
        fields = line.split(",")
        id = int(fields[0])
        isPaid = (fields[1])
        date = Date.fromString(fields[2])
        billType = fields[3]
        amount = float(fields[4])
        userName = fields[5]

        return cls(id,isPaid,date,billType,amount,userName)