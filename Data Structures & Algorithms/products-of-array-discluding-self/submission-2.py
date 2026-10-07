class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] # 1,1,2,8
        for i in range(1, len(nums)):
            prefix_prod.append(nums[i-1]*prefix_prod[i-1])
        
        result = [1]*len(nums) # 8
        suffix_prod = 1
        for j in range(len(nums), 0, -1): # 4 3 2 1
            result[j-1] = prefix_prod[j-1]*suffix_prod # 8 12 24 48
            suffix_prod *= nums[j-1] # 6 | 24 | 48
        
        return result
