class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        list1=nums1+nums2+nums3
        list2=[]
        for i in range(len(list1)):
            if list1[i] in nums1 and list1[i] in nums2:
                list2.append(list1[i])
            elif list1[i] in nums2 and list1[i] in nums3:
                list2.append(list1[i])
            elif list1[i] in nums1 and list1[i] in nums3:
                list2.append(list1[i])
        return set(list2)