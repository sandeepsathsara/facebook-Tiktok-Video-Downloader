import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
from youtube_downloader import download_youtube
from tiktok_downloader import download_tiktok

# ---------- Functions ----------
def select_folder():
    path = filedialog.askdirectory()
    folder_var.set(path)

def youtube_download_thread():
    url = url_entry.get()
    path = folder_var.get()
    res = res_var.get()
    audio = audio_var.get()
    if not url or not path:
        messagebox.showerror("Error", "Please enter URL and select folder")
        return
    try:
        progress_label.configure(text="Downloading YouTube...")
        download_youtube(url, path, resolution=res, as_audio=audio)
        progress_label.configure(text="✅ YouTube Download Completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        progress_label.configure(text="❌ Error!")

def tiktok_download_thread():
    url = url_entry.get()
    path = folder_var.get()
    if not url or not path:
        messagebox.showerror("Error", "Please enter URL and select folder")
        return
    try:
        progress_label.configure(text="Downloading TikTok...")
        download_tiktok(url, path)
        progress_label.configure(text="✅ TikTok Download Completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        progress_label.configure(text="❌ Error!")

# ---------- GUI ----------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")  # green accent

app = ctk.CTk()
app.geometry("600x450")
app.title("🎬 Modern TikTok & YouTube Downloader")
app.resizable(False, False)

folder_var = ctk.StringVar()
res_var = ctk.StringVar(value="720p")
audio_var = ctk.BooleanVar()

# ---------- Title ----------
title = ctk.CTkLabel(app, text="🌟 Video Downloader", font=ctk.CTkFont(size=24, weight="bold"))
title.pack(pady=(20,10))

# ---------- URL ----------
ctk.CTkLabel(app, text="Video URL:", font=ctk.CTkFont(size=14)).pack(pady=(10,5))
url_entry = ctk.CTkEntry(app, width=500, height=35, font=ctk.CTkFont(size=14))
url_entry.pack(pady=(0,10))

# ---------- Save Folder ----------
ctk.CTkLabel(app, text="Save Folder:", font=ctk.CTkFont(size=14)).pack(pady=(5,5))
frame_folder = ctk.CTkFrame(app)
frame_folder.pack(pady=(0,10))
folder_entry = ctk.CTkEntry(frame_folder, textvariable=folder_var, width=350, height=30)
folder_entry.pack(side="left", padx=5, pady=5)
ctk.CTkButton(frame_folder, text="Browse", command=select_folder, width=100, height=30, fg_color="#FF9900",
              hover_color="#FFB84D").pack(side="left", padx=5)

# ---------- YouTube Options ----------
ctk.CTkLabel(app, text="Resolution (YouTube):", font=ctk.CTkFont(size=14)).pack(pady=(5,5))
res_option = ctk.CTkOptionMenu(app, values=["1080p","720p","480p","360p"], variable=res_var, width=150, dropdown_hover_color="#33CCFF")
res_option.pack(pady=(0,10))

ctk.CTkCheckBox(app, text="Download as MP3 (Audio Only)", variable=audio_var).pack(pady=(0,15))

# ---------- Buttons ----------
button_frame = ctk.CTkFrame(app, fg_color="#1E1E2F")
button_frame.pack(pady=(5,15), fill="x")

ctk.CTkButton(button_frame, text="🎥 Download YouTube", command=lambda: threading.Thread(target=youtube_download_thread).start(),
              width=250, height=40, fg_color="#33CCFF", hover_color="#66DDFF", corner_radius=12).pack(side="left", padx=20, pady=10)
ctk.CTkButton(button_frame, text="🎵 Download TikTok", command=lambda: threading.Thread(target=tiktok_download_thread).start(),
              width=250, height=40, fg_color="#FF3399", hover_color="#FF66B3", corner_radius=12).pack(side="left", padx=20, pady=10)

# ---------- Progress Label ----------
progress_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
progress_label.pack(pady=15)

# ---------- Footer ----------
footer = ctk.CTkLabel(app, text="Created by Sathsara Sandeep | 2025", font=ctk.CTkFont(size=10), text_color="#AAAAAA")
footer.pack(side="bottom", pady=10)

app.mainloop()
