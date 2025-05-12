import streamlit as st
from yt_dlp import YoutubeDL
import os

# Set up downloads directory
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

st.title("🎬 YouTube & TikTok Downloader")
st.markdown("Paste a YouTube or TikTok link below to download the video:")

url = st.text_input("Video URL")

if st.button("Download"):
    if url:
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'noplaylist': True,
            'quiet': True
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                st.success("✅ Download completed!")
                st.markdown(f"[Click to download]({filename})")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter a valid video URL.")
