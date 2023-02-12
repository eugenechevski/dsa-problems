"""
https://github.com/eugenechevski
https://leetcode.com/problems/network-delay-time

You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

Constraints:
  * 1 <= k <= n <= 100
  * 1 <= times.length <= 6000
  * times[i].length == 3
  * 1 <= ui, vi <= n
  * ui != vi
  * 0 <= wi <= 100
  * All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

class Solution:
    def getMinDistanceNode(self, dist, visited, n):
        """
            Finds a node with a minimum distance at the current state.
        """

        minDist = 1e7
        minNode = -1

        for node in range(n):
            if dist[node] < minDist and visited[node] == False:
                minDist = dist[node]
                minNode = node

        return minNode

    def dijkstra(self, graph, n, src):
        """
            Computes the minimum shortest paths to each node in the graph
            from a given source node using the Dijkstra's algorithm.
        """

        dist = [1e7] * n  # a resulting array
        visited = [False] * n  # a tracker for visited nodes
        dist[src] = 0

        for _ in range(n):
            u = self.getMinDistanceNode(dist, visited, n)
            visited[u] = True

            for v in range(n):
                # No connection
                if graph[u][v] == -1:
                    continue

                newDist = dist[u] + graph[u][v]
                if newDist < dist[v]:
                    dist[v] = newDist

        return dist

    def networkDelayTime(self, times, n, k):
        # Building the graph
        # using the adjacency matrix
        graph = [[-1 for col in range(n)] for row in range(n)]
        for a, b, weight in times:
            graph[a - 1][b - 1] = weight

        # Get the shortest paths array
        shortestPaths = self.dijkstra(graph, n, k - 1)
        print(graph)
        print(shortestPaths)

        # Find the minimum time for a signal to reach all nodes
        # by taking the maximum value from the array above
        result = -1
        for i in range(n):
            result = max(result, shortestPaths[i])

        return result if result != 1e7 else -1
