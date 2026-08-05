class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
    edge cases
        1 item
        no items

    general solution 
        loop through each item
        sort it
        if sorted string IN dict
            then append value array with this normal item
        if sorted string NOT IN dict
            then create new entry in the dict 
        when finished, loop through the dictionary
        append each value_arr, to the results_arr 
        output results_arr
     """

        anagram_dict = {}

        for i in range(len(strs)): 
            item = strs[i]
            sorted_item = "".join(sorted(item))
            
            if sorted_item not in anagram_dict: 
                anagram_dict[sorted_item] = [item]

            else: 
                res = anagram_dict[sorted_item]
                res.append(item)
                anagram_dict[sorted_item] = res

        
        #loop through dictionary
        results_arr = []

        for k,v in anagram_dict.items(): 
            results_arr.append(v) 

        return results_arr

    