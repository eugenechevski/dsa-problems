"""
https://github.com/eugenechevski
https://leetcode.com/problems/4sum
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, len(nums)):
                if j - 1 > i and nums[j - 1] == nums[j]:
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]

                    if fourSum < target:
                        l += 1
                    elif fourSum > target:
                        r -= 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1

        return result
