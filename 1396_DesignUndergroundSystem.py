# 1st solution
class UndergroundSystem:

    def __init__(self):
        self.records = {}
        self.pairs = Counter()
        self.freqs = Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.records[id] = [stationName, t]
       
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.records.pop(id)
        deltaTime = t - startTime
        pair = (startStation, stationName)
        self.pairs[pair] += deltaTime
        self.freqs[pair] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        pair = (startStation, endStation)
        totalTime = self.pairs[pair]
        count = self.freqs[pair]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)