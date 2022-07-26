class Solution:
    def largestInteger(self, num: int) -> int:
        # so first we identify even and odd digits and store them in lists even[] & odd[]
		# then we sort even & odd lists so the largest even/odd digit is at the last [-1]the index
		# then we go through our given num(which we typecast into list) and see if the digit is
		# even, we swap that digit by poping the last largest digit from even list and we do the 
		# same when we see a odd digit. Lastly we join each element into a str and return the
		# int object of num. That's it. 
        odd = []
        even = []
        num = str(num)
        for n in num:
            if int(n)%2 == 0:
                even.append(n)
            else:
                odd.append(n)
        even.sort()
        odd.sort()
        num = list(num)
        for i in range(len(num)):
            if int(num[i])%2 == 0:
                num[i] = even.pop()
            else:
                num[i] = odd.pop()
        return int("".join(num))