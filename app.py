import streamlit as st
from yt_dlp import YoutubeDL
import os

# Set up download folder
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="YouTube & TikTok Downloader", layout="centered")

st.title("🎬 YouTube & TikTok Downloader")
st.markdown("Paste a **YouTube** or **TikTok** video link below to download the video in MP4 format.")

url = st.text_input("📥 Video URL", placeholder="https://www.youtube.com/watch?v=... or TikTok link")

if st.button("Download"):
    if url.strip():
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

                with open(filename, "rb") as file:
                    st.download_button(
                        label="📥 Click to download video",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="video/mp4"
                    )

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter a valid video URL.")
