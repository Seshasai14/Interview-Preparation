from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = {}
        # Count occurrences of each element in nums
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        # Find elements with value equal to 1
        elements_with_value_1 = [key for key, value in count_dict.items() if value == 1]

        # Return the first element that appears only once
        return elements_with_value_1[0]
