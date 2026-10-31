class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        loop through the numbers
        -calculate the complement
        -check if curr num in the dict DS 
        return current idx, and the complements idx

        so the dict {complement:idx}
        """
        my_dict = {}
        for idx, num in enumerate(nums): 
            complement = target - num

            if num in my_dict: 
                return [my_dict[num], idx]
            else: 
                my_dict[complement] = idx

                