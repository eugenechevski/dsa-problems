""" 
  
  https://githib.com/eugenechevski
  https://leetcode.com/problems/maximum-product-subarray/

  Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
  and return the product.

  The test cases are generated so that the answer will fit in a 32-bit integer.
  A subarray is a contiguous subsequence of the array.

  Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

  Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    
  Constraints:
    * 1 <= nums.length <= 2 * 104
    * -10 <= nums[i] <= 10
    * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_products = [nums[0]]
        min_products = [nums[0]]
        global_max = nums[0]

        for i in range(1, len(nums)):
            max_products.append(0)
            min_products.append(0)

            max_products[i] = max(nums[i], max(nums[i] * max_products[i - 1], nums[i] * min_products[i - 1]))
            min_products[i] = min(nums[i], min(nums[i] * max_products[i - 1], nums[i] * min_products[i - 1]))
            global_max = max(global_max, max_products[i])

        return global_max        