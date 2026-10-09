class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        sub_seq = set()

        for r in range(len(s)):
            while s[r] in sub_seq:
                sub_seq.remove(s[l])
                l += 1
            
            sub_seq.add(s[r])
            max_len = max(max_len, (r-l)+1)
        
        return max_len