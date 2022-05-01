class AuthenticationManager(object):
    def __init__(self, timeToLive):
        self.timeToLive = timeToLive
        self.record = collections.OrderedDict()

    def generate(self, tokenId, currentTime):
        self.removeExpire(currentTime)
        self.record[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId, currentTime):
        self.removeExpire(currentTime)
        if tokenId in self.record and self.record[tokenId] > currentTime:
            self.record[tokenId] = currentTime + self.timeToLive
            self.record.move_to_end(tokenId)

    def countUnexpiredTokens(self, currentTime):
        self.removeExpire(currentTime)
        return len(self.record)
    
    def removeExpire(self, currentTime):
        while self.record and next(iter(self.record.values())) <= currentTime:
            self.record.popitem(last=False)




# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
