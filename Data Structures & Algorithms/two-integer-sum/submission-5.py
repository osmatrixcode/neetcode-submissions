class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        create a dict: num: idx
        enumerate over the array 
        calculate diff, return if in the dict 
        '''

        my_dict = {} #{num: idx}

        for i, num in enumerate(nums): 
            diff = target - num

            if diff in my_dict: 
                return [my_dict[diff], i]

            my_dict[num] = i
