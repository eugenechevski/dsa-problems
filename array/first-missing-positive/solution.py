"""
https://github.com/eugenechevski
https://leetcode.com/problems/first-missing-positive
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Cycle sort
        # Swap elements until nums[i] == i + 1
        for i in range(len(nums)):
            # We only care about positive numbers and those that are
            # less than the size of the array
            while (
                nums[i] != i + 1 and  # mismatch
                nums[i] > 0 and  # negatives
                nums[i] <= len(nums) and  # in the range
                nums[i] != nums[nums[i] - 1]  # duplicates
            ):
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp

        result = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result = i + 1
                break

        return result
