class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            if count[num] < 2:
                result.append(num)
                count[num] += 1
        nums[:]=result
        return len(nums)
                
        