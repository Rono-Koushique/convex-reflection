from pygame import QUIT, K_ESCAPE, KEYDOWN, display

def refresh():
    display.flip()

def quitGame(event, system):
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        system.running = False
    