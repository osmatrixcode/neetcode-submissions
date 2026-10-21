class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        loop trhough array, 
        each item, sort it. 
        if sorted in dict, append to value array 
        else, create new dict key value pair. 

        output all v in the array 
        """

        my_dict = {} #{sorted_word: [word1,word2,etc...]}
        res = []

        for i in range(len(strs)): 
            word = strs[i]
            sorted_word = str.join("",sorted(word))

            if sorted_word not in my_dict: 
                my_dict[sorted_word] = [word]
            else: 
                my_dict[sorted_word].append(word)

        #output results
        for k,v in my_dict.items(): 
            res.append(v) 

        return res