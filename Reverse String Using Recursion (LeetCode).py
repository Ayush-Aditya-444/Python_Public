class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def ayush(left,right,str1):
            if left>=right:
                return
            str1[left],str1[right]=str1[right],str1[left]
            ayush(left+1,right-1,str1)
        left=0
        right=len(s)-1
        a=ayush(left,right,s)