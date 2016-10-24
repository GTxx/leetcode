class Twitter(object):
    def __init__(self):
        self.users = {}
        self.id = 0

    def get_id(self):
        self.id += 1
        return self.id

    def get_or_create_user(self, userId):
        if userId not in self.users:
            self.users[userId] = {'follower': set(),
                                  'followee': set(),
                                  'feeds': [],
                                  'self_feeds': []}
        return self.users.get(userId)

    def postTweet(self, userId, tweetId):
        id = self.get_id()
        user = self.get_or_create_user(userId)
        tweet = {'user_id': userId, 'tweetId': tweetId, 'tweet_id': id}
        user['self_feeds'].append(tweet)
        for user_id in set([userId]).union(user['followee']):
            user = self.users.get(user_id)
            user['feeds'] = [tweet] + user['feeds']

    def getNewsFeed(self, userId):
        user = self.get_or_create_user(userId)
        return [tweet['tweetId'] for tweet in user['feeds'][:10]]

    def follow(self, followerId, followeeId):
        if followeeId == followerId:
            return

        follower = self.get_or_create_user(followerId)
        followee = self.get_or_create_user(followeeId)

        if followerId in followee['followee'] and followeeId in follower['follower']:
            return

        followee['followee'].add(followerId)
        follower['follower'].add(followeeId)

        follower['feeds'] += followee['self_feeds']
        follower['feeds'] = sorted(follower['feeds'], key=lambda tweet: tweet['tweet_id'], reverse=True)

    def unfollow(self, followerId, followeeId):
        if followerId == followeeId:
            return
        follower = self.get_or_create_user(followerId)
        followee = self.get_or_create_user(followeeId)
        if followerId in followee['followee']:
            followee['followee'].remove(followerId)
        if followeeId in follower['follower']:
            follower['follower'].remove(followeeId)

        # remove feeds for follower
        follower['feeds'] = [tweet for tweet in follower['feeds'] if tweet['user_id']!=followeeId]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.getNewsFeed(1)
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    twitter.getNewsFeed(1)
    twitter.unfollow(1, 2)
    twitter.getNewsFeed(1)

    twitter = Twitter()
    twitter.postTweet(1, 1)
    assert(twitter.getNewsFeed(1) == [1])
    twitter.follow(2, 1)
    assert(twitter.getNewsFeed(2) == [1])
    twitter.unfollow(2, 1)
    assert(twitter.getNewsFeed(2) == [])
