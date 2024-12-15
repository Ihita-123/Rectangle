import pygame
pygame.init()

screen= pygame.display.set_mode((400,600))

red=(255,0,0)
blue=(0,255,0)
green=(0,0,255)
white=(255,255,255)
black=(0,0,0)
green=(0,255,255)

screen.fill(white)
class rectangle():
    def __init__(self,color,dimensions):
        self.surf=screen
        self.color=color
        self.dimensions= dimensions

    def draw(self):
        pygame.draw.rect(self.surf, self.color, self.dimensions)


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    grect=rectangle(green,(100,40,20,30))
    rrect=rectangle(red,(10,250,30,40))
    blrect=rectangle(black,(30,40,50,40))
    brect=rectangle(blue,(40,20,200,70))
    grect.draw()
    rrect.draw()
    brect.draw()
    blrect.draw()


    pygame.display.update()