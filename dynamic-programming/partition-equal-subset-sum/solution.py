"""
https://github.com/eugenechevski
https://leetcode.com/problems/partition-equal-subset-sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
    
Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
    * 1 <= nums.length <= 200
    * 1 <= nums[i] <= 100
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If the sum of all numbers is odd
        # you cannot partition the nums evenly
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        target = sum_ // 2
        dp_set = set()
        for i in range(len(nums)):
            dp_arr = list(dp_set)

            # iterate over the current level
            for j in range(len(dp_arr)):
                if nums[i] + dp_arr[j] == target or nums[i] == target:
                    return True

                dp_set.add(nums[i] + dp_arr[j])

            dp_set.add(nums[i])

        return False