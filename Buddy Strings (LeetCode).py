class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s=list(s)
        goal=list(goal)
        if len(s)!=len(goal):
            return False
        elif s == goal and len(s) != len(set(s)):
            return True
        else:
            differences = []
            for x in range(len(goal)):
                if s[x] != goal[x]:
                    differences.append([s[x], goal[x]])

            if len(differences) == 2 and differences[0] == differences[-1][::-1]:
                return True

            return False
                

            