"""
https://github.com/eugenechevski
https://leetcode.com/problems/-minimum-difference-between-highest-and-lowest-of-k-scores
"""


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        min_diff = float('+inf')

        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff
