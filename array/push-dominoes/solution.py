"""
https://github.com/eugenechevski
https://leetcode.com/problems/push-dominoes
"""

from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
            The idea is to isolate regions of standing dominoes and assign forces
            that are coming from either or both ends.
        """
        # Create the list of dominoes
        result = [*dominoes]

        def assignForces(leftForce, rightForce, left, right):
            # Assign respective forces from both ends
            if leftForce == 'R' and rightForce == 'L':
                while left < right:
                    result[left] = 'R'
                    result[right] = 'L'
                    left += 1
                    right -= 1

            # Just from left
            if leftForce == 'R' and rightForce == '.':
                while left <= right:
                    result[left] = 'R'
                    left += 1

            # Just from right
            if leftForce == '.' and rightForce == 'L':
                while left <= right:
                    result[right] = 'L'
                    right -= 1

        i = 0
        while i < len(result):
            if result[i] == '.':
                leftForce = 'R' if i > 0 and result[i - 1] == 'R' else '.'

                # Find the right force
                j = i + 1
                rightForce = '.'
                while j < len(result):
                    if result[j] != '.':
                        rightForce = 'L' if result[j] == 'L' else '.'
                        break
                    j += 1

                # Save for next iteraton
                nextStep = j
                j -= 1

                # Assign forces
                if leftForce != rightForce:
                    assignForces(leftForce, rightForce, i, j)

                # Start the next iteration
                i = nextStep - 1
            i += 1

        return self.queueSolution(dominoes)

    def queueSolution(self, dominoes):
        doms = list(dominoes)
        q = deque()

        def knockRight(i):
            if i + 1 < len(doms) and doms[i + 1] == '.':
                if i + 2 < len(doms) and doms[i + 2] == 'L':
                    q.popleft()
                else:
                    q.append((i + 1, 'R'))
                    doms[i + 1] = 'R'

        # Build the queue by adding only pushed dominoes
        for i, dom in enumerate(doms):
            if dom != '.':
                q.append((i, dom))

        # Simulate the falling second by second
        while q:
            i, dom = q.popleft()

            # Knock the standing dominoe from the left
            if dom == 'L' and i > 0 and doms[i - 1] == '.':
                q.append((i - 1, 'L'))
                doms[i - 1] = 'L'

            # Knock the standing dominoe from the right unless there's
            # the left standing dominoe after it
            if dom == 'R':
                knockRight(i)

        return ''.join(doms)
