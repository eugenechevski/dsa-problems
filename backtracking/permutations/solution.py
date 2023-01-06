"""
https://leetcode.com/problems/permutations/
https://github.com/eugenechevski

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
    * 1 <= nums.length <= 6
    * -10 <= nums[i] <= 10
    * All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        chosen = set()  # indices of the chosen elements

        def dfs():
            nonlocal nums, res, subset, chosen

            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if i not in chosen:
                    subset.append(nums[i])
                    chosen.add(i)
                    dfs()
                    subset.pop()
                    chosen.remove(i)

        dfs()

        return res
