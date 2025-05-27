import snscrape.modules.twitter as sntwitter

def get_latest_tweet_url(username):
    for tweet in sntwitter.TwitterUserScraper(username).get_items():
        if tweet.media:
            for media in tweet.media:
                if media.type == 'video' or media.type == 'animated_gif':
                    return f"https://twitter.com/{username}/status/{tweet.id}"
        break  # Only check the latest tweet
    return None
