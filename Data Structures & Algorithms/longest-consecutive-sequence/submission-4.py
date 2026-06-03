class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0

        for num in numset:
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                ans = max(length, ans)
        return ans

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0

    #     ans = 1
    #     for i in range(len(nums)):
    #         cnt = 1
    #         cur_num = nums[i] + 1
    #         while (cur_num in nums):
    #             # print(cur_num)
    #             cnt += 1
    #             cur_num += 1
            
    #         if cnt > ans:
    #             ans = cnt

    #     return ans
        