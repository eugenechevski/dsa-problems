"""
https://github.com/cherokee-rose
https://leetcode.com/problems/course-schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
    * 1 <= numCourses <= 2000
    * 0 <= prerequisites.length <= 5000
    * prerequisites[i].length == 2
    * 0 <= ai, bi < numCourses
    * All the pairs prerequisites[i] are unique.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        graph = {}
        # Build the dependency graph
        for dep in prerequisites:
            if dep[0] not in graph:
                graph[dep[0]] = []
            graph[dep[0]].append(dep[1])

        path = set()  # stores the current search path
        validated = set()  # stores the global search history

        def dfs(course):
            nonlocal path, graph, validated

            if course in path:
                return False
            
            if course in validated:
                return True

            res = True
            path.add(course)
            if course in graph:
                # Check all prerequisites of the course
                for val in graph[course]:
                    if not dfs(val):
                        res = False
                        break
                    
            if res:
                validated.add(course)
            path.remove(course)

            return res

        # Check all courses
        for key in graph.keys():
            if not dfs(key):
                return False

        return True