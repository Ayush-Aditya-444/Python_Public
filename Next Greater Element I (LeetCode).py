class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums1)):
            a=nums2.index(nums1[i])
            for j in range(a,len(nums2)):
                try:
                    if nums2[a]<nums2[j+1]:
                        list1.append(nums2[j+1])
                        break
                    else:
                        continue
                except IndexError:
                    list1.append(-1)
        return list1