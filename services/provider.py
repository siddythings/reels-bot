from abc import ABC, abstractmethod


class ServiceProvider(ABC):
    """Provider Class is the abstraction over the Utility provider"""

    @abstractmethod
    def get_posts(self):
        pass

    @abstractmethod
    def get_images(self):
        pass

    @abstractmethod
    def create_video(self):
        pass
