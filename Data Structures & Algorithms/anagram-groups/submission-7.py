class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        loop through words in strs. 
            - each word: 
                - sort it (string build) 
            - fill in a dict {sorted_word:[word1,word2,etc...]}
        loop through values in dict 
            - save all 'v' in a results arr
            - output results
        """


        my_dict = {}
        res_arr = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in my_dict: 
                my_dict[sorted_word].append(word)
            else:
                my_dict[sorted_word] = [word]

        for k,v in my_dict.items(): 
            res_arr.append(v) 

        return res_arr
