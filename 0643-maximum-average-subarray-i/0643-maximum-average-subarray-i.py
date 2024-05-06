from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k == 1:
            return max(nums)
        
        # Calculate the sum of the first subarray of length k
        sum_window = sum(nums[:k])
        max_avg = sum_window / k  # Initialize max_avg with the average of the first subarray
        
        # Iterate over the rest of the subarrays
        for i in range(1, n - k + 1):
            # Update the sum by subtracting the first element of the previous subarray
            # and adding the next element
            sum_window = sum_window - nums[i - 1] + nums[i + k - 1]
            
            # Calculate the average of the current subarray
            avg = sum_window / k
            
            # Update max_avg if necessary
            max_avg = max(max_avg, avg)
        
        return max_avg
