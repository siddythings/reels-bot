from abc import ABC, abstractmethod


class ServiceProvider(ABC):
    """Provider Class is the abstraction over the Utility provider"""

    @abstractmethod
    def get_posts(self, screen_objects):
        pass

    @abstractmethod
    def get_images(self, screen_objects):
        pass

    @abstractmethod
    def create_audio(self, screen_objects):
        pass

    @abstractmethod
    def create_video(self, length, screen_objects):
        pass
