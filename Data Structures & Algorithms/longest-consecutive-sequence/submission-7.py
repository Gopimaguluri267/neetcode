class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,3,4,4,5,10,20]
        max_seq_len = 0
        nums_set = set(nums)
        for i in nums:
            if i-1 not in nums_set:
                seq_start = i+1
                curr_max = 1
                while seq_start in nums_set:
                    curr_max += 1
                    seq_start += 1
                max_seq_len = max(max_seq_len, curr_max)
        
        return max_seq_len