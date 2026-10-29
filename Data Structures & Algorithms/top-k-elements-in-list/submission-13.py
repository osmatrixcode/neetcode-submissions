class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        store some way {num:counter}
        create freq_bucket array [[],[]] etc...
            - the idx represents count, and array item contains numbers  with idx count 
            - loop through the freq_bucket decrement
            - append to res_arr until K items in the array 
        """

        my_dict = {} #{num:count}
        res_arr = []
        for num in nums: 
            my_dict[num] = my_dict.get(num,0)+1

        freq_bucket = [[] for _ in range(len(nums)+1)]

        for key,v in my_dict.items(): 
            freq_bucket[v].append(key) 

        for i in range(len(freq_bucket)-1,0,-1): #doesnt matter to get idx 0 as useless ()
            if freq_bucket[i] != []: #not an empty bucket
                for num in freq_bucket[i]:
                    if len(res_arr) < k: 
                        res_arr.append(num) 
            else:
                continue


        return res_arr
