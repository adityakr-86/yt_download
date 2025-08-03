# YouTube Video Downloader (720p)

A simple Streamlit web app to download YouTube videos in 720p MP4 format.

## Features

- Download YouTube videos in 720p resolution (MP4)
- Merges best video and audio streams
- Easy-to-use web interface
- Download button for the final video file

## Requirements

- Python 3.7+
- [ffmpeg](packages.txt)
- [streamlit](requirements.txt)
- [yt-dlp](requirements.txt)

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd yt_download
   ```

2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install ffmpeg:**
   - On Ubuntu/Debian:
     ```sh
     sudo apt-get install ffmpeg
     ```
   - On Windows:  
     Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your PATH.

## Usage

1. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

2. **Open the app in your browser** (usually at http://localhost:8501).

3. **Paste a YouTube video URL** and click "Download".

4. **Download the video** using the provided download button.

## Notes

- Downloads are saved in the `downloads/` directory.
- Only single video URLs are supported (no playlists).
- The app downloads the best available video and audio streams up to 720p and merges them into an MP4 file.

## License

MIT License

---

**Developed with [Streamlit](https://streamlit.io/)