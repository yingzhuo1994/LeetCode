# 1st solution
class FrequencyTracker:

    def __init__(self):
        self.count = {}
        self.frequency = {}

    def add(self, number: int) -> None:
        self.count[number] = self.count.get(number, 0) + 1
        freq = self.count[number]
        self.frequency[freq] = self.frequency.get(freq, 0) + 1
        freq -= 1
        if freq > 0 and freq in self.frequency:
            self.frequency[freq] -= 1

    def deleteOne(self, number: int) -> None:
        if self.count.get(number, 0) <= 0:
            return
        freq = self.count[number]
        self.count[number] -= 1
        self.frequency[freq] -= 1
        freq -= 1
        if freq > 0:
            self.frequency[freq] = self.frequency.get(freq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency.get(frequency, 0) > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)