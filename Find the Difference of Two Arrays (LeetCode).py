class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1=[]
        list2=[]
        list3=[]
        nums1=set(nums1)
        nums1=list(nums1)
        nums2=set(nums2)
        nums2=list(nums2)
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                list1.append(nums1[i])
        list3.append(list1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                list2.append(nums2[i])
        list3.append(list2)
        return list3