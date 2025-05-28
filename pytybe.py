from pytube import Playlist, YouTube
from pytube.cli import on_progress
import os
from typing import Optional


def download_video(video: YouTube, folder: str, index: int) -> None:
    """Скачивает видео в наилучшем качестве и сохраняет его с кастомным именем."""
    try:
        video.register_on_progress_callback(on_progress)
        stream = video.streams.get_highest_resolution()
        downloaded_path = stream.download(output_path=folder)

        # Переименование файла
        new_name = f"{folder}/Tutorial {index + 1} - {video.title}.mp4"
        os.rename(downloaded_path, new_name)
        print(f"✅ Скачано: {video.title}")
    except Exception as e:
        print(f"❌ Ошибка при скачивании {video.title}: {e}")


def download_playlist(playlist_url: str) -> None:
    """Основная функция: скачивает весь плейлист по ссылке."""
    try:
        playlist = Playlist(playlist_url)
        folder_name = playlist.title.strip().replace(" ", "_")
        os.makedirs(folder_name, exist_ok=True)

        print(f"🎬 Загружаем плейлист: {playlist.title}")
        for idx, video in enumerate(playlist.videos):
            download_video(video, folder_name, idx)
    except Exception as e:
        print(f"⚠️ Не удалось загрузить плейлист: {e}")


if __name__ == "__main__":
    url = input("🔗 Введите ссылку на плейлист YouTube: ").strip()
    download_playlist(url)
