class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(B) + len(A)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A 


        l, r = 0, len(A) - 1

        while True:
            left_a = (l + r) // 2
            left_b = half - left_a - 2
            # wanna know if the half is valid

            A_l = A[left_a] if left_a >= 0 else float("-inf")
            A_r = A[left_a + 1] if left_a + 1 < len(A) else float("inf")
            B_l = B[left_b] if left_b >= 0 else float("-inf")
            B_r = B[left_b + 1] if left_b + 1 < len(B) else float("inf")

            if A_l > B_r:
                r = left_a - 1
            elif B_l > A_r:
                l = left_a + 1
            else:
                return (max(A_l, B_l) + min(A_r, B_r)) / 2 if total % 2 == 0 else min(A_r, B_r)

            





            





        




        



        