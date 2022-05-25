import pygame


def mainloop(onupdate:object, eventhandler:object=None, updateinterval:float=0.0):
    running = True
    while running:
        eventhandler()
        if onupdate:
            onupdate()
        else:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    running = False
        pygame.time.delay(updateinterval)
        

class Animation:
    def __init__():
        pass
    
    def get_frame():
        pass
