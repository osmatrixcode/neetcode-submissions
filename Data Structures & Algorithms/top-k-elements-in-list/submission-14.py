class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create a counter dictionary from the nums
        create a freq bucket, idx represents count, and item in the array is a bucket of all numbers that has that count of idx
        loop through the freq_bucket decremented, 
        add to a results array (making sure not reached k length) 
        """
        my_dict = {}
        freq_bucket = []
        res_arr = []

        for num in nums: 
            my_dict[num] = my_dict.get(num,0)+1

        freq_bucket = [[] for _ in range(len(nums)+1)]

        for key,v in my_dict.items(): 
            freq_bucket[v].append(key) #idx represents count, item is array of nums

        for i in range(len(freq_bucket)-1,0,-1):
            if freq_bucket[i] != []: 
                for num in freq_bucket[i]:
                    if len(res_arr) < k: 
                        res_arr.append(num)

        return res_arr
