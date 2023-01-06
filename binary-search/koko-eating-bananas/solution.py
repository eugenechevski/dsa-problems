"""
https://github.com/eugenechevski
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours. 

Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30
    
Example 3:
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23
 
Constraints:
    * 1 <= piles.length <= 10^4
    * piles.length <= h <= 10^9
    * 1 <= piles[i] <= 10^9
"""

from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            k = min_speed + (max_speed - min_speed) // 2
            hours = 0
            for p in piles:
                hours += ceil(p / k)

            if hours > h:
                min_speed = k + 1
            elif hours <= h:
                max_speed = k

        return max_speed

