class Solution:
    def specialArray(self, nums: List[int]) -> int:
        i = 1 # set our i to 1
        n = len(nums) # for readability=
        max_num = max(nums) + 1 

        # max_num: 5
        # i: 2
        # n: 2
        # j: 0
        # count: 2

        while i < max_num:
            count = 0
            j = 0
            while j < n: # O(n)
                if nums[j] >= i:
                    count += 1
                j += 1
            
            if count == i:
                return count
            i += 1
            

        # time complexity: O(n * max_num)
                 
                
        return -1
    


    

            

            
            

