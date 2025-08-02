import streamlit as st
from yt_dlp import YoutubeDL
import os

output_dir = "downloads"
os.makedirs(output_dir, exist_ok=True)

def download_video_720p(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'merge_output_format': 'mp4',
        'quiet': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info['title'], ydl.prepare_filename(info)

st.title("🎬 YouTube Video Downloader (720p)")
url = st.text_input("📎 Paste YouTube Video URL:")

if st.button("Download"):
    if url:
        try:
            with st.spinner("📥 Downloading & Merging..."):
                title, filepath = download_video_720p(url)
            st.success(f"✅ Downloaded: {title}")
            
            # Read file content in binary
            with open(filepath, "rb") as f:
                video_data = f.read()

            # Show download button
            st.download_button(
                label="⬇️ Click to Download Video",
                data=video_data,
                file_name=os.path.basename(filepath),
                mime="video/mp4"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid URL")
