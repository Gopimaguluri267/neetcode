class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_map = {}
        s_map = {}
        matches_needed = 0
        for i in t:
            t_map[i] = t_map.get(i,0)+1
            matches_needed+=1
            s_map[i] = 0
        
        result = ""
        max_len = float('inf')
        matches_have = 0
        
        i=0
        j=0
        while i<len(s) and j<len(s):
            if s[j] in t_map:
                if s_map.get(s[j],0) < t_map.get(s[j],0):
                    matches_have += 1
                s_map[s[j]] = s_map.get(s[j],0)+1

            while matches_needed == matches_have:
                if max_len > j-i+1:
                    result = s[i:j+1]
                    max_len = j-i+1

                if s[i] in s_map:
                    s_map[s[i]] = s_map.get(s[i])-1
                    if s_map.get(s[i],0) < t_map.get(s[i],0):
                        matches_have -= 1
                i += 1

                # if matches_needed == matches_have:
                #     if max_len > j-i+1:
                #         result = s[i:j+1]
                #         max_len = j-i+1
            j+=1

        return result

        