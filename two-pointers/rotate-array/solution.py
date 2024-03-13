"""
https://github.com/eugenechevski
https://leetcode.com/problems/rotate-array
"""


class Solution:
    def rotate(self, nums, k):
        self.reverseRotate(nums, k)
        # self.cyclicRotate(nums, k)
        return

    def reverseRotate(self, nums, k):
        """
            The idea is to reverse the entire array and then reverse the first k elements
            and the last n - k elements. The result will be the rotated array.
        """

        k = k % len(nums)
        # Reverse the entire array
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Reverse the first k elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Reverse the last n - k elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def cyclicRotate(self, nums, k):
        """
            The idea is to put an element into its final position and then
            take the initial element at that position and transfer it too. Continuing
            this shifting until we hit the inital starting position of our first element.
            In total the number of shifts we make should match the length of the array.
        """
        i = 0
        shifts = len(nums)
        dist = k % len(nums)
        start = i  # keep track of the initial jump
        curr = nums[i]  # tracks previous element to be inserted
        while shifts > 0:
            shifts -= 1
            next_i = (i + dist) % len(nums)  # next jumping position
            curr, nums[next_i] = nums[next_i], curr  # swap

            if next_i == start:  # Hit the cycle
                start += 1
                if start == len(nums):
                    break

                i = start
                curr = nums[i]
                continue
            else:
                i = next_i
