class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        loop through each num in array
        calculate complement 
        see if this number already in dict, 
        return idx of number in dict, and in current iter

        """

        my_dict = {} #{complement:idx}

        for idx, num in enumerate(nums): 
            complement = target - num
            if num in my_dict: 
                return [my_dict[num],idx]
            else: 
                my_dict[complement] = idx