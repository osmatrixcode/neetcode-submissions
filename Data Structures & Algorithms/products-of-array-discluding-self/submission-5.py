class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        calculate the total product
        when reach item 'x', divide total product by x 
        add to the res array 
        - remember '0' problem in x
        - remember '0' problem when calculating total_product. 
        """

        total_product_normal = 1
        total_product_zero_case = 1
        res_arr = []
        contains_zero_flag = True
        count_zeros = 0

        #calculate total product values
        if 0 in nums:
            for num in nums: 
                if num == 0: 
                    count_zeros += 1
                    continue
                else: 
                    total_product_zero_case *= num
        else: 
            contains_zero_flag = False
            for num in nums: 
                total_product_normal *= num

        # print(total_product_zero_case)
        # print(total_product_normal)

        # multiple zeros edge case: 
        if count_zeros > 1: 
            return [0 for num in nums]
        if contains_zero_flag: 
            for num in nums: 
                if num == 0: 
                    res_arr.append(total_product_zero_case)
                else: 
                    res_arr.append(0)

        else: 
            for num in nums: 
                calculation = int(total_product_normal / num)
                res_arr.append(calculation) 

        return res_arr

            


            






