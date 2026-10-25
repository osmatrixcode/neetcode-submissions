class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        dict: "{diff: idx}" to get this diff value, get the number at idx
        loop through nums array: 
        calculate diff 
        check if 'diff' in dictionary
        return idx of item in dict, and current item in the loop
        """


        my_dict = {} #{diff: idx}

        for idx, num in enumerate(nums): 
            diff = target - num
            if num in my_dict: 
                print(str(my_dict[num]),str(idx))
                return [my_dict[num], idx] 
            else:
                my_dict[diff] = idx
        
            