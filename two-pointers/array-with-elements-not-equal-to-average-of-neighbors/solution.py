"""
https://github.com/eugenechevski
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        half = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1

        # Fill-in even indices
        ind = 0
        for i in range(half):
            res[ind] = nums[i]
            ind += 2

        # Fill-in odd indices
        ind = 1
        for i in range(half, len(nums)):
            res[ind] = nums[i]
            ind += 2

        return res
