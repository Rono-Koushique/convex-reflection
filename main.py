import pygame
from config import System
from utils import macros

pygame.init()
system = System(pygame.display.Info())

def main():
    while system.running:
        system.screen.fill((255, 255, 255))
        macros.refresh()
        for event in pygame.event.get():
            macros.quitGame(event, system)

if __name__ == "__main__":
    main()