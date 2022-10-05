"""
https://github.com/cherokee-rose
https://leetcode.com/problems/last-stone-weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. 
The result of this smash is:
    * If x == y, both stones are destroyed, and
    * If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
import heapq


class Solution:
    def lastStoneWeight(self, stones):
        heap = list(map(lambda x: x * -1, stones))
        heapq.heapify(heap)  # O(n log n)

        while len(heap) > 1:  # O(n)
            y = heapq.heappop(heap)  # O(n log n)
            x = heapq.heappop(heap)  # O(n log n)

            if x != y:
                heapq.heappush(heap, -1 * (abs(y) - abs(x)))  # O(n log n)

        return abs(heap[0]) if len(heap) == 1 else 0
