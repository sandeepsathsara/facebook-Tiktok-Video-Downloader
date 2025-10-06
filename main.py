import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
import threading
from youtube_downloader import download_youtube
from tiktok_downloader import download_tiktok

def select_folder():
    path = filedialog.askdirectory()
    folder_var.set(path)

def download_youtube_thread():
    url = url_entry.get()
    path = folder_var.get()
    resolution = res_var.get()
    as_audio = audio_var.get()
    try:
        download_youtube(url, path, resolution, as_audio)
        messagebox.showinfo("Success", "YouTube Download Completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def download_tiktok_thread():
    url = url_entry.get()
    path = folder_var.get()
    try:
        download_tiktok(url, path)
        messagebox.showinfo("Success", "TikTok Download Completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = ThemedTk(theme="arc")
root.title("TikTok & YouTube Downloader")
root.geometry("500x400")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Video URL:", font=("Arial", 12)).pack(pady=5)
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

tk.Label(root, text="Save Folder:", font=("Arial", 12)).pack(pady=5)
folder_var = tk.StringVar()
tk.Entry(root, textvariable=folder_var, width=40).pack(side="left", padx=10)
ttk.Button(root, text="Browse", command=select_folder).pack(side="left")

tk.Label(root, text="Resolution:", font=("Arial", 12)).pack(pady=10)
res_var = tk.StringVar(value="720p")
ttk.OptionMenu(root, res_var, "1080p", "720p", "480p", "360p").pack()

audio_var = tk.BooleanVar()
ttk.Checkbutton(root, text="Download as MP3", variable=audio_var).pack(pady=10)

ttk.Button(root, text="Download YouTube", width=25, command=lambda: threading.Thread(target=download_youtube_thread).start()).pack(pady=10)
ttk.Button(root, text="Download TikTok", width=25, command=lambda: threading.Thread(target=download_tiktok_thread).start()).pack(pady=10)

root.mainloop()
