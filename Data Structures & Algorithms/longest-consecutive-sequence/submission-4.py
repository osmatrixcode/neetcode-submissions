class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        create a set (do not need to deal with duplicates) 
        loop through the numbers: 
        - if no n-1 number in the sequence, is the start of a sequence
        - if a smaller n-1 exists, not a start of a sequence
        """

        nums_set = set(nums) 
        max_num = 0

        for num in nums_set: 
            if num-1 in nums_set: #not a start of a sequence 
                continue
            else: 
                length = 0
                while num+length in nums_set: 
                    length+=1
                max_num = max(max_num,length) 

        return max_num