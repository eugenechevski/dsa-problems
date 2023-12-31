"""
http://github.com/eugenechevski
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    
Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
    
Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
    * 1 <= s.length <= 2 * 10^5
    * s consists only of printable ASCII characters.
"""

from asyncio import constants


class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                formatted += ch.lower()

        left, right = 0, len(formatted) - 1
        while True:
            if left >= right:
                break
                
            if formatted[left] != formatted[right]:
                return False
                
            left += 1
            right -= 1
            
        return left >= right
