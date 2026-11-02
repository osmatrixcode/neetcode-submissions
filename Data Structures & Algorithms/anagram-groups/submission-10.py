class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        loop through the array
        - sort the current item
        - check if sorted word already in a DS 
        - add to the DS 
        - loop through items and add to a results arra
        """


        my_dict = {} #{sorted:[items]}
        res_arr = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in my_dict:
                my_dict[sorted_word].append(word)
            else:
                my_dict[sorted_word] = [word]

        for k, v in my_dict.items(): 
            res_arr.append(v) 

        return res_arr
        




