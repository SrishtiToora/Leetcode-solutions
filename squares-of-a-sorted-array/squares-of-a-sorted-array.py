class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        n=len(arr)
        left, right = 0, n - 1
        index = n - 1
        result = [0 for x in arr]

        while index >= 0:

            if abs(arr[left]) >= abs(arr[right]):
                result[index] = arr[left] * arr[left]
                left += 1
            else:
                result[index] = arr[right] * arr[right]
                right -= 1
            index -= 1
        return result