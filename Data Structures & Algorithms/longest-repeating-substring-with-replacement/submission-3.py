class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0
        maxFreq = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(count[s[right]], maxFreq)
            while (right-left+1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, (right-left+1))

        return ans