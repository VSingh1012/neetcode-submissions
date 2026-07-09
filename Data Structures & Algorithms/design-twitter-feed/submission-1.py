class Twitter:

    def __init__(self):
        self.followingMap = defaultdict(set) # whoever bro IS following
        self.tweetMap = defaultdict(list)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1 # for the max heap variant
        self.tweetMap[userId].append((self.count, tweetId))


        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetList = []
        res = []

        following = self.followingMap[userId]
        tweetList += self.tweetMap[userId]

        if following:
            for follower in following:
               tweetList += self.tweetMap[follower] 
        

        
        heapq.heapify(tweetList) # O(nlog(n))

        while tweetList and len(res) < 10:
            res.append(heapq.heappop(tweetList)[1])

        return res

        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followingMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)        
