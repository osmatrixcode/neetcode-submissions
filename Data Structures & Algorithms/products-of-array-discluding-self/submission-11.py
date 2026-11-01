class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res_arr = []

        prefix = 1
        for i in range(n):
            res_arr.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1): 
            res_arr[i] *= suffix
            suffix *= nums[i]

        return res_arr