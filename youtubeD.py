import flet as ft
from pytube import YouTube
from time import sleep
import os

def main(page : ft.Page):
    #Page Title and aligment
    page.title = "YouTube Video Downloader"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    Intro = ft.Stack(
            [
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            "Youtube Video Downloader",
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                foreground=ft.Paint(
                                    color=ft.colors.BLUE_700,
                                    stroke_width=6,
                                    stroke_join=ft.StrokeJoin.ROUND,
                                    style=ft.PaintingStyle.STROKE,
                                ),
                            ),
                        ),
                    ],
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            "Youtube Video Downloader",
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.GREY_300,
                            ),
                        ),
                    ],
                ),
            ]
        )

    url = ft.TextField(hint_text="Insert URL", autofocus= True)
    submit = ft.ElevatedButton(
        height= 55, text= "Download Video", icon="ARROW_DOWNWARD"                        
    )
    submit_Audio = ft.ElevatedButton(
        height= 55, text= "Download Audio", icon="ARROW_DOWNWARD"
    )

    #Progress Bar method
    def ProgressBar(e):
        pb = ft.ProgressBar(width=1300, visible= False)
        down = ft.Column([ft.Text("Downloading...")])
        page.add(pb, down)
        
        #Loop for load bar
        for i in range(0, 15):
            pb.visible = True
            pb.value = i * 0.07
            sleep(0.1)
            page.update()
            
        pb.visible= False
        down.visible= False
        page.update()   

    #Button Method
    def btn_click_Video(e):
        ProgressBar(e)
        page.update()
        current_folder = os.getcwd()
        yt = YouTube(url.value)
        video = yt.streams.get_highest_resolution()
        video.download(output_path = current_folder)

    def dropdown_menu_Audio(e):
        ProgressBar(e)
        page.update()
        current_folder = os.getcwd()
        yt = YouTube(url.value)
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path = current_folder)

    #performing button action
    submit.on_click = btn_click_Video
    submit_Audio.on_click = dropdown_menu_Audio
    page.add(Intro, url, submit, submit_Audio)
    
ft.app(target=main)
