class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:(i+l)]:
                return i
                break
        return -1

