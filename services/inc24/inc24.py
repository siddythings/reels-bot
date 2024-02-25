from services.provider import ServiceProvider
import requests
from bs4 import BeautifulSoup


class INC24(ServiceProvider):
    def __init__(self) -> None:
        super().__init__()

    def get_posts(self, number_of_page):
        cookies = {
            '_uid': 'CgEABmXaLfyMNABDdLjpAg==',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2024-02-24%2017%3A48%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_first_add': 'fd%3D2024-02-24%2017%3A27%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
            'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A122.0%29%20Gecko%2F20100101%20Firefox%2F122.0',
            'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F',
            'auth0_state': 'eyJpbnRlcmltIjpmYWxzZSwibm9uY2UiOiJjY2RhNjA0ZDQ0ZjQzNWEyNTkxMGFmMGM4YWE3MGZiMmRkMDdhYTA3MGY4Yjc0Mjk1YzhmNmYwOWIxM2M5OWVhIiwicmVkaXJlY3RfdG8iOiJodHRwczpcL1wvaW5jNDIuY29tXC9idXp6XC8ifQ==',
            'auth0_nonce': '4536e130569b143d1cc136403b438e2bcb9c27bc0ff0278db07d16900665138b',
            'wp-unique_token': 'inc42-1708797444-222c789a-8156-441d-b23e-7ab1016838bc',
            'wp-issuem_lp': '%7B%22post%22%3A%7B%22444517%22%3A1711389444%7D%7D',
            'user_identified': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-NewRelic-ID': 'VQMDU1ZRCxABVVBRDgcDUlEI',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE1NDIwMjMiLCJhcCI6IjExMjAyMDMzMTUiLCJpZCI6Ijc4ZGYwNWRjZDZkMWNmMmIiLCJ0ciI6ImI3ZjIzNDRkYjdhYjFlYWJjMWJiYTVjZTRjNTBiMDNjIiwidGkiOjE3MDg3OTg3ODY4MTZ9fQ==',
            'traceparent': '00-b7f2344db7ab1eabc1bba5ce4c50b03c-78df05dcd6d1cf2b-01',
            'tracestate': '1542023@nr=0-1-1542023-1120203315-78df05dcd6d1cf2b----1708798786816',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://inc42.com',
            'Alt-Used': 'inc42.com',
            'Connection': 'keep-alive',
            'Referer': 'https://inc42.com/buzz/',
            # 'Cookie': '_uid=CgEABmXaLfyMNABDdLjpAg==; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-02-24%2017%3A48%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2024-02-24%2017%3A27%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A122.0%29%20Gecko%2F20100101%20Firefox%2F122.0; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Finc42.com%2Fbuzz%2F; auth0_state=eyJpbnRlcmltIjpmYWxzZSwibm9uY2UiOiJjY2RhNjA0ZDQ0ZjQzNWEyNTkxMGFmMGM4YWE3MGZiMmRkMDdhYTA3MGY4Yjc0Mjk1YzhmNmYwOWIxM2M5OWVhIiwicmVkaXJlY3RfdG8iOiJodHRwczpcL1wvaW5jNDIuY29tXC9idXp6XC8ifQ==; auth0_nonce=4536e130569b143d1cc136403b438e2bcb9c27bc0ff0278db07d16900665138b; wp-unique_token=inc42-1708797444-222c789a-8156-441d-b23e-7ab1016838bc; wp-issuem_lp=%7B%22post%22%3A%7B%22444517%22%3A1711389444%7D%7D; user_identified=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        post_data = []

        for i in range(1, number_of_page+1):
            data = {
                'action': 'inc42_load_more_cat',
                'nonce': 'efa5bb79b3',
                'page': {str(i)},
                'query': '{"category_name":"buzz","error":"","m":"","p":0,"post_parent":"","subpost":"","subpost_id":"","attachment":"","attachment_id":0,"name":"","pagename":"","page_id":0,"second":"","minute":"","hour":"","day":0,"monthnum":0,"year":0,"w":0,"tag":"","cat":15,"tag_id":"","author":"","author_name":"","feed":"","tb":"","paged":0,"meta_key":"","meta_value":"","preview":"","s":"","sentence":"","title":"","fields":"","menu_order":"","embed":"","category__in":[],"category__not_in":[],"category__and":[],"post__in":[],"post__not_in":[],"post_name__in":[],"tag__in":[],"tag__not_in":[],"tag__and":[],"tag_slug__in":[],"tag_slug__and":[],"post_parent__in":[],"post_parent__not_in":[],"author__in":[],"author__not_in":[],"search_columns":[],"ignore_sticky_posts":false,"suppress_filters":false,"cache_results":true,"update_post_term_cache":true,"update_menu_item_cache":false,"lazy_load_term_meta":true,"update_post_meta_cache":true,"post_type":"","posts_per_page":12,"nopaging":false,"comments_per_page":"50","no_found_rows":false,"order":"DESC","auth0_login_successful":false}',
            }

            # Request to inc42
            response = requests.post(
                'https://inc42.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(response, 'html.parser')

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
                    "href_value": href_value,
                    "title_data": title_data,
                    "image_url": image_url
                })

        return post_data

    def get_images(self):
        pass

    def create_video(self):
        pass
