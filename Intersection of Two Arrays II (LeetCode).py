class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        counter = counter1 & counter2
        return list(counter.elements())