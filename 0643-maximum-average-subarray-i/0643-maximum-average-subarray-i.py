class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L=0
        windowSum=sum(nums[:k])
        maxAvg,avg=windowSum/k,0
        for R in range(k,len(nums)):
            windowSum+=nums[R]-nums[L]
            maxAvg=max(windowSum/k,maxAvg)
            L+=1
        return maxAvg



        