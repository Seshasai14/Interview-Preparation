from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        result = []
        p_hash = [0] * 26
        s_hash = [0] * 26

        # Initialize the character count for p and the first window of s
        for i in range(len(p)):
            p_hash[ord(p[i]) - ord('a')] += 1
            s_hash[ord(s[i]) - ord('a')] += 1
        
        # Compare the first window
        if p_hash == s_hash:
            result.append(0)

        # Slide the window across the string s
        for i in range(len(p), len(s)):
            s_hash[ord(s[i]) - ord('a')] += 1
            s_hash[ord(s[i - len(p)]) - ord('a')] -= 1

            # If the hashes match, it means we found an anagram
            if p_hash == s_hash:
                result.append(i - len(p) + 1)

        return result
