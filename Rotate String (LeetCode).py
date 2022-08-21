class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        str1=s+s
        if goal in str1 and len(s)==len(goal):
            return True
        else:
            return False
        
        