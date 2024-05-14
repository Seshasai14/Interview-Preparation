from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # Check if the list is empty
            return ""

        strs.sort()  # Sort the list of strings
        first_str = strs[0]
        last_str = strs[-1]
        prefix = ""
        
        # Iterate through characters of the first string and compare with the last string
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                prefix += first_str[i]
            else:
                break  # Stop if characters don't match
        
        return prefix
