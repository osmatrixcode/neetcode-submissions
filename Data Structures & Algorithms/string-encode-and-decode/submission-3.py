class Solution:



    def encode(self, strs: List[str]) -> str:
        """
        add a number that is length of word
        add a hashtag to separate it
        """
        output_str = ""
        for word in strs: 
            output_str += str(len(word)) + "#" + word

        return output_str



    def decode(self, s: str) -> List[str]:

        res_arr = []
        i = 0

        while i < len(s): 
            j = i
            
            while s[j] != "#":
                j+=1
            
            size = int(s[i:j])

            word = s[j+1 : j + size + 1]
            res_arr.append(word) 
            i = j + size + 1
        return res_arr



            
