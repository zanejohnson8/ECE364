class Duration:

    def __init__(self, weeks, days, hours):
            chk = isinstance(weeks, int)
            if (chk != True):
                raise TypeError("Cannot instantiate an object with non-integer values.")
            chk = isinstance(days, int)
            if (chk != True):
                raise TypeError("Cannot instantiate an object with non-integer values.")
            chk = isinstance(hours, int)
            if (chk != True):
                raise TypeError("Cannot instantiate an object with non-integer values.")

            if (weeks < 0):
                raise ValueError("Cannot instantiate an object with negative values.")
            if (days < 0):
                raise ValueError("Cannot instantiate an object with negative values.")
            if (hours < 0):
                raise ValueError("Cannot instantiate an object with negative values.")

            if (hours >= 24):
                chk = hours % 24
                self.hours = chk
                test = hours / 24
                self.days = int(test)
            else:
                self.days = 0
                self.hours = hours

            if (days >= 7):
                chk = days % 7
                self.days += chk
                test = days / 7
                self.weeks = weeks + int(test)
            else:
                self.days = days
                self.hours = hours
                self.weeks = weeks



    def __str__(self):
        return ("{0:02d}W {1}D {2:02d}H".format(self.weeks, self.days, self.hours))

    def getTotalHours(self):
        return (self.weeks * (7 * 24) + self.days * 24 + self.hours)

    def __mul__(self,other):
        if (isinstance(other, int) == False):
            raise TypeError("Must be of type integer.")
        elif (other <= 0):
            raise ValueError("Must be greater than 0.")
        else:
            self.weeks = self.weeks * other
            self.days = self.days * other
            self.hours = self.hours * other
            return self

    def __add__(self, other):
        if (isinstance(other, Duration) == False):
            raise TypeError("Expected: type Duration")
        else:
            tmp1 = Duration.getTotalHours(self)
            tmp2 = Duration.getTotalHours(other)
            ret = tmp1 + tmp2
            return ret

if __name__ == "__main__":
    tst = Duration(0,1,24)
    tst1 = Duration(0,1,24)
    ret = Duration.getTotalHours(tst)
    print(tst * 2)