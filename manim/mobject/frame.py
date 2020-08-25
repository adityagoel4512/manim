from ..constants import Colors
from ..config import config
from ..mobject.geometry import Rectangle
from ..utils.config_ops import digest_config


class ScreenRectangle(Rectangle):
    CONFIG = {"aspect_ratio": 16.0 / 9.0, "height": 4}

    def __init__(self, **kwargs):
        Rectangle.__init__(self, **kwargs)
        self.set_width(self.aspect_ratio * self.get_height(), stretch=True)


class FullScreenRectangle(ScreenRectangle):
    CONFIG = {
        "height": config["frame_height"],
    }


class FullScreenFadeRectangle(FullScreenRectangle):
    CONFIG = {
        "stroke_width": 0,
        "fill_color": Colors.black.value,
        "fill_opacity": 0.7,
    }


class PictureInPictureFrame(Rectangle):
    CONFIG = {"height": 3, "aspect_ratio": 16.0 / 9.0}

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        Rectangle.__init__(
            self, width=self.aspect_ratio * self.height, height=self.height, **kwargs
        )
