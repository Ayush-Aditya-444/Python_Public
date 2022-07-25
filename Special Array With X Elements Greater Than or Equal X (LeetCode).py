class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while l <= r:
            mid = (l+r)//2
            count = 0
            for n in nums:
                if n >= mid:
                    count += 1
            if count == mid:
                return mid
            elif count < mid:
                r = mid-1
            else:
                l = mid+1
        return -1