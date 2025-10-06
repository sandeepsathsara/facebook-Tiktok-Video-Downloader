import requests

def download_tiktok(url, path, filename="tiktok_video.mp4"):
    # For simplicity, direct video download (may need TikTokApi for watermark-free)
    response = requests.get(url)
    if response.status_code == 200:
        full_path = f"{path}/{filename}"
        with open(full_path, "wb") as f:
            f.write(response.content)
        return full_path
    else:
        raise ValueError("Failed to download TikTok video")
