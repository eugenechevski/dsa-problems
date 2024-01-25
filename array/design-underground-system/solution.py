"""
https://github.com/eugenechevski
https://leetcode.com/problems/design-underground-system
"""


class UndergroundSystem:
    def __init__(self):
        self.checkedIn = {}  # customer_id -> [station, t]
        self.trips = {}  # station_A -> station_B -> [total_time, trip_count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedIn:
            # Check-in the customer
            self.checkedIn[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedIn:
            # Check-out the customer and update the trips
            startStation, startTime = self.checkedIn[id]
            del self.checkedIn[id]

            if startStation not in self.trips:
                self.trips[startStation] = {}
            if stationName not in self.trips[startStation]:
                self.trips[startStation][stationName] = [t - startTime, 1]
            else:
                self.trips[startStation][stationName][0] += (t - startTime)
                self.trips[startStation][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation not in self.trips or endStation not in self.trips[startStation]:
            return 0.0

        return self.trips[startStation][endStation][0] / self.trips[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
