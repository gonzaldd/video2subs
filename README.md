
# Video2Subs

This Python script automates the process of generating subtitles for videos using the Whisper speech recognition model.



## Prerequisites

To run this script, you will need:

- **Python 3.9+:** Ensure you have Python 3.9 or a later version installed. You can download it from the [official Python website](https://www.python.org/).
## Run Locally

Put your videos in videos folder. 

Clone the project

```bash
  git clone git@github.com:gonzaldd/video2subs.git
```

Go to the project directory

```bash
  cd video2subs
```

Create env

```bash
  python3 -m venv env
```

Activate env

```bash
  source env/bin/activate
```

Install dependencies

```bash
  pip3 install faster-whisper ffmpeg-python
```

Run the script

```bash
  python3 main.py
```


The subtitles will create in created_subtitles folder


## Demo

![](https://github.com/gonzaldd/video2subs/blob/main/media/demo.gif)

