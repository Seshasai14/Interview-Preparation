class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in dicti:
                return [dicti[complement],i]
            dicti[num]=i
        return []
        