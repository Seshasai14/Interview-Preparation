class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        L=0
        charSet=set()
        for R in range(len(s)):
            if s[R] not in charSet:
                charSet.add(s[R])
                length=max(length,R-L+1)
            else:
                while s[R] in charSet:
                    charSet.remove(s[L])
                    L+=1
                charSet.add(s[R])
        return length
        