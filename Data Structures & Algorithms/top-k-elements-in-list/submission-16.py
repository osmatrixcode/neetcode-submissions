class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        my_dict = {}

        for num in nums: 
            my_dict[num] = my_dict.get(num,0)+1

        freq_bucket = [[] for _ in range(len(nums)+1)]

        for key, v in my_dict.items(): 
            freq_bucket[v].append(key) 

        res_arr = []

        for i in range(len(freq_bucket)-1,-1,-1): 
            if freq_bucket[i] != []: 
                for item in freq_bucket[i]: 
                    if len(res_arr) < k: 
                        res_arr.append(item)

        return res_arr
                        
                    
    