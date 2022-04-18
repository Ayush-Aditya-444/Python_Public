class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        a=0
        for i in range(len(seats)):
            a+=abs(students[i]-seats[i])
        return abs(a)