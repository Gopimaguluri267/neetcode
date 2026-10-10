class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        result = 0
        freq_counter = {}
        r = 0

        while r<len(s): # 0 1 2 3 4 5 6
            freq_counter[s[r]] = freq_counter.get(s[r], 0)+1 # {A:2 B:3}
            max_freq = max(max_freq, freq_counter[s[r]]) # 4

            while (r-l)+1 - max_freq > k: # 1>1 2>1
                freq_counter[s[l]] -= 1
                l += 1 # 1 2

            result = max(result, (r-l)+1) # 5
            r+=1
        
        return result
                
