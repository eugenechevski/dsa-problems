/*
    github.com/eugenechevski

    Given an integer n and an integer start.
    Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
    Return the bitwise XOR of all elements of nums.

    Example:
        Input: n = 4, start = 3
        Output: 8
        Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

    Constraints:
        * 1 <= n <= 1000
        * 0 <= start <= 1000
        * n == nums.length
*/

/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
 var xorOperation = function(n, start) {
    let result = 0;

    for (let i = 0; i < n; i++) {
        result = result ^ (start + 2 * i);
        
    }

    return result;
};
