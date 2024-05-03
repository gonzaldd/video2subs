import math
import ffmpeg
from faster_whisper import WhisperModel
import os

LANG = 'es' # Change by language of the videos
WHISPER_MODEL = "base" # Modify by your hardware


def extract_audio(input_video_path, input_video_name):
    # Check if audio file already exists
    os.makedirs("created_audios", exist_ok=True)
    extracted_audio = f"created_audios/audio-{input_video_name}.mp3"
    if os.path.exists(extracted_audio):
        print(f"Audio file already exists: {extracted_audio}")
        return extracted_audio

    # Extract audio if it doesn't exist
    stream = ffmpeg.input(input_video_path)
    stream = ffmpeg.output(stream, extracted_audio, acodec="libmp3lame")
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

# ... (rest of the code remains the same)
def transcribe(audio):
    model = WhisperModel(WHISPER_MODEL)
    segments, info = model.transcribe(audio, language=LANG)
    language = info[0]
    print("Transcription language", info[0])
    segments = list(segments)
    for segment in segments:
        # print(segment)
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    return language, segments


def format_time(seconds):
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
    return formatted_time


def generate_subtitle_file(language, segments, input_video_name):
    # Create the 'created_subtitles' folder if it doesn't exist
    os.makedirs("created_subtitles", exist_ok=True)

    subtitle_file = f"created_subtitles/sub-{input_video_name}.{language}.srt"
    text = ""
    for index, segment in enumerate(segments):
        segment_start = format_time(segment.start)
        segment_end = format_time(segment.end)
        text += f"{str(index+1)} \n"
        text += f"{segment_start} --> {segment_end} \n"
        text += f"{segment.text} \n"
        text += "\n"
    f = open(subtitle_file, "w")
    f.write(text)
    f.close()
    return subtitle_file


def process_video(video_file):
    input_video_path = os.path.join("videos", video_file)
    input_video_name, _ = os.path.splitext(video_file)
    extracted_audio = extract_audio(input_video_path, input_video_name)
    language, segments = transcribe(audio=extracted_audio)
    subtitle_file = generate_subtitle_file(language, segments, input_video_name)
    print(f"Subtitles generated for {video_file}: {subtitle_file}")


def run():
    for video_file in os.listdir("videos"):
        if video_file.endswith(".mp4"):
            process_video(video_file)


run()