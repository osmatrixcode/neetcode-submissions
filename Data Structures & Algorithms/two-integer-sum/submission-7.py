class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        my_dict = {} #{diff: idx}


        for i, num in enumerate(nums): 
            diff = target - num
            if diff in my_dict: 
                return [my_dict[diff],i]
            else:
                my_dict[num] = i
