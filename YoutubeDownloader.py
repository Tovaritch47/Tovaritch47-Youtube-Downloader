import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

class YoutubeDownloaderGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tovaritch YouTube Downloader")

        # Create labels and entry fields
        self.url_label = tk.Label(self.root, text="Enter YouTube URL:")
        self.url_entry = tk.Entry(self.root, width=150)
        self.save_label = tk.Label(self.root, text="Select save location:")
        self.save_entry = tk.Entry(self.root, width=150)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)

        # Create radio buttons to select download type
        self.var = tk.StringVar(value="video")
        self.radio1 = tk.Radiobutton(self.root, text="Video", variable=self.var, value="video")
        self.radio2 = tk.Radiobutton(self.root, text="Audio", variable=self.var, value="audio")

        # Create download button
        self.download_button = tk.Button(self.root, text="Download", command=self.download)

        # Pack widgets
        self.url_label.pack()
        self.url_entry.pack()
        self.save_label.pack()
        self.save_entry.pack()
        self.browse_button.pack()
        self.radio1.pack()
        self.radio2.pack()
        self.download_button.pack()

        # Start GUI
        self.root.mainloop()

    def browse_file(self):
        # Open file dialog to select save location
        save_location = filedialog.askdirectory()
        self.save_entry.delete(0, tk.END)
        self.save_entry.insert(0, save_location)

    def download(self):
        # Get YouTube video URL and save location
        url = self.url_entry.get()
        save_location = self.save_entry.get()

        # Check if URL and save location are valid
        if not url or not save_location:
            tk.messagebox.showerror("Error", "Please enter a valid URL and save location.")
            return

        try:
            # Download YouTube video or audio based on radio button selection
            yt = YouTube(url)
            if self.var.get() == "video":
                stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
            else:
                stream = yt.streams.filter(only_audio=True).first()
            stream.download(save_location)

            # Show success message
            tk.messagebox.showinfo("Success", "Download complete!")
        except Exception as e:
            # Show error message
            tk.messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    YoutubeDownloaderGUI()
