class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        
        while True:
            m = (l + r) // 2
            mB = half - m - 2

            A_l = A[m] if m >= 0 else float("-inf")
            A_r = A[m + 1] if m + 1 < len(A) else float("inf")
            # larger array 
            B_l = B[mB] if mB >= 0 else float("-inf")
            B_r = B[mB + 1] if mB + 1 < len(B) else float("inf")

            if A_l > B_r:
                r = m - 1
            elif B_l > A_r:
                l = m + 1
            else:
                return (max(A_l, B_l) + min(A_r, B_r)) / 2 if total % 2 == 0 else min(A_r, B_r)