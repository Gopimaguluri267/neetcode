class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    # 5#hello5#world
    def decode(self, s: str) -> List[str]:
        decoded_result = []
        i = 0
        len_collector = 0
        while i < len(s):
            if s[i] == '#':
                length = int(s[i-len_collector:i])
                word = s[i+1:i+1+length]
                decoded_result.append(word)
                i = i+1+length
                len_collector = 0
            else:
                i+=1
                len_collector += 1
        
        return decoded_result
