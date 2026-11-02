class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        calculate prefix sums
        calculate suffix sums 
        will update res_arr accoringly 
        """

        res_arr = [1 for _ in range(len(nums))]
        n = len(nums)

        prefix = 1
        for i in range(n): 
            res_arr[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            res_arr[i] *= suffix
            suffix *= nums[i]

        return res_arr