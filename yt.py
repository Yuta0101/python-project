import re
import os
from pytube import YouTube, exceptions
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, messagebox, filedialog
from tkinter import ttk
from urllib.parse import urlparse, parse_qs

def clean_youtube_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if 'v' in query_params:
        video_id = query_params['v'][0]
        base_url = f"https://www.youtube.com/watch?v={video_id}"
    else:
        base_url = f"https://{parsed_url.netloc}{parsed_url.path}"
    return base_url

def download_youtube_video(link, download_path, file_format, resolution):
    try:
        clean_link = clean_youtube_url(link)
        yt = YouTube(clean_link)
        print("已成功建立 YouTube 物件")
        print("影片標題:", yt.title)
        print("觀看次數:", yt.views)

        if resolution == 'Highest':
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.filter(file_extension=file_format, res=resolution).first()

        if not stream:
            messagebox.showerror("錯誤", f"找不到解析度為 {resolution} 的 {file_format} 格式")
            return

        cleaned_title = re.sub(r'[\/:*?"<>|]', '', yt.title)
        file_path = os.path.join(download_path, f"{cleaned_title}.{file_format}")
        stream.download(output_path=download_path, filename=f"{cleaned_title}.{file_format}")
        messagebox.showinfo("成功", f"下載成功！影片已保存至: {file_path}")

    except exceptions.AgeRestrictedError:
        messagebox.showerror("錯誤", "這個影片被限制，需要登入確認年齡。")
    except exceptions.VideoUnavailable:
        messagebox.showerror("錯誤", "這個影片不可用。")
    except exceptions.RegexMatchError:
        messagebox.showerror("錯誤", "連結格式不正確。請確認您輸入的連結。")
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤: {e}")

def start_download():
    link = url_entry.get()
    download_path = path_entry.get()
    file_format = format_var.get()
    resolution = resolution_var.get()
    if not link or not download_path:
        messagebox.showerror("錯誤", "請提供有效的 YouTube 連結和下載路徑")
        return
    download_youtube_video(link, download_path, file_format, resolution)

def browse_directory():
    directory = filedialog.askdirectory()
    path_entry.set(directory)

# 創建主窗口
root = Tk()
root.title("YouTube 影片下載器")
root.geometry("600x300")
root.configure(bg="#e0f7fa")

# 使用 ttk 模組來改進外觀
style = ttk.Style()
style.configure("TLabel", background="#e0f7fa", font=("Arial", 12))
style.configure("TButton", background="#0078D7", foreground="black", font=("Arial", 12, "bold"))
style.configure("TEntry", font=("Arial", 12))
style.configure("TOptionMenu", font=("Arial", 12))

# 創建 GUI 元件
ttk.Label(root, text="YouTube 連結:").grid(row=0, column=0, padx=10, pady=10, sticky="W")
url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

ttk.Label(root, text="下載路徑:").grid(row=1, column=0, padx=10, pady=10, sticky="W")
path_entry = StringVar()
ttk.Entry(root, textvariable=path_entry, width=50).grid(row=1, column=1, padx=10, pady=10, columnspan=2)
ttk.Button(root, text="瀏覽", command=browse_directory).grid(row=1, column=3, padx=10, pady=10)

ttk.Label(root, text="格式:").grid(row=2, column=0, padx=10, pady=10, sticky="W")
format_var = StringVar(value="mp4")
ttk.OptionMenu(root, format_var, "mp4", "mp4", "webm").grid(row=2, column=1, padx=10, pady=10, sticky="W")

ttk.Label(root, text="解析度:").grid(row=3, column=0, padx=10, pady=10, sticky="W")
resolution_var = StringVar(value="Highest")
ttk.OptionMenu(root, resolution_var, "Highest", "Highest", "1080p", "720p", "480p", "360p").grid(row=3, column=1, padx=10, pady=10, sticky="W")

ttk.Button(root, text="下載", command=start_download).grid(row=4, column=1, padx=10, pady=20, columnspan=2)

# 運行主循環
root.mainloop()
