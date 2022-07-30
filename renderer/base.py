from typing import Any, Generator, Union, Optional
from abc import ABC, abstractmethod
from .data import ReplayData
from PIL import Image


class RendererBase(ABC):
    """A template for Renderer classes"""

    replay_data: ReplayData
    res: str
    minimap_image: Optional[Image.Image]
    minimap_size: int
    space_size: int
    scaling: float

    @abstractmethod
    def __init__(self, replay_data: ReplayData):
        pass

    @abstractmethod
    def start(self):
        """
        Starts the renderer.
        """
        pass

    @abstractmethod
    def _load_map(self):
        """
        Loads the map.
        """
        pass


class LayerBase(ABC):
    """A template for Layer classes"""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def draw(
        self, game_time: int
    ) -> Union[Generator[Any, None, None], Image.Image]:
        """
        Yields whatever the fuck it wants to yield.
        :return: A generator.
        """
        pass