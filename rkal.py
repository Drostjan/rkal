class Calendar:
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self, day=1,month=1,year=1900):
        self.day = day
        self.month = month
        self.year = year

    def bisyear(self, year):
        if year % 4 == 0:
            return 1
        else: return 0

    def setDate(self, year, month,day):
        self.year = year
        self.month = month
        self.day = day

    def getDate(self):
        return self.__str__()

    def update(self):
        months = Calendar.months
        max_days = months[self.month - 1]
        if self.month == 2:
            max_days += self.bisyear(self.year)
        if self.day == max_days:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else: 
                self.month +=1

        else: 
            self.day += 1

    def __str__(self):
    	return str(self.day) + "/" + str(self.month) + "/" + str(self.year)
        
