"""
https://github.com/eugenechevski
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            # Count repeated contigous numbers
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1

            # Replace all
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            r += 1

        return l
