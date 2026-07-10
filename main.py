import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    pygame.init()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    

    while True:
        log_state()

        for event in pygame.event.get():
            pass
        
        # Movement
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        # Rendering
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
