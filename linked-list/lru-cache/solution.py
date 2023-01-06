"""
https://github.com/eugenechevski
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. 
    Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    
The functions get and put must each run in O(1) average time complexity.

Example 1:
    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    
Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4

Constraints:
    * 1 <= capacity <= 3000
    * 0 <= key <= 10^4
    * 0 <= value <= 10^5
    * At most 2 * 10^5 calls will be made to get and put.
"""

"""
The implementation of LRU Cache with Linked List and Hash Table.
All operations are run in O(1) time complexity.
"""


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


class DoublyNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.dblist = DoublyLinkedList()
        self.map = {}

    """
    Moves a node to the head of the list
    """

    def _bubble(self, key: int) -> None:
        # Move to the head only when there are at least two nodes
        # and the node is not at the head already
        if self.size == 1 or self.map[key] == self.dblist.head:
            return

        node = self.map[key]

        # update the tail
        if node == self.dblist.tail:
            self.dblist.tail = node.prev

        # change pointers
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        node.next = self.dblist.head
        node.prev = None
        self.dblist.head.prev = node
        self.dblist.head = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        # update the priority
        self._bubble(key)

        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        # The node already exists
        if key in self.map:
            self.map[key].val = value
            self._bubble(key)
        else:
            # Create the node
            new_node = DoublyNode(key, value)
            self.map[key] = new_node
            self.size += 1

            # Move to the head
            self._bubble(key)

            # Validate the size
            if self.size == 1:
                self.dblist.head = new_node
                self.dblist.tail = new_node
            elif self.size > self.capacity:  # Eviction of the tail
                tail = self.dblist.tail
                tail.prev.next = None
                self.dblist.tail = tail.prev
                self.size -= 1
                del self.map[tail.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
