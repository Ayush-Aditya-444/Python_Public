from collections import deque
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary=deque(salary)
        salary.pop()
        salary.popleft()
        return sum(salary)/len(salary)
        