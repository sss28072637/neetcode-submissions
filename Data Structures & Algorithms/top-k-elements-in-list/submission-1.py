class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        
        ans = []
        cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            ans.append(cnt[i][0])
                    
        return ans
