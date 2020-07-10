class Date:
    def __init__(self,year,month,day):
        self._year = year
        self._month = month
        self._day = day

    def toString(self):
        return str(self._year)+"/"+str(self._month)+"/"+str(self._day)

    def getYear(self):
        return str(self._year)
    def getMonth(self):
        return str(self._month)

    @classmethod
    def fromString(cls,pattern):
        fields = pattern.split("/")
        return cls(fields[0],fields[1],fields[2])

   