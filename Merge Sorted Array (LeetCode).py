class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
			# Index to append to: len(nums1)-1 = m+n-1
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1  # Check the next element in nums1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1  # Check the next element in nums2
		# The remaining k elements in nums2 can just be inserted into the front
		# If k == 0, nums2 has already been merged, so this for loop is also skipped
        for i in range(n):
            nums1[i] = nums2[i]
		# nums1[:n] = nums2[:n]  # one-liner