"""
https://github.com/eugenechevski
https://leetcode.com/problems/insert-delete-getrandom-o(1)
"""

from random import randint


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.map = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.arr.append(val)
        self.map[val] = self.size
        if self.size < len(self.arr):  # in case where there're deleted elements
            self.arr[-1] = self.arr[self.size]
            self.arr[self.size] = val

        self.size += 1

        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            # Get indices
            removedIndex = self.map[val]
            lastIndex = self.size - 1

            # Update the map
            self.map[self.arr[lastIndex]] = removedIndex
            del self.map[val]

            # Update the array
            self.arr[removedIndex] = self.arr[lastIndex]
            self.arr[lastIndex] = val
            self.size -= 1

            return True

        return False

    def getRandom(self) -> int:
        return self.arr[randint(0, self.size - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
