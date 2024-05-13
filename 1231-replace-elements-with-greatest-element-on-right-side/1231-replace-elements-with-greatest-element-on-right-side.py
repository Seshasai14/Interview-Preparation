class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1
        for i in range(n - 1, -1, -1):
            current_value = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current_value)
        arr[-1] = -1
        return arr
        