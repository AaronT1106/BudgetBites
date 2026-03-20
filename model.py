#creating an expense class that keeps track of:
#meal name, amount, category, and date

class Expense:

    def __init__(self, name,amount, category, date ):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    