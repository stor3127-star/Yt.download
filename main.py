import flet as ft
import os
from yt_dlp import YoutubeDL

def main(page: ft.Page):
    page.title = "YouTube Загрузчик"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    url_input = ft.TextField(label="Вставь ссылку на видео с YouTube", width=400)
    status_text = ft.Text(value="", color=ft.colors.GREEN)
    
    def download_click(e):
        url = url_input.value.strip()
        if not url:
            status_text.value = "❌ Ошибка: Ссылка пустая!"
            status_text.color = ft.colors.RED
            page.update()
            return
        
        status_text.value = "⏳ Подключение и скачивание... Подождите."
        status_text.color = ft.colors.YELLOW
        page.update()
        
        try:
            download_path = "/sdcard/Download/"
            ydl_opts = {
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'format': 'best',
                'noplaylist': True,
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            status_text.value = "🎉 Готово! Видео сохранено в 'Загрузки'!"
            status_text.color = ft.colors.GREEN
            url_input.value = ""
        except Exception as ex:
            status_text.value = f"❌ Ошибка: {str(ex)}"
            status_text.color = ft.colors.RED
            
        page.update()

    download_button = ft.ElevatedButton("Скачать видео", on_click=download_click)

    page.add(
        ft.Text("🎥 YT Video Downloader", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        url_input,
        download_button,
        status_text
    )

ft.app(target=main)
