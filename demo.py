import pygame

pygame.init()
display_surface = pygame.display.set_mode((400,400))
pygame.display.set_caption("Adding background image")
bg=pygame.transform.scale(pygame.image.load("background.jpeg").convert(),(400,400))


def game():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 
                 running=False

        display_surface.blit(bg,(0,0))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__=="__main__":
    game()

