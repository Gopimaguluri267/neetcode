class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        seen = {}

        s1_set = {}
        for i in s1:
            s1_set[i] = s1_set.get(i, 0)+1
        
        while l<len(s2) and r<len(s2):
            
            while r<len(s2) and s2[r] in s1 and seen.get(s2[r],0)<s1_set[s2[r]]:
                seen[s2[r]] = seen.get(s2[r], 0)+1
                r+=1
            
            if seen == s1_set:
                return True

            if s2[l] in seen:
                seen[s2[l]] = seen.get(s2[l], 0)-1

            l+=1
            if l>r:
                r=l
            # r+=1
            
        return False