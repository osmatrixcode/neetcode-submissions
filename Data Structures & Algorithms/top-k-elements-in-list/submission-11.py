class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create a counter dict: {num:count}
        append to res_arr the k most frequent nums with highest counts
        - get a freq bucket array, idx represents count, bucket item contains all numbers with that frequency   
            - create by making freq_bucket_arr, filled with empty arr items (is length of size of the nums array) 

        """



        counter_nums = {}

        for num in nums: 
            counter_nums[num] = counter_nums.get(num,0)+1

        freq_bucket_arr = [[] for _ in range(len(nums)+1)] # we +1 due to not include a zero bucket icea 


        for key, v in counter_nums.items(): 
            freq_bucket_arr[v].append(key) 

        res_arr = []
        for idx in range(len(freq_bucket_arr)-1,0,-1): 
            if freq_bucket_arr[idx] != []: #not an empty item
                for item in freq_bucket_arr[idx]: #loop through bucket items
                    if len(res_arr) < k: #can add item to the res_arr
                        res_arr.append(item)

                    else:
                        return res_arr

            else:
                continue

        return res_arr


