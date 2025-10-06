from pytube import YouTube

def download_youtube(url, path, resolution="720p", as_audio=False, progress_callback=None):
    """
    Downloads a YouTube video.
    If as_audio=True, it downloads only the audio stream as MP4 (no conversion to MP3).
    """
    yt = YouTube(url, on_progress_callback=progress_callback)

    if as_audio:
        # Download audio-only stream (as .mp4)
        stream = yt.streams.filter(only_audio=True).first()
        if not stream:
            raise ValueError("No audio stream available")
    else:
        # Download video stream with selected resolution
        stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
        if not stream:
            raise ValueError(f"Resolution {resolution} not available")

    output = stream.download(path)
    return output
