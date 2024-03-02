from services.provider import ServiceProvider
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, ViewportSize
from helper_functions import *
from moviepy.editor import AudioFileClip, CompositeAudioClip, concatenate_audioclips


class Leetcode(ServiceProvider):
    def __init__(self) -> None:
        super().__init__()

    def get_posts(self, number_of_page):
        pass

    def get_images(self, screen_objects):
        pass

    def create_audio(self, screen_objects):
        pass

    def create_video(self, length, screen_objects):
        pass
