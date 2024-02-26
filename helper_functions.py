from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import requests
from io import BytesIO
import random
import re
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip, CompositeAudioClip, concatenate_audioclips
from moviepy.video.VideoClip import ImageClip
from services.video import Video
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import multiprocessing

W, H = 1080, 1920


def text_to_image(text, output_image_path, font_size=72, max_width=1272, font_path="Hind-Light.ttf"):
    # Initialize image with a white background
    # Initial height is 0, will be updated dynamically
    image_size = (max_width, 0)
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        font_path, font_size) if font_path else ImageFont.load_default()

    # Split the text into lines based on max_width
    lines = []
    words = text.split()
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + " " + word
        text_width, _ = draw.textsize(test_line, font)

        if text_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    # Calculate the total text height and update image size
    total_text_height = sum(font.getsize(line)[1] for line in lines)
    image_size = (max_width, total_text_height)
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Draw the lines on the image
    y_position = 0
    for line in lines:
        text_width, text_height = draw.textsize(line, font)
        x_position = (max_width - text_width) // 2
        draw.text((x_position, y_position), line, fill="black", font=font)
        y_position += text_height

    image.save(output_image_path)


def resize_image(width, filename):
    base_width = width
    img = Image.open(filename)

    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))

    # Use Image.LANCZOS for resampling
    img = img.resize((base_width, h_size), Image.LANCZOS)
    img.save(filename)


def save_image_from_url(url, path):
    max_width = 1272
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(path)
        resize_image(max_width, path)
        print('Image saved successfully.')
    else:
        print('Failed to download image. Status code:', response.status_code)


def get_start_and_end_times(video_length: int, length_of_clip: int):
    random_time = random.randrange(
        0, int(length_of_clip) - int(video_length))

    return random_time, random_time + video_length


def chop_background_video(
    video_length: int,
    screen_objects: dict
):
    length = video_length
    background = VideoFileClip(
        f"common/Futuristic.mp4")

    start_time, end_time = get_start_and_end_times(
        video_length, background.duration
    )
    try:
        ffmpeg_extract_subclip(
            f"common/Futuristic.mp4",
            start_time,
            end_time,
            targetname=f"results/temp/{screen_objects['thread_id']}/background.mp4",
        )
    except (OSError, IOError):
        with VideoFileClip(f"common/Futuristic.mp4") as video:
            new = video.subclip(start_time, end_time)
            new.write_videofile(
                f"results/temp/{screen_objects['thread_id']}/background.mp4")


def make_final_video_new(
    length: int,
    screen_objects: dict
):
    VideoFileClip.reW = lambda clip: clip.resize(width=W)
    VideoFileClip.reH = lambda clip: clip.resize(width=H)
    opacity = 1.0
    transition = 0
    background_clip = (
        VideoFileClip(
            f"results/temp/{screen_objects['thread_id']}/background.mp4")
        .without_audio()
        .resize(height=H)
        .crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)
    )

    # Gather all audio clips
    audio_clips = [AudioFileClip(
        f"results/temp/{screen_objects['thread_id']}/0.mp3")]
    audio_concat = concatenate_audioclips(audio_clips)
    audio_composite = CompositeAudioClip([audio_concat])

    # add title to video
    image_clips = []
    # Gather all images
    new_opacity = 1 if opacity is None or float(
        opacity) >= 1 else float(opacity)
    new_transition = (
        0 if transition is None or float(
            transition) > 2 else float(transition)
    )
    image_clips.insert(
        0,
        ImageClip(f"results/temp/{screen_objects['thread_id']}/final.png")
        .set_duration(audio_clips[0].duration)
        .resize(width=W - 100)
        .set_opacity(new_opacity),
    )

    img_clip_pos = "center"

    image_concat = concatenate_videoclips(image_clips).set_position(
        img_clip_pos
    )
    image_concat.audio = audio_composite
    final = CompositeVideoClip([background_clip, image_concat])
    final = Video(final).add_watermark(
        text=f"Background credit: sid",
        opacity=0,
        redditid=screen_objects['thread_id'],
        duration=length,
    )

    final.write_videofile(
        f"results/temp/{screen_objects['thread_id']}/temp.mp4",
        fps=30,
        audio_codec="aac",
        audio_bitrate="192k",
        verbose=False,
        threads=multiprocessing.cpu_count(),
    )
    ffmpeg_extract_subclip(
        f"results/temp/{screen_objects['thread_id']}/temp.mp4",
        0,
        length,
        targetname=f"output/{screen_objects['thread_id']}.mp4",
    )
