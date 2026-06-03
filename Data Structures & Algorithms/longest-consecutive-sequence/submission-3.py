class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = 1
        for i in range(len(nums)):
            cnt = 1
            cur_num = nums[i] + 1
            while (cur_num in nums):
                # print(cur_num)
                cnt += 1
                cur_num += 1
            
            if cnt > ans:
                ans = cnt

        return ans
        