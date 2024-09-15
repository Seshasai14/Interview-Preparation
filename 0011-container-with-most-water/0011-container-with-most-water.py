from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0  
        L = 0  
        R = len(height) - 1 
        while L < R:
            currContainer = (R - L) * min(height[L], height[R])
            maxi = max(maxi, currContainer)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxi
