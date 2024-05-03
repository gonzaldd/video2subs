# Video2Subs

This Python script automates the process of generating subtitles for videos using the Whisper speech recognition model.

## Prerequisites

To run this script, you will need:

- **Python 3.9+:** Ensure you have Python 3.9 or a later version installed. You can download it from the [official Python website](https://www.python.org/).
- **venv:** A virtual environment is recommended to isolate the project's dependencies. You can learn how to create and use virtual environments [here](https://docs.python.org/3/library/venv.html).
- **FFmpeg:** This is used for audio extraction from videos. You can download FFmpeg from the [official website](https://ffmpeg.org/).
- **Create folder "videos"** and put inside the videos to create subs.

## Instalation

```bash
python3 -m venv env
source env/bin/activate
pip3 install faster-whisper ffmpeg-python
```
