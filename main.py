import pygame
from config import System
from utils import macros
from data.constants.color import color
from objects import Background, Axis

pygame.init()
system = System(pygame.display.Info())

# creating objects
bg = Background(system, color=color.white, grid_on=True)
mainAxis = Axis(system, color=color.gray_800)


def main():
    while system.running:
        bg.draw()
        mainAxis.draw()

        macros.refresh()
        for event in pygame.event.get():
            macros.quitGame(event, system)


if __name__ == "__main__":
    main()
