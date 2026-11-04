class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        numSet = set(nums)

        for num in numSet: 
            
            if (num-1) in numSet: 
                continue
            else: 
                length = 0
                while (num+length) in numSet: 
                    length+=1
                max_length = max(max_length,length)

        return max_length