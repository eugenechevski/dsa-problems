/*
    https://leetcode.com/problems/power-of-three/
    https://github.com/eugenechevski

    Given an integer n, return true if it is a power of three. Otherwise, return false.
    An integer n is a power of three, if there exists an integer x such that n == 3^x.

    Example 1:
        Input: n = 27
        Output: true

    Example 2:
        Input: n = 0
        Output: false

    Example 3:
        Input: n = 9
        Output: true

    Constraints:
        * -2^31 <= n <= 2^31 - 1

*/

/**
 * @param {number} n
 * @return {boolean}
 */
 var isPowerOfThree = function(n) {
    return n > 0 && Number.isInteger(Math.log10(n) / Math.log10(3));
    
};
