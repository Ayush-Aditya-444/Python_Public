class Solution:
    def dayOfYear(self, date: str) -> int:
        date=date.split("-")
        if (int(date[0]) % 400 == 0) and (int(date[0]) % 100 == 0):
            leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            sum1=sum(leap_year[:int(date[1])-1])
            sum2=int(date[2])
            return sum1+sum2
        elif (int(date[0]) % 4 ==0) and (int(date[0]) % 100 != 0):
            leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            sum1=sum(leap_year[:int(date[1])-1])
            sum2=int(date[2])
            return sum1+sum2
        else:
            year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            sum1=sum(year[:int(date[1])-1])
            sum2=int(date[2])
            return sum1+sum2
        