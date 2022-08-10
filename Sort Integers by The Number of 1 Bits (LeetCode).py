class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # so I iterate through arr, take every n and count "1" in their binary str and append [count, n] to stack.
        # After that I sort stack. Sorting happens on stack[0].
        # Now I just use list comprehension and update my arr, only adding num in arr. 
		# Finally I return arr.
		
        stack = []

        for n in arr:
            count = bin(n)[2:].count("1")
            stack.append([count, n])
        
        stack.sort()
        list1=[]
        for i in range(len(stack)):
            list1.append(stack[i][1])
        return list1
    