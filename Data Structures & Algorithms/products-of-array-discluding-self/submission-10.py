class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        calculate total product
        - count number of zeros
            no zeros, 1 zero, many zeros edge case
        - loop through array and append to res_arr the product_except_self
        """

        count_zeros = 0
        total_product = 1
        total_product_edge_case = 1
        res_arr = []

        for num in nums: 
            if num == 0: 
                count_zeros += 1
                continue
            else:
                total_product *= num

        if count_zeros == 1: 
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


        elif count_zeros == 0:
            for num in nums: 
                calculation = int(total_product / num)
                res_arr.append(calculation)


        else: 
            return [0 for _ in range(len(nums))]

        return res_arr

        
        