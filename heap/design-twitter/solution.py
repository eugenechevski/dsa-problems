"""
https://github.com/eugenechevski
https://leetcode.com/problems/design-twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
    * Twitter() Initializes your twitter object.
    * void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
    * List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
    * void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
    * void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Example 1:
    Input
    ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    Output
    [null, null, [5], null, null, [6, 5], null, [5]]

Explanation
    Twitter twitter = new Twitter();
    twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2);    // User 1 follows user 2.
    twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2);  // User 1 unfollows user 2.
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

Constraints:
    * 1 <= userId, followerId, followeeId <= 500
    * 0 <= tweetId <= 10^4
    * All the tweets have unique IDs.
    * At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""

import heapq


class User:
    def __init__(self):
        self.following = {}
        self.feed = []
        self.tweets = []

    # O(log n)
    def post(self, tweetId, time_stamp):
        heapq.heappush(self.tweets, (time_stamp * -1, tweetId))

    # O(1)
    def followUser(self, userId, user):
        self.following[userId] = user

    # O(1)
    def unfollowUser(self, userId):
        if userId in self.following:
            del self.following[userId]

    # O(m log n)
    def updateFeed(self):
        self.feed.clear()
        self.feed = list(self.tweets)

        for user in self.following.values():
            for tweet in user.tweets:
                heapq.heappush(self.feed, tweet)


class Twitter:
    def __init__(self):
        self.users = {}
        self.time_stamp = 0

    # O(log n)
    def postTweet(self, userId, tweetId):
        if userId not in self.users:
            self.users[userId] = User()

        self.users[userId].post(tweetId, self.time_stamp)
        self.time_stamp += 1

    # O(m log n)
    def getNewsFeed(self, userId):
        if userId in self.users:
            self.users[userId].updateFeed()
        else:
            self.users[userId] = User()

        feed = self.users[userId].feed
        result = []
        while len(feed) > 0 and len(result) < 10:
            result.append(heapq.heappop(feed)[1])

        return result

    # O(1)
    def follow(self, followerId, followeeId):
        follower = None
        followee = None

        if followerId in self.users:
            follower = self.users[followerId]
        else:
            follower = User()
            self.users[followerId] = follower

        if followeeId in self.users:
            followee = self.users[followeeId]
        else:
            followee = User()
            self.users[followeeId] = followee

        follower.followUser(followeeId, followee)

    # O(1)
    def unfollow(self, followerId, followeeId):
        self.users[followerId].unfollowUser(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
