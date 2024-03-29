from services.provider import ServiceProvider
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, ViewportSize
from helper_functions import *
from moviepy.editor import AudioFileClip, CompositeAudioClip, concatenate_audioclips


class INC42(ServiceProvider):
    def __init__(self) -> None:
        super().__init__()

    def get_posts(self, number_of_page):
        cookies = {
            '_uid': 'CgEABmXaLfyMNABDdLjpAg==',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2024-02-25%2008%3A29%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2F%3Futm_medium%3Dreferral%26utm_souce%3Dwebsite%26utm_campaign%3Dback%26utm_content%3Darticle%7C%7C%7Crf%3Dhttps%3A%2F%2Finc42.com%2Fwp-content%2Fuploads%2F2024%2F02%2FRBI-PPIs-featured-1',
            'sbjs_first_add': 'fd%3D2024-02-24%2017%3A27%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_current': 'typ%3Dutm%7C%7C%7Csrc%3D%28none%29%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3Dback%7C%7C%7Ccnt%3Darticle%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
            'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
            'sbjs_udata': 'vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A122.0%29%20Gecko%2F20100101%20Firefox%2F122.0',
            'auth0_state': 'eyJpbnRlcmltIjpmYWxzZSwibm9uY2UiOiI4ZDc0NmFkZjIwZTc0YzFkNzhmMmMyMzYxZmI5NWFlNTg3ZDcyZjJlOTc0NzkzZGUwY2Y3NTAxNzU5YmUyOWVmIiwicmVkaXJlY3RfdG8iOiJodHRwczpcL1wvaW5jNDIuY29tXC9idXp6XC8ifQ==',
            'auth0_nonce': '03c333ee2e1ee32190f90baa5dd6fd342e3311079593d2168118cabfde7f0e50',
            'wp-unique_token': 'inc42-1708797444-222c789a-8156-441d-b23e-7ab1016838bc',
            'wp-issuem_lp': '%7B%22post%22%3A%7B%22444517%22%3A1711389444%2C%22444487%22%3A1711391033%7D%7D',
            'user_identified': '1',
            'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-NewRelic-ID': 'VQMDU1ZRCxABVVBRDgcDUlEI',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDIwMjMiLCJhcCI6IjExMjAyMDMzMTUiLCJpZCI6IjczZjM3YTgxZmEzM2RjMGMiLCJ0ciI6ImU0ODJmYjA5YjFlMDE5MzUwNDU4NjUxYjAyYjEzMTFkIiwidGkiOjE3MDg4NzcxNDk0NjJ9fQ==',
            'traceparent': '00-e482fb09b1e019350458651b02b1311d-73f37a81fa33dc0c-01',
            'tracestate': '1542023@nr=0-1-1542023-1120203315-73f37a81fa33dc0c----1708877149462',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://inc42.com',
            'Alt-Used': 'inc42.com',
            'Connection': 'keep-alive',
            'Referer': 'https://inc42.com/buzz/',
            # 'Cookie': '_uid=CgEABmXaLfyMNABDdLjpAg==; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-25%2008%3A29%3A51%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2F%3Futm_medium%3Dreferral%26utm_souce%3Dwebsite%26utm_campaign%3Dback%26utm_content%3Darticle%7C%7C%7Crf%3Dhttps%3A%2F%2Finc42.com%2Fwp-content%2Fuploads%2F2024%2F02%2FRBI-PPIs-featured-1; sbjs_first_add=fd%3D2024-02-24%2017%3A27%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dutm%7C%7C%7Csrc%3D%28none%29%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3Dback%7C%7C%7Ccnt%3Darticle%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A122.0%29%20Gecko%2F20100101%20Firefox%2F122.0; auth0_state=eyJpbnRlcmltIjpmYWxzZSwibm9uY2UiOiI4ZDc0NmFkZjIwZTc0YzFkNzhmMmMyMzYxZmI5NWFlNTg3ZDcyZjJlOTc0NzkzZGUwY2Y3NTAxNzU5YmUyOWVmIiwicmVkaXJlY3RfdG8iOiJodHRwczpcL1wvaW5jNDIuY29tXC9idXp6XC8ifQ==; auth0_nonce=03c333ee2e1ee32190f90baa5dd6fd342e3311079593d2168118cabfde7f0e50; wp-unique_token=inc42-1708797444-222c789a-8156-441d-b23e-7ab1016838bc; wp-issuem_lp=%7B%22post%22%3A%7B%22444517%22%3A1711389444%2C%22444487%22%3A1711391033%7D%7D; user_identified=1; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        post_data = []

        for i in range(1, number_of_page+1):
            data = data = {
                'action': 'inc42_load_more_cat',
                'nonce': '9fac6296c6',
                'page': f'{str(i)}',
                'query': '{"category_name":"buzz","error":"","m":"","p":0,"post_parent":"","subpost":"","subpost_id":"","attachment":"","attachment_id":0,"name":"","pagename":"","page_id":0,"second":"","minute":"","hour":"","day":0,"monthnum":0,"year":0,"w":0,"tag":"","cat":15,"tag_id":"","author":"","author_name":"","feed":"","tb":"","paged":0,"meta_key":"","meta_value":"","preview":"","s":"","sentence":"","title":"","fields":"","menu_order":"","embed":"","category__in":[],"category__not_in":[],"category__and":[],"post__in":[],"post__not_in":[],"post_name__in":[],"tag__in":[],"tag__not_in":[],"tag__and":[],"tag_slug__in":[],"tag_slug__and":[],"post_parent__in":[],"post_parent__not_in":[],"author__in":[],"author__not_in":[],"search_columns":[],"ignore_sticky_posts":false,"suppress_filters":false,"cache_results":true,"update_post_term_cache":true,"update_menu_item_cache":false,"lazy_load_term_meta":true,"update_post_meta_cache":true,"post_type":"","posts_per_page":12,"nopaging":false,"comments_per_page":"50","no_found_rows":false,"order":"DESC","auth0_login_successful":false}',
            }

            # Request to inc42
            response = requests.post(
                'https://inc42.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all 'a' tags within the specified class
            all_links = soup.find_all('a', class_='recommended-block-head')
            for link in all_links:
                href_value = link.get('href')
                title_data = link.get('title')
                img_tag = link.find('img')
                image_url = None
                if img_tag:
                    image_url = img_tag.get("src")

                post_data.append({
                    "thread_id": str(random.randint(1000000, 99999999)),
                    "href_value": href_value,
                    "title_data": title_data,
                    "image_url": image_url
                })
        print(post_data)
        return post_data

    def get_images(self, screen_objects):
        print(screen_objects["thread_id"])
        with sync_playwright() as p:
            iphone_11 = p.devices["iPhone 11 Pro Max"]
            browser = p.chromium.launch()
            context = browser.new_context(**iphone_11)
            page = context.new_page()
            page.goto(
                screen_objects.get("href_value"),
                timeout=0,
            )
            flag = False
            page.set_viewport_size(ViewportSize(width=448, height=1800))
            # page.reload(timeout=0)

            if page.locator(".entry-title").is_visible():
                page.locator(".entry-title").screenshot(
                    path=f'results/temp/{screen_objects["thread_id"]}/one.png'
                )
                flag = True
            # if page.locator("div.single-featured-thumb").is_visible():
            #     page.locator("div.single-featured-thumb").screenshot(
            #         path=f'results/temp/1/two.png'
            #     )
            #     flag = True
            test = page.locator(
                '.single-post-summary').inner_html()

            soup = BeautifulSoup(test, 'html.parser')

            # Find the 'h4' tag with text 'SUMMARY'
            summary_tag = soup.find('h4', text='SUMMARY')

            # If 'SUMMARY' tag is found, get the text of the first <p> block after it
            if summary_tag:
                # Find the first <p> tag after the 'SUMMARY' tag
                first_p_after_summary = summary_tag.find_next('p')

                # Get the text of the <p> block
                if first_p_after_summary:
                    summary_text = first_p_after_summary.get_text(strip=True)
                    text_to_image(
                        summary_text, f"results/temp/{screen_objects['thread_id']}/summary_text.png", max_width=1272)
                    save_image_from_url(screen_objects.get(
                        "image_url"), f"results/temp/{screen_objects['thread_id']}/two.png")
                    screen_objects.update({
                        "summary_text": summary_text
                    })
            browser.close()

        max_width = 1272

        use_images = [
            "common/header.png",
            f"results/temp/{screen_objects['thread_id']}/one.png",
            f"results/temp/{screen_objects['thread_id']}/two.png",
            f"results/temp/{screen_objects['thread_id']}/summary_text.png",
            "common/footer.png"
        ]

        # # To check if all the image are same height
        # images = [Image.open(x) for x in use_images]

        # for i, img in enumerate(images):
        #     if img.size[0] > max_width:
        #         resize_image(max_width, use_images[i])

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
        # Save the image

        new_img.save(
            f"results/temp/{screen_objects['thread_id']}/final.png"
        )

    def create_audio(self, screen_objects):
        from IPython.display import Audio
        from bark import SAMPLE_RATE, generate_audio, preload_models
        text_prompt = screen_objects.get("summary_text")
        speech_array = generate_audio(
            text_prompt, history_prompt="v2/en_speaker_6")
        with open(f"results/temp/{screen_objects['thread_id']}/0.mp3", "wb") as audio_file:
            audio_file.write(Audio(speech_array, rate=SAMPLE_RATE).data)

        clip = AudioFileClip(
            f"results/temp/{screen_objects['thread_id']}/0.mp3"
        )
        length = clip.duration
        clip.close()
        return length, 1

    def create_video(self, length, screen_objects):
        chop_background_video(length, screen_objects)
        make_final_video_new(length, screen_objects)
