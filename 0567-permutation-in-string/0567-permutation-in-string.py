class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_hash = [0] * 26
        s2_hash = [0] * 26
        
        # Initialize character counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_hash[ord(s1[i]) - ord('a')] += 1
            s2_hash[ord(s2[i]) - ord('a')] += 1
        
        # Compare initial windows
        if s1_hash == s2_hash:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            s2_hash[ord(s2[i]) - ord('a')] += 1
            s2_hash[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            # Compare current window with s1_hash
            if s1_hash == s2_hash:
                return True
        
        return False
