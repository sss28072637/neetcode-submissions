class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in nums:
            ans = min(i, ans)

        return ans