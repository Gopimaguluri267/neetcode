class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                curr_sum = nums[i]+nums[l]+nums[r]
                if curr_sum == 0:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                elif curr_sum > 0:
                    r-=1
                elif curr_sum < 0:
                    l+=1
        
        return result
