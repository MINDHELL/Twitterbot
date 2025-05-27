import re
import snscrape.modules.twitter as sntwitter

def is_valid_twitter_username(username):
    return re.match(r"^[A-Za-z0-9_]{1,15}$", username) is not None

def get_latest_tweet_url(username):
    if not is_valid_twitter_username(username):
        raise ValueError("Invalid Twitter username format")
    
    for tweet in sntwitter.TwitterUserScraper(username).get_items():
        if tweet.media:
            for media in tweet.media:
                if media.type == 'video' or media.type == 'animated_gif':
                    return f"https://twitter.com/{username}/status/{tweet.id}"
        break  # Only check the latest tweet
    return None
