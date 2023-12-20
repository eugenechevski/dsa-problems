"""
https://github.com/eugenechevski
https://leetcode.com/problems/continuous-subarray-sum
"""

from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # If the list has less than 2 elements, return False
        if len(nums) < 2:
            return False

        # Calculate the prefix sum for the first two elements
        prefix = nums[0] + nums[1]

        # If the prefix sum is divisible by k, return True
        if prefix % k == 0:
            return True

        # Initialize a dictionary to store the remainders and their indices
        remains = defaultdict(list)
        # Store the remainder of the first element
        remains[nums[0] % k].append(0)
        # Store the remainder of the prefix sum of the first two elements
        remains[prefix % k].append(1)

        # Iterate over the rest of the list
        for i in range(2, len(nums)):
            prefix += nums[i]  # Update the prefix sum
            rem = prefix % k  # Calculate the remainder

            # If the remainder is 0 or it is already in the dictionary and the difference
            # between the current index and the smallest index associated with this remainder is greater than 1, return True
            if rem == 0 or (rem in remains and i - remains[rem][0] > 1):
                return True

            # If the remainder is not in the dictionary, add it
            remains[rem].append(i)

        # If no subarray is found, return False
        return False
