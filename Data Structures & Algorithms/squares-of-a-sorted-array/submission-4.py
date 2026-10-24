class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for pos in range(n - 1, -1, -1):           # fill from the back: largest first
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1                           # the left value is used, move inward
            else:
                result[pos] = nums[right] ** 2
                right -= 1                          # the right value is used, move inward
        return result