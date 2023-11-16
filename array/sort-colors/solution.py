"""
https://github.com/eugenechevski
https://leetcode.com/problems/sort-colors
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.dutch(nums)

    def dutch(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

    def countSort(self, nums):
        # Counts of colors
        reds, whites, blues = 0, 0, 0

        # Perform the count
        for n in nums:
            if n == 0:
                reds += 1

            if n == 1:
                whites += 1

            if n == 2:
                blues += 1

        # Override the array
        i = 0
        while reds > 0:
            nums[i] = 0
            i += 1
            reds -= 1
        while whites > 0:
            nums[i] = 1
            i += 1
            whites -= 1
        while blues > 0:
            nums[i] = 2
            i += 1
            blues -= 1
