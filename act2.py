#Add image and background image-
import pygame

pygame.init()
scrWidth, scrHeight = 500, 500

display_surface = pygame.display.set_mode((scrWidth, scrHeight))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.transform.scale(pygame.image.load('background.jpeg').convert(),(scrWidth, scrHeight))

bird_image = pygame.transform.scale(pygame.image.load('bird.jpeg').convert_alpha(), (200, 200))

bird_rect = bird_image.get_rect(center=(scrWidth // 2, scrHeight // 2 - 30))


def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    display_surface.blit(background_image, (0, 0))
    display_surface.blit(bird_image, bird_rect)
    pygame.display.flip()
    clock.tick(30)

  pygame.quit()


if __name__ == '__main__':
  game_loop()
