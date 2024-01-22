"""
https://github.com/eugenechevski
https://leetcode.com/problems/number-of-zero-filled-subarrays
"""


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        i = 0
        while i < len(nums):
            # Start counting
            if nums[i] == 0:
                count = 0
                while i < len(nums) and nums[i] == 0:
                    count += 1
                    i += 1
                result += (count * (count + 1)) // 2
            else:
                i += 1

        return result
