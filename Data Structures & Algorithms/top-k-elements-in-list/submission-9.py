class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        loop through the array
            - update dict: {num: [count]} (increment count) 
        freq bucket (idx is count, item is a list of the numbers what that idx count)
        loop dec from the freq bucket, and read out the results

        """

        my_dict = {}
        res_arr = []

        for num in nums: 
            my_dict[num] = my_dict.get(num,0)+1

        freq_bucket = [[] for _ in range(len(nums)+1)]
        
        for key,v in my_dict.items(): 
            freq_bucket[v].append(key) 

        for idx in range(len(freq_bucket)-1,0,-1):
            for num in freq_bucket[idx]: 
                res_arr.append(num) 
                if len(res_arr) == k: 
                    return res_arr




