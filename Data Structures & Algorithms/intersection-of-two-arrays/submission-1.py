
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1 = len(nums1)
        n2 = len(nums2)

        nums1.sort()
        nums2.sort()

        res, i, j = [], 0, 0

        while i < n1 and j < n2:
            while (i < n1 and j < n2) and nums1[i] < nums2[j]:
                i += 1
            while (j < n2 and i < n1) and nums2[j] < nums1[i]:
                j += 1
            
            # lowkey wondering what the conditions are for this nonsense
            if (i < n1 and j < n2) and nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1

            while (i < n1) and (i - 1 >= 0) and nums1[i] == nums1[i - 1]:
                i += 1
            while (j < n2) and (j - 1 >= 0) and nums2[j] == nums2[j - 1]:
                j += 1

        return res
              


    
        