"""
https://github.com/eugenechevski
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition
"""


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        count = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                count += 1 << (r - l)
                l += 1

        return count % (10 ** 9 + 7)
