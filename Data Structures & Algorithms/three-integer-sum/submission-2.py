class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)
        nums.sort() # O(1) space with O(n)
        triplets = []


        for i, n in enumerate(nums): # O(n)
            
            target = -1 * n

            if i > 0 and n == nums[i-1]: # do this to avoid the duplicates
                continue

            j, k = i + 1, length - 1
            while j < k:
                summ = nums[j] + nums[k]
                if summ < target: 
                    j += 1
                elif summ > target:
                    k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
               
        return triplets
        
                            
