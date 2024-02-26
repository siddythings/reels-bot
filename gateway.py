from services.provider import ServiceProvider


class Gateway:
    _provider: ServiceProvider

    def __init__(self, provider: ServiceProvider) -> None:
        self._provider = provider

    def get_posts(self, number_of_page):
        return self._provider.get_posts(number_of_page)

    def get_images(self, screen_objects):
        return self._provider.get_images(screen_objects)

    def create_audio(self, screen_objects):
        return self._provider.create_audio(screen_objects)

    def create_video(self, length, screen_objects):
        return self._provider.create_video(length, screen_objects)
