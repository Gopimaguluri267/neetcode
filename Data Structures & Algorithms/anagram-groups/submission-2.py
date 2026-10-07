class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for s in strs:
            sorted_s = ''.join(sorted(list(s)))
            anagram_groups.setdefault(sorted_s, []).append(s)
        
        return list(anagram_groups.values())
