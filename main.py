import shutil
import pyautogui
import time
from io import BytesIO
from PIL import Image
from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, ViewportSize
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import random
import re
import json
from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from gateway import Gateway
from helper_functions import *
import requests

from services.factory import ServiceProviderFactory


# utility = Gateway(ServiceProviderFactory.get_provider("INC42"))
# screen_objects_all = utility.get_posts(1)
# for screen_objects in screen_objects_all:
#     utility.get_images(screen_objects)
#     length, number_of_comments = utility.create_audio(screen_objects)
#     utility.create_video(length, screen_objects)
# with open('videos_to_upload.json', 'w', encoding='utf-8') as f:
#     json.dump(val+[screen_objects], f, ensure_ascii=False, indent=4)
# # print(screen_objects)
# for i in range(51, 101):
# VIDEOS_TO_UPLOAD = open('videos_to_upload.json')
# val = json.load(VIDEOS_TO_UPLOAD)
screen_objects = {
    "thread_id": 1,
    "summary_text": "Check Out, This easy coding question is very commonly asked"
}
utility = Gateway(ServiceProviderFactory.get_provider("LEETCODE"))
screen_objects_all = utility.get_posts(screen_objects)
get_question_for_leetcode(screen_objects)
utility.get_images(screen_objects)
# utility.create_audio(screen_objects)

utility.create_video(length=8, screen_objects=screen_objects)

# with open('videos_to_upload.json', 'w', encoding='utf-8') as f:
#     json.dump(val+[screen_objects], f, ensure_ascii=False, indent=4)
# shutil.rmtree(f"results/temp/{screen_objects['thread_id']}")
