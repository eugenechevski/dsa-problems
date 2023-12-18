"""
https://github.com/eugenechevski
https://leetcode.com/problems/largest-number
"""

import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: int, b: int):
            "Comparing logic of two numbers"
            a_str = str(a)
            b_str = str(b)

            if int(a_str + b_str) > int(b_str + a_str):
                return -1

            if int(a_str + b_str) < int(b_str + a_str):
                return 1

            return 0

        # Sort the numbers
        nums.sort(key=functools.cmp_to_key(compare))

        # Build the number
        result = ""
        for n in nums:
            result += str(n)

        return "0" if result.startswith("0") else result
