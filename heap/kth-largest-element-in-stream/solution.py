"""
https://github.com/eugenechevski
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    * KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    * int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Constraints:
    * 1 <= k <= 10^4
    * 0 <= nums.length <= 10^4
    * -10^4 <= nums[i] <= 10^4
    * -10^4 <= val <= 10^4
    * At most 10^4 calls will be made to add.
    * It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""


from collections import deque
import heapq


# O(log n)
def heapify(arr, i):
    size = len(arr)
    smallest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < size and arr[left] < arr[smallest]:
        smallest = left
    if right < size and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest)

# O(n log n)


def build_minheap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i)

# O(n log n)


def insert(arr, val):
    size = len(arr)
    arr.append(val)

    if size != 0:
        build_minheap(arr)

# O(n log n)


def popmin(arr):
    if len(arr) > 0:
        arr.popleft()
        build_minheap(arr)


class NativeImplementation:
    """
        1. Build the min heap out of the given array
        2. Remove a minimum value from the heap until the size becomes equal to k
        3. Add a new value to the heap and return the minimum element
    """

    # O(n^2)
    def __init__(self, k, nums):
        self.k = k
        self.heap = deque(nums)

        build_minheap(self.heap)

        while len(self.heap) > k:
            popmin(self.heap)

    # O(n log n)
    def add(self, val):
        insert(self.heap, val)

        if len(self.heap) > self.k:
            popmin(self.heap)

        return self.heap[0]

# Optimized solution to pass the last case with the Python's library


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


sol = KthLargest(3, [4, 5, 8, 2])
