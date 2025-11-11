import yt_dlp

def get_youtube_metadata(url):
    try:
        ydl_opts = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title"),
                "channel": info.get("uploader")
            }
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return None

