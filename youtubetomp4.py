from pytube import YouTube

def download_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if video:
        video.download(output_path)
        print("Téléchargement terminé.")
    else:
        print("Aucune vidéo disponible avec une qualité MP4.")

if __name__ == "__main__":
    video_url = input("Entrez l'URL de la vidéo YouTube : ")
    output_directory = input("Entrez le chemin de sortie pour le téléchargement : ")
    download_video(video_url, output_directory)
