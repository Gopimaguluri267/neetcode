class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        for i in nums:
            freq_counter[i] = freq_counter.get(i, 0)+1
        
        freq_counter = dict(sorted(freq_counter.items(), key=lambda x:x[1], reverse=True))
        
        return list(freq_counter.keys())[:k]