from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from twitter_utils import get_latest_tweet_url
from downloader import download_twitter_video
from health_check import start_health_check

bot = Client("twitter_video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Send me a Twitter username (without @) and I'll get their latest video!")

@bot.on_message(filters.text & ~filters.command("start"))
async def fetch_video(client, message):
    username = message.text.strip().lstrip("@")
    await message.reply(f"Searching latest video tweet from @{username}...")
    
    tweet_url = get_latest_tweet_url(username)
    if not tweet_url:
        return await message.reply("No video tweet found or profile is private.")
    
    video_path = download_twitter_video(tweet_url)
    if not video_path:
        return await message.reply("Failed to download the video.")
    
    await message.reply_video(video_path)


# 🔰 Run the Bot
if __name__ == "__main__":
    threading.Thread(target=start_health_check, daemon=True).start()
    bot.run()
