# 1st solution
class UndergroundSystem:

    def __init__(self):
        self.routes = {}
        self.records = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.records[id] = [stationName, t]
       
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.records[id][0]
        startTime = self.records[id][1]
        endStation = stationName
        deltaTime = t - startTime
        if startStation not in self.routes:
            self.routes[startStation] = {}
        route = self.routes[startStation]
        if endStation not in route:
            route[endStation] = [0, 0]
        route[endStation][0] += deltaTime
        route[endStation][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = self.routes[startStation][endStation][0]
        count = self.routes[startStation][endStation][1]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)