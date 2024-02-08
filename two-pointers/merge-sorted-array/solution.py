"""
https://github.com/eugenechevski
https://leetcode.com/problems/merge-sorted-array
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0

        while l < m and r < n:
            if nums1[l] > nums2[r]:
                nums1[l], nums2[r] = nums2[r], nums1[l]

                # update the nums2 array
                i = r
                while i < n - 1 and nums2[i] > nums2[i + 1]:
                    nums2[i], nums2[i + 1] = nums2[i + 1], nums2[i]
                    i += 1
            l += 1

        while r < n:
            nums1[l] = nums2[r]
            l += 1
            r += 1
