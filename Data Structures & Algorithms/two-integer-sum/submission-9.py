class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        loop through the nums: 
            - fill in the dict
            - calculate the complement
            - check if complement in it 
        """

        my_dict = {}

        for idx, num in enumerate(nums): 
            print(str(idx) + str(num))
            complement = target - num

            if num in my_dict:
                return [my_dict[num], idx]
            
            else:
                my_dict[complement] = idx