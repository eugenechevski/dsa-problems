"""
https://github.com/eugenechevski
https://leetcode.com/problems/removde-duplicates-from-sorted-array
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max_n = float('-inf')
        for n in nums:
            max_n = max(max_n, n)

        l, r = 0, 1
        while r < len(nums):
            if nums[l] < nums[r]:
                nums[l + 1], nums[r] = nums[r], nums[l + 1]
                l += 1

                if nums[l] == max_n:
                    break
            r += 1

        return l + 1
