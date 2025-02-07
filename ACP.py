
#ACP- Add game images-
import pygame

pygame.init()
scrWidth, scrHeight = 500, 500

display_surface = pygame.display.set_mode((scrWidth, scrHeight))
pygame.display.set_caption('Adding  game images')

background_image = pygame.transform.scale(pygame.image.load('gameBG.jpeg').convert(),(scrWidth, scrHeight))

game_image = pygame.transform.scale(pygame.image.load('game.jpeg').convert_alpha(), (200, 200))
game_rect = game_image.get_rect(center=(scrWidth // 2, scrHeight // 2 - 30))
text = pygame.font.Font(None, 36).render('Welcome to Game Zone', True, pygame.Color('pink'))
text_rect = text.get_rect(center=(scrWidth // 2, scrHeight // 2 + 110))

def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    display_surface.blit(background_image, (0, 0))
    display_surface.blit(game_image, game_rect)
    display_surface.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(30)

  pygame.quit()


if __name__ == '__main__':
  game_loop()
