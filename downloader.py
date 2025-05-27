import yt_dlp

def download_twitter_video(url):
    output_path = "downloads/%(id)s.%(ext)s"
    ydl_opts = {
        "outtmpl": output_path,
        "format": "bestvideo+bestaudio/best",
        "quiet": True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print("Download error:", e)
        return None
