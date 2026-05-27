class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = dict()
        for c in s:
            if c in freq_s:
                freq_s[c] += 1
            else:
                freq_s[c] = 1
        
        freq_t = dict()
        for c in t:
            if c in freq_t:
                freq_t[c] += 1
            else:
                freq_t[c] = 1
        
        if freq_s == freq_t:
            return True
        else:
            return False