from pygame.display import set_mode
from pygame.time import Clock

class System:
    fps = 60
    running = True

    def __init__(self, infoObject) -> None:
        self.resolution = [infoObject.current_w, infoObject.current_h]
        self.screen = set_mode(self.resolution)
        self.clock = Clock().tick(self.fps)