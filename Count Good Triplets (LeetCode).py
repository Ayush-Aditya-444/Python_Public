class Solution:
    def countGoodTriplets(self, ar: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(ar)):
            for j in range(i+1, len(ar)):
                for k in range(j+1, len(ar)):
                    if abs(ar[i]-ar[j])<=a and abs(ar[j]-ar[k])<=b and abs(ar[i]-ar[k])<=c:
                        count += 1
        return count