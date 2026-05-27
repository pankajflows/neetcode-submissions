class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append((self.count, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        # get followers including the user
        people = [userId]
        for c in self.following[userId]:
            people.append(c)

        # for all the people, get last tweets and feed into a heap
        # feed in max-heap like this (time, tweetId, index_from_back, userId)
        heap = list()
        for p in people:
            if p in self.tweets and self.tweets[p]:
                last_idx = len(self.tweets[p]) - 1
                time, tweetId = self.tweets[p][last_idx]
                heap.append((time, tweetId, last_idx, p))
        heapq.heapify(heap)

        # run a loop over heap
        # pop one item at a time
        # just after popping get the next tweet for the same user and insert into the heap
        # repeat untill you have 10 tweets
        top_ten = list()
        while heap and len(top_ten) < 10:
            time, tweetId, idx, p_id = heapq.heappop(heap)
            top_ten.append(tweetId)

            if idx > 0:
                next_idx = idx - 1
                next_time, next_tweetId = self.tweets[p_id][next_idx]
                heapq.heappush(heap, (next_time, next_tweetId, next_idx, p_id))


        # return 10 tweets
        return top_ten


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        
