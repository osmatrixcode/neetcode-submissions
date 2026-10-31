class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        calculate total product of all nums in the array
        track how many zeros
        - no,1,many zeros 
        loop through the nums, calculate the value, and input into the results array
        """

        zero_counter = 0
        total_product = 1
        total_product_edge_case = 1
        res_arr = []

        #build variables
        for num in nums: 
            if num == 0:
                zero_counter+=1
            else:
                total_product*=num

        if zero_counter > 1: 
            return [0 for _ in range(len(nums))]

        #one 0 in the array (edge)
        if zero_counter == 1: 
            for num in nums: 
                if num == 0: 
                    continue
                else:
                    total_product_edge_case *= num

            for num in nums: 
                if num == 0: 
                    res_arr.append(total_product_edge_case) 
                else:
                    res_arr.append(0)

        # no zeros in array 
        else: 
            for num in nums: 
                res_arr.append(int(total_product/num))

        return res_arr


        



        
        