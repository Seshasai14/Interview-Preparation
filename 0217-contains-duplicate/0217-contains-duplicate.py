class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashi=set()
        for i in nums:
            if i not in hashi:
                hashi.add(i)
            else:
                return True
                break
        return False

        