"""
https://github.com/eugenechevski
https://leetcode.com/problems/reconstruct-itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. 
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". 
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
    Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]
    
Example 2:
    Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
  * 1 <= tickets.length <= 300
  * tickets[i].length == 2
  * from[i].length == 3
  * to[i].length == 3
  * from[i] and toi consist of uppercase English letters.
  * from[i] != to[i]
"""


class Solution(object):
    def findItinerary(self, tickets):
        # Build the map
        connections = defaultdict(deque)
        tickets.sort()
        for ticket in tickets:
            departFrom, arriveTo = ticket
            connections[departFrom].append(arriveTo)

        inOrder = ['JFK']
        def dfs(current):
            if len(inOrder) == len(tickets) + 1:
                return True
            if current not in connections:
                return False

            temp = list(connections[current]) # A snapshot
            for nextArrival in temp:
                connections[current].popleft()
                inOrder.append(nextArrival)

                if dfs(nextArrival): # Check if the combination is valid
                    return True
                
                # Nope, continue searching
                connections[current].append(nextArrival)
                inOrder.pop()

        dfs('JFK')

        return inOrder
