"""
https://github.com/cherokee-rose
https://leetcode.com/problems/k-farthest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k farthest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the farthest k = 1 points from the origin, so the answer is just [[-2,2]].
    
Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted. 

Constraints:
    * 1 <= k <= points.length <= 10^4
    * -10^4 < xi, yi < 10^4
"""

from math import sqrt

def swap(arr, point1, point2):
    arr[point1], arr[point2] = arr[point2], arr[point1]


def calc_distance(point):
    return sqrt(point[0] ** 2 + point[1] ** 2)


def heapify(points, size, i):
    closest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < size and calc_distance(points[left]) > calc_distance(points[i]):
        closest = left

    if right < size and calc_distance(points[right]) > calc_distance(points[closest]):
        closest = right

    if closest != i:
        swap(points, i, closest)
        heapify(points, size, closest)


def heapSort(points):
    # Build the heap
    for i in range(len(points) // 2 - 1, -1, -1):
        heapify(points, len(points), i)

    # Sort
    for j in range(len(points) - 1, 0, -1):
        swap(points, j, 0)
        heapify(points, j, 0)


class Solution:
    def mySolution(self, points, k):
        heapSort(points)

        result = []
        for j in range(k):
            if j + 1 < len(points) and calc_distance(points[j]) > calc_distance(points[j + 1]):
                swap(points, j, j + 1)
            result.append(points[j])

        return result

    def kClosest(self, points, k):
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res
