# 1st solution
class TimeMap:

    def __init__(self):
        self.dic = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = {'time': [], 'value': []}
        dic = self.dic[key]
        idx = bisect.bisect_left(dic["time"], timestamp)
        dic["time"].insert(idx, timestamp)
        dic["value"].insert(idx, value)      
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        dic = self.dic[key]
        idx = bisect.bisect_right(dic["time"], timestamp) - 1
        if idx < 0:
            return ""
        return dic["value"][idx]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)