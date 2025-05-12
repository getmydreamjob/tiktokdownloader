import streamlit as st
from yt_dlp import YoutubeDL
import os

# Setup
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="YouTube & TikTok Downloader", layout="centered")
st.title("🎬 YouTube & TikTok Downloader")
st.markdown("Paste a **YouTube** or **TikTok** link below to download the video (audio+video in MP4).")

url = st.text_input("📥 Video URL", placeholder="https://www.tiktok.com/@...")

if st.button("Download"):
    if url.strip():
        st.info("Downloading... please wait ⏳")

        ydl_opts = {
            'format': 'mp4',  # ⚠️ restrict to formats with audio+video
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # ensure merged output is MP4
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'  # Final container format
            }],
            'quiet': True
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

                # Ensure the file exists
                if os.path.exists(filename):
                    st.success("✅ Download completed!")
                    with open(filename, "rb") as f:
                        st.download_button(
                            label="📥 Click to download",
                            data=f,
                            file_name=os.path.basename(filename),
                            mime="video/mp4"
                        )
                else:
                    st.error("❌ Video not saved. Try a different link or platform.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter a valid video URL.")
