from pygame.display import set_mode, set_caption
from pygame.time import Clock

class System:
    fps = 60
    running = True

    def __init__(self, infoObject) -> None:
        self.width, self.height = infoObject.current_w, infoObject.current_h
        self.screen = set_mode((self.width, self.height))
        self.clock = Clock().tick(self.fps)
        set_caption("Reflection Visualizer")