from pytube import YouTube

def download_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if video:
        video.download(output_path)
        print("Download Completed")
    else:
        print("Video not found")

if __name__ == "__main__":
    video_url = input("Enter the YouTube URL :")
    output_directory = input("Enter the the desired file location :")
    download_video(video_url, output_directory)
