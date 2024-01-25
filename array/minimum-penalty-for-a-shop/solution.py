"""
https://github.com/eugenechevski
https://leetcode.com/problems/minimum-penalty-for-a-shop
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        preOpened = [0]

        for c in customers:
            preOpened.append(0)
            preOpened[-1] += preOpened[-2]
            if c == 'N':
                preOpened[-1] += 1

        preClosed = [0]
        for c in customers[::-1]:
            preClosed.append(0)
            preClosed[-1] += preClosed[-2]
            if c == 'Y':
                preClosed[-1] += 1

        minPenalty, time = len(customers), len(customers)
        for i in range(len(customers) + 1):
            current = 0
            current += preOpened[i]
            current += preClosed[len(customers) - i]

            if current < minPenalty:
                minPenalty = current
                time = i

        return time
