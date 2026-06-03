class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        ans = 1
        for i in range(len(s)):
            chars = set()
            chars.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in chars:
                    break
                else:
                    chars.add(s[j])
                    ans = max(ans, len(chars))
                
        return ans