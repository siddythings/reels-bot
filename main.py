from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import random
import re
import json
from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from gateway import Gateway


from services.factory import ServiceProviderFactory

VIDEOS_TO_UPLOAD = open('videos_to_upload.json')
val = json.load(VIDEOS_TO_UPLOAD)

utility = Gateway(ServiceProviderFactory.get_provider("INC42"))
screen_objects_all = utility.get_posts(1)
for screen_objects in screen_objects_all:
    utility.get_images(screen_objects)
    length, number_of_comments = utility.create_audio(screen_objects)
    utility.create_video(length, screen_objects)
    with open('videos_to_upload.json', 'w', encoding='utf-8') as f:
        json.dump(val+[screen_objects], f, ensure_ascii=False, indent=4)
# print(screen_objects)
