class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumSumSubarray = nums[0]
        sum_ = float('-inf')  # Renamed to sum_ to avoid overriding built-in sum function
        for i in nums:
            sum_ = max(i, sum_ + i)  # Update sum_ to the maximum of current element and (current element + sum_)
            maximumSumSubarray = max(maximumSumSubarray, sum_)  # Update maximum sum subarray
        return maximumSumSubarray

        