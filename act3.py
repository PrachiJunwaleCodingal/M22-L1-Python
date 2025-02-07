#play with text and font
import pygame

pygame.init()
scrWidth, scrHeight = 500, 500

display_surface = pygame.display.set_mode((scrWidth, scrHeight))
display_surface.fill("white")
pygame.display.set_caption('text and font')

text = pygame.font.Font(None, 36).render('Welcome to my app', True, pygame.Color('blue'))
text_rect = text.get_rect(center=(scrWidth // 2, scrHeight // 2))



def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    
    display_surface.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(30)

  pygame.quit()


if __name__ == '__main__':
  game_loop()
