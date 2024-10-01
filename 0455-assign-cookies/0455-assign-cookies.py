class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l, r, count = 0, 0, 0
        g = sorted(g)
        s = sorted(s)

        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                count += 1
                l += 1
                r += 1
            else:
                r += 1
        return count
        