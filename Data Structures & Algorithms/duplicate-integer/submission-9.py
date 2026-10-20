class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        create dict: number: counter 
        loop through and create dict, 
        if dict already 1 when checked, (so +1) then that means we contain duplicate
        else false
        '''

        my_dict = {}

        if len(nums) == 0:
            return False

        for num in nums: 
            if num in my_dict:
                return True
            else:
                my_dict[num] = 1


        return False