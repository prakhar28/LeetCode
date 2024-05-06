class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = []
        l1 = 0
        l2 = 0
        len1 = len(nums1)
        len2 = len(nums2)

        while l1 < len1 or l2 < len2:
            if l1 == len1:
                mergedArr.extend(nums2[l2:])
                break
            if l2 == len2:
                mergedArr.extend(nums1[l1:])
                break
            
            if nums1[l1] <= nums2[l2]:
                mergedArr.append(nums1[l1])
                l1 += 1
            else:
                mergedArr.append(nums2[l2])
                l2 += 1
            
        mid = len(mergedArr) // 2
        if len(mergedArr) % 2 == 1:
            return mergedArr[mid]
        else:
            return (mergedArr[mid] + mergedArr[mid - 1]) / 2
            

