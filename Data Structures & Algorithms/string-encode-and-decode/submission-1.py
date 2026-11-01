class Solution:



    def encode(self, strs: List[str]) -> str:
        """
        use number sign and a delimitter 
        """
        output_str = ""
        for word in strs: 
            length = len(word)
            output_str += str(length) + "#" + word

        return output_str
        




    def decode(self, s: str) -> List[str]:
        res_arr = []
        i = 0

        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            string = s[j + 1 : j + 1 + size]
            res_arr.append(string) 
            i = j + 1 + size

        return res_arr



            
