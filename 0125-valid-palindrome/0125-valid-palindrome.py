class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        text = re.sub(r'[^a-z0-9]', '', text)
        L=0
        R=len(text)-1
        while L<R:
            if text[L]!=text[R]:
                return False
            else:
                L+=1
                R-=1
        return True

        