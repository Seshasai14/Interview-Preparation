class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        newList = list(filter(None, x))
        k=newList[-1]
        return len(k)
        
        