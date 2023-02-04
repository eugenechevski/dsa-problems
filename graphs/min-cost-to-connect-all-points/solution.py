"""
https://github.com/eugenechevski
https://leetcode.com/problems/min-cost-to-connect-all-points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. 
All points are connected if there is exactly one simple path between any two points.

* 1 <= points.length <= 1000
* -10^6 <= xi, yi <= 10^6
* All pairs (xi, yi) are distinct.
"""

class Solution(object):
    def minCostConnectPoints(self, points):
        if len(points) == 1:
            return 0

        parents = [i for i in range(len(points))]
        ranks = [0] * len(points)

        def getWeight(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        def find(node):
            root = node
            while parents[root] != root:
                root = parents[root]

            return root

        def union(node1, node2):
            if ranks[node1] >= ranks[node2]:
                parents[node2] = parents[node1]
                ranks[node1] += 1
            else:
                parents[node1] = parents[node2]
                ranks[node2] += 1
                
        # Create edges
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                edges.append([getWeight(points[i], points[j]), i, j])

        # Sort
        edges.sort(key=lambda a: a[0])

        # Connect nodes
        minCost = 0
        for edge in edges:
            weight, node1, node2 = edge
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 != parent2:
                minCost += weight
                union(parent1, parent2)

        return minCost

