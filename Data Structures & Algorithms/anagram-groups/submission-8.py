class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        loop through each word in strs: 
        sort the current word
        store in dict: {sorted_word: [word1,word2,etc...]}
        loop through each value in the dict,
        -output in an arr, the sorted words
        """

        sorted_dict = {} #{sorted_word: [word1,word2,etc...]}
        res_arr = []

        for word in strs: 
            sorted_word = "".join(sorted(word)) 
            if sorted_word in sorted_dict:
                sorted_dict[sorted_word].append(word)
            else: 
                sorted_dict[sorted_word] = [word]

        for v in sorted_dict.values(): 
            res_arr.append(v)

        return res_arr
