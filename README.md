# YouTube Transcript Downloader

A simple Python script to download subtitles (transcript) from a YouTube video and save them to a text file.

## Requirements

- Python 3.x
- `youtube-transcript-api` library

### Install dependencies

```bash
pip install youtube-transcript-api
```

## Usage

1. Clone the repo : `git clone https://github.com/squach90/pythonYoutubeTranscript.git` 
2. Run the script in your terminal : `python main.py`
3. Enter the YouTube video URL when prompted
4. If subtitles are available, they will be saved to `transcript.txt`

### Example

```bash
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Subtitles saved to 'transcript.txt'
```
```

#### Notes

- The script only works if the video has subtitles (manual or auto-generated).
- If the URL is invalid or no subtitles are available, an error will be displayed.
```
```
