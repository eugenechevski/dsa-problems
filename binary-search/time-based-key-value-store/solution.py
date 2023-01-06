"""
https://github.com/eugenechevski
https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 
Example 1:
    Input
        ["TimeMap", "set", "get", "get", "set", "get", "get"]
        [[], ["bar", "bar", 1], ["bar", 1], ["bar", 3], ["bar", "bar2", 4], ["bar", 4], ["bar", 5]]
    Output
        [null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
    TimeMap timeMap = new TimeMap();
    timeMap.set("bar", "bar", 1);  // store the key "bar" and value "bar" along with timestamp = 1.
    timeMap.get("bar", 1);         // return "bar"
    timeMap.get("bar", 3);         // return "bar", since there is no value corresponding to bar at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("bar", "bar2", 4); // store the key "bar" and value "bar2" along with timestamp = 4.
    timeMap.get("bar", 4);         // return "bar2"
    timeMap.get("bar", 5);         // return "bar2"
 

Constraints:
    * 1 <= key.length, value.length <= 100
    * key and value consist of lowercase English letters and digits.
    * 1 <= timestamp <= 107
    * All the timestamps timestamp of set are strictly increasing.
    * At most 2 * 10^5 calls will be made to set and get.
"""


class TimeMap:
    def __init__(self):
        self.map = {}
        self.prev_timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}
            self.prev_timestamps[key] = []

        self.map[key][timestamp] = value
        self.prev_timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or timestamp < self.prev_timestamps[key][0]:
            return ""

        if timestamp in self.map[key]:
            return self.map[key][timestamp]

        left = 0
        right = len(self.prev_timestamps[key]) - 1
        mid = 0

        while left <= right:
            mid = left + (right - left) // 2

            if self.prev_timestamps[key][mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return self.map[key][self.prev_timestamps[key][right]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
