"""
https://github.com/cheroke-rose
https://leetcode.com/problems/combination-sum-ii

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]

Constraints:
    * 1 <= candidates.length <= 100
    * 1 <= candidates[i] <= 50
    * 1 <= target <= 30
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def backtrack(target_sum, i):
            nonlocal res, subset, candidates, target

            if target_sum == target:
                res.append(subset[::])
                return

            if i == len(candidates) or target_sum > target:
                return

            # Inlclude in the combination
            subset.append(candidates[i])
            backtrack(target_sum + candidates[i], i + 1)
            subset.pop()

            # Do not include in the combination
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(target_sum, i + 1)

        backtrack(0, 0)

        return res
