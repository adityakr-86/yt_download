import streamlit as st
from yt_dlp import YoutubeDL
import os

# Create output directory
output_dir = "downloads"
os.makedirs(output_dir, exist_ok=True)

# 🔹 Download Function (Works for both Videos & Shorts)
def download_youtube(url, quality="720"):
    ydl_opts = {
        'format': f'bestvideo[height<={quality}][ext=mp4]+bestaudio[ext=m4a]/best[height<={quality}]',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'merge_output_format': 'mp4',
        'quiet': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info['title'], ydl.prepare_filename(info)

# Streamlit App UI
st.title("🎬 YouTube Downloader (Videos + Shorts)")
tab1, tab2 = st.tabs(["📹 Download Video", "🎯 Download Shorts"])

# ✅ Common UI inside a function
def download_ui(tab_label):
    st.subheader(tab_label)
    url = st.text_input(f"🔗 Paste {tab_label} URL:", key=tab_label)

    if st.button(f"⬇️ Download {tab_label}", key=f"btn_{tab_label}"):
        if url:
            try:
                with st.spinner("📥 Downloading & Merging..."):
                    title, filepath = download_youtube(url)
                st.success(f"✅ Downloaded: {title}")

                # Serve the file as download
                with open(filepath, "rb") as f:
                    video_data = f.read()

                st.download_button(
                    label="💾 Save to Your Device",
                    data=video_data,
                    file_name=os.path.basename(filepath),
                    mime="video/mp4"
                )
            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please enter a valid URL")

# Tabs for Videos & Shorts
with tab1:
    download_ui("Video")

with tab2:
    download_ui("Shorts")
