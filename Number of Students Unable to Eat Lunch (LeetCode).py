from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students=deque(students)
        sandwiches=deque(sandwiches)
        z=True
        count1=0
        count2=0
        b=0
        while z==True:
            try:
                if sandwiches[count1]==students[count2]:
                    sandwiches.popleft()
                    students.popleft()
                    b=0
                elif sandwiches[count1]!=students[count2]:
                    a=students.popleft()
                    students.append(a)
                    b+=1
                    if b==len(students):
                        break
            except IndexError:
                break
        return len(students)
        