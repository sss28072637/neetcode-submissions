class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            ans_arr = [0] * len(nums)
            for i in range(len(nums)):
                ans = 1
                for j in range(len(nums)):
                    if i != j:
                        ans *= nums[j]
                ans_arr[i] = ans
            return ans_arr
        