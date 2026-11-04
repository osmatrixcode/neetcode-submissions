class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        get a dictionary that is num: Bool
        if already there, then return True, else False
        """

        my_dict = {}

        for num in nums: 
            if num in my_dict: 
                return True
            else: 
                my_dict[num] = True

        return False