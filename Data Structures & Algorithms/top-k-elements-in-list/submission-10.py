class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create DS that tracks num: frequency
        create DS that idx represents frequency, 
            DS item will be an arr that contains all nums with that freq
        loop decrement over DS_2 and fill results arr until k is met 

        """


        count_dict = {} #{num: freq}

        for num in nums: 
            count_dict[num] = count_dict.get(num,0)+1

        freq_arr = [[] for _ in range(len(nums)+1)]
        # print(count_dict)
        # print(freq_arr)

        for key,v in count_dict.items(): 
            freq_arr[v].append(key)

        # print(freq_arr)

        res_arr = []
        for i in range(len(freq_arr)-1,0,-1): 
            bucket = freq_arr[i]
            if bucket != []: #check not an empty bucket: 
                for num in bucket: #loop through each item in a bucket
                    if len(res_arr) < k: # can add to the res array
                        res_arr.append(num) 
            else:
                continue

        return res_arr




