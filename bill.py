class Bill:
    def __init__(self, creator, billtype, date, paid, price):
        self.creator = creator
        self.billtype = billtype
        self.date = date
        self.paid = paid
        self.price = price

    @classmethod
    def fromstringbill(cls, x):
        _creator, _billtype, _date, _paid, _price = x.split("-")
        return cls(_creator, _billtype, _date, _paid, _price)

    def getCreator(self):
        return self.creator
    def getBilltype(self):
        return self.billtype
    def getDate(self):
        return self.date
    def getPaid(self):
        return self.paid
    def getPrice(self):
        return self.price

    def setCreator(self, creator):
        self.creator = creator
    def setBilltype(self, billtype):
        self.billtype = billtype
    def setDate(self, date):
        self.date = date
    def setPaid(self, paid):
        self.paid = paid
    def setPrice(self, price):
        self.price = price
