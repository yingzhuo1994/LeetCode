class Twitter:
    def __init__(self):
        self.followers = defaultdict(set)
        self.followees = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        lines = {}

        if len(self.userTweets[userId]) > 0:
            lines[userId] = len(self.userTweets[userId]) - 1

        for followeeId in self.followees[userId]:
            lines[followeeId] = len(self.userTweets[followeeId]) - 1

        while len(tweets) < 10 and lines:
            curUser = 0
            curTime = 0
            for id in list(lines.keys()):
                if lines[id] < 0:
                    lines.pop(id)
                else:
                    print(lines[id])
                    if self.userTweets[id][lines[id]][0] < curTime:
                        curTime = self.userTweets[id][lines[id]][0]
                        curUser = id

            if curTime < 0:
                tweet = self.userTweets[curUser][lines[curUser]][1]
                lines[curUser] -= 1
                tweets.append(tweet)
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].add(followerId)
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)