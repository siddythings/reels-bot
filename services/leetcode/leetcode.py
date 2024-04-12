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

    def get_posts(self, screen_objects):
        number_of_page = screen_objects["thread_id"]
        with sync_playwright() as p:
            # iphone_11 = p.devices["iPhone 11 Pro Max"]
            element_selector = ".tabbed-content"
            browser = p.chromium.launch()
            context = browser.new_context(viewport={'width': 800, 'height': 1440},
                                          device_scale_factor=10,

                                          is_mobile=False,
                                          strict_selectors=False)
            page = context.new_page()

            page.goto(
                f"https://walkccc.me/LeetCode/problems/{number_of_page}/#__tabbed_1_3",
                timeout=0,
            )
            element = page.locator(element_selector).nth(0)

            if element.count():
                element.screenshot(
                    path=f"results/temp/{number_of_page}/one.png")
            else:
                page.goto(
                    f"https://walkccc.me/LeetCode/problems/{number_of_page}/#__tabbed_1_3",
                    timeout=0,
                )
                element = page.locator(element_selector).nth(0)
                element.screenshot(
                    path="results/temp/{number_of_page}/one.png")

            response = requests.get(
                f"https://walkccc.me/LeetCode/problems/{number_of_page}/#__tabbed_1_3")
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the element with the specified ID and get the H1 text
            h1_element = soup.find('h1')
            p_element = soup.find('p').find("img").get("src")

            if "easy" in p_element.lower():
                screen_objects.update({
                    "type": "easy",
                    "headline": h1_element.text.replace("¶", "")
                })
            elif "medium" in p_element.lower():
                screen_objects.update({
                    "type": "medium",
                    "headline": h1_element.text.replace("¶", "")
                })
            else:
                screen_objects.update({
                    "type": "hard",
                    "headline": h1_element.text.replace("¶", "")
                })

            update_footer_image(p_element.replace("svg", "png"))

            # Find the 'h4' tag with text 'SUMMARY'
            text_to_image(
                h1_element.text.replace("¶", ""), f"results/temp/{number_of_page}/summary_text.png", max_width=1272, image_background_color="#272A35")
            max_width = 1272
            resize_image(max_width, f"results/temp/{number_of_page}/one.png")

            browser.close()

    def get_images(self, screen_objects):

        number_of_page = screen_objects["thread_id"]

        use_images = [
            "common/leetcode_header.png",
            f"results/temp/{number_of_page}/summary_text.png",
            f"results/temp/{number_of_page}/final_question.png",
            f"results/temp/{number_of_page}/one.png",
            "leetcode_footer.png"
        ]
        images = [Image.open(x) for x in use_images]

        if images:
            total_width = 0
            max_height = 0

            # find the width and height of the final image
            for img in images:
                total_width = max(total_width, img.size[0])
                # total_width = img.size[0]
                max_height += img.size[1]

            # create a new image with the appropriate height and width
            new_img = Image.new("RGBA", (total_width, max_height))
            # Write the contents of the new image
            current_width = 0
            new_img.paste(images[0], (current_width, 0))
            current_width += images[0].size[1]
            for img in range(1, len(images)):
                new_img.paste(images[img], (0, current_width))
                current_width += images[img].size[1]
        new_img.save(
            f"results/temp/{number_of_page}/final.png"
        )

    def create_audio(self, screen_objects):
        #     from IPython.display import Audio
        #     from bark import SAMPLE_RATE, generate_audio, preload_models
        #     text_prompt = screen_objects.get("summary_text")
        #     speech_array = generate_audio(
        #         text_prompt, history_prompt="v2/en_speaker_7")
        #     with open(f"results/temp/{screen_objects['thread_id']}/0.mp3", "wb") as audio_file:
        #         audio_file.write(Audio(speech_array, rate=SAMPLE_RATE).data)

        #     clip = AudioFileClip(
        #         f"results/temp/{screen_objects['thread_id']}/0.mp3"
        #     )
        #     length = clip.duration
        #     clip.close()
        #     return length, 1
        pass

    def create_video(self, length=10, screen_objects={}):
        W, H = 1080, 1920

        background_clip = "1709828999594251.mp4"
        # chop_background_video(length, screen_objects,
        #                       background_clip=f"common/{background_clip}")

        VideoFileClip.reW = lambda clip: clip.resize(width=W)
        VideoFileClip.reH = lambda clip: clip.resize(width=H)
        opacity = 1.0
        transition = 0
        if screen_objects["type"] == "easy":
            background_clip = (
                VideoFileClip(
                    f"common/Check_This_Out_easy.mp4")
            )
        elif screen_objects["type"] == "medium":
            background_clip = (
                VideoFileClip(
                    f"common/Check_This_Out_medium.mp4")
            )
        else:
            background_clip = (
                VideoFileClip(
                    f"common/Check_This_Out_hard.mp4")
            )

        # Gather all audio clips
        # audio_clips = [AudioFileClip(
        #     f"results/temp/{screen_objects['thread_id']}/0.mp3")]
        # audio_concat = concatenate_audioclips(audio_clips)
        # audio_composite = CompositeAudioClip([audio_concat])

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
            ImageClip(f"Rectangle 42.png")
            .set_duration(3)
            .set_opacity(new_opacity)
            .crossfadein(new_transition)
            .crossfadeout(new_transition),
        )
        image_clips.insert(
            1,
            ImageClip(f"results/temp/{screen_objects['thread_id']}/final.png")
            .set_duration(6)
            .resize(width=W - 100)
            .set_opacity(new_opacity)
            .crossfadein(new_transition)
            .crossfadeout(new_transition),
        )
        img_clip_pos = "center"

        image_concat = concatenate_videoclips(image_clips).set_position(
            img_clip_pos
        )
        # image_concat.audio = audio_composite
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
