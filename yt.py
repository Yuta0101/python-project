import re
from pytube import YouTube
from pytube import exceptions

# 從用戶輸入中取得 YouTube 影片的連結
link = input("請貼上 YouTube 影片的連結: ")

try:
    # 用 PyTube 庫建立 YouTube 物件
    yt = YouTube(link)

    # 輸出影片的標題
    print("Title:", yt.title)

    # 輸出影片的觀看次數
    print("Views:", yt.views)

    # 選擇影片的最高解析度
    yd = yt.streams.get_highest_resolution()

    # 設定下載目錄路徑
    download_path = r"C:\Users\user\OneDrive"

    # 使用正則表達式移除標題中的非法字符
    cleaned_title = re.sub(r'[\/:*?"<>|]', '', yt.title)

    # 使用清理後的標題作為文件名下載到指定目錄
    yd.download(f"{download_path}\\{cleaned_title}.mp4")

    print("正在下載......")

except exceptions.AgeRestrictedError as e:
    print(f"Error: {e}")
    print("這個影片被限制，需要登入確認年齡。")
except Exception as e:
    print(f"Error: {e}")