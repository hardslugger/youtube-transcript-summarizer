from urllib.parse import urlparse, parse_qs

def get_youtube_video_id(youtube_url):
    """
    Extracts the video ID from a given YouTube URL.

    Args:
        youtube_url (str): The YouTube video URL.

    Returns:
        str or None: The video ID if found, otherwise None.
    """
    try:
        parsed_url = urlparse(youtube_url)
        query_params = parse_qs(parsed_url.query)

        if 'v' in query_params:
            return query_params['v'][0]
        elif 'youtu.be' in parsed_url.netloc:
            # Handle short YouTube URLs like youtu.be/VIDEO_ID
            return parsed_url.path.strip('/')
        else:
            return None
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None

# # Example usage:
# youtube_link1 = "https://www.youtube.com/watch?v=nA_Y8qkgCLc"
# youtube_link2 = "https://youtu.be/SA2iWivDJiE"
# youtube_link3 = "https://www.youtube.com/embed/SA2iWivDJiE" # Handles embed links as well

# video_id1 = get_youtube_video_id(youtube_link1)
# video_id2 = get_youtube_video_id(youtube_link2)
# video_id3 = get_youtube_video_id(youtube_link3)

# print(f"Video ID for '{youtube_link1}': {video_id1}")
# print(f"Video ID for '{youtube_link2}': {video_id2}")
# print(f"Video ID for '{youtube_link3}': {video_id3}")

# invalid_link = "https://www.google.com"
# video_id_invalid = get_youtube_video_id(invalid_link)
# print(f"Video ID for '{invalid_link}': {video_id_invalid}")