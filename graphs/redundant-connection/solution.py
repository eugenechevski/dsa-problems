"""
https://github.com/eugenechevski
https://leetcode.com/problems/redundant-connection

In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]

Example 2:
    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]

Constraints:
    * n == edges.length
    * 3 <= n <= 1000
    * edges[i].length == 2
    * 1 <= ai < bi <= edges.length
    * ai != bi
    * There are no repeated edges.
    * The given graph is connected.
"""


class Solution:
    def unionFindApproach(self, edges):
        """
            The following code solves the problem with the Union Find algorithm in the most efficient way.
        """

        parent = [i for i in range(len(edges) + 1)]
        ranks = [0] * (len(edges) + 1)

        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node

        def union(node1, node2):
            if ranks[node1] >= ranks[node2]:
                parent[node2] = node1
                ranks[node1] += 1
            else:
                parent[node1] = node2
                ranks[node2] += 1


        for i in range(len(edges)):
            node1, node2 = edges[i]
            parent1, parent2 = find(node1), find(node2)

            # Cycle detected
            if parent1 == parent2:
                return [node1, node2]
            else:
                union(parent1, parent2)

        return []
    
    def findRedundantConnection(self, edges):
        # Build the graph
        graph = {}
        for n1, n2 in edges:
            if n1 not in graph:
                graph[n1] = set()
            graph[n1].add(n2)

            if n2 not in graph:
                graph[n2] = set()
            graph[n2].add(n1)

        visited = set()

        def dfs(current, target):
            nonlocal graph, visited

            if current in visited:
                return False

            if target in graph[current]:
                return True

            visited.add(current)
            for neighbor in graph[current]:
                if dfs(neighbor, target):
                    return True

            visited.remove(current)

            return False

        for i in range(len(edges) - 1, -1, -1):
            n1, n2 = edges[i]

            # Remove the connection
            graph[n1].remove(n2)
            graph[n2].remove(n1)

            if dfs(n1, n2):
                return [n1, n2]
            else:
                # Restore the connection
                graph[n1].add(n2)
                graph[n2].add(n1)

        return []
