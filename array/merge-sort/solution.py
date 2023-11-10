"""
https://github.com/eugenechevski
https://leetcode.com/problems/merge-sort
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge sort

        Concept:
            1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
            2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. 
               This will be the sorted list.
        """

        if len(nums) < 2:
            return nums

        # Create left and right sub-lists
        mid = len(nums) // 2

        leftSub = nums[:mid]
        rightSub = nums[mid:]

        # Sort the sublists
        self.sortArray(leftSub)
        self.sortArray(rightSub)

        # Put the sorted sub-lists
        # into the parent list
        i = j = k = 0
        while i < len(leftSub) and j < len(rightSub):
            if leftSub[i] <= rightSub[j]:
                nums[k] = leftSub[i]
                i += 1
                k += 1
            else:
                nums[k] = rightSub[j]
                j += 1
                k += 1

        # Put the leftovers to the end of the parent list

        while i < len(leftSub):
            nums[k] = leftSub[i]
            i += 1
            k += 1

        while j < len(rightSub):
            nums[k] = rightSub[j]
            j += 1
            k += 1

        return nums
