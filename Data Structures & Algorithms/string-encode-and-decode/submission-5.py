class Solution:



    def encode(self, strs: List[str]) -> str:
        """
        add length of string + a delimitter + string to output
        """
        output_str = ""
        for word in strs: 
            output_str += str(len(word)) + "#" + word
            
        return output_str



    def decode(self, s: str) -> List[str]:

        i = 0
        res_arr = []

        while i < len(s): 
            j = i

            while s[j] != "#":
                j+=1

            len_word = int(s[i:j])
            word = s[j+1:j+len_word+1]
            res_arr.append(word)

            i = j + len_word + 1

        return res_arr

  

            
