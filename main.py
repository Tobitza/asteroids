import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from gameover import game_over

def main():
    # Groups setup
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable

    pygame.init()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        log_state()

        # Exit game via window's X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        # Movement
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        # Rendering
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        # Collision check asteroid vs player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                game_over(screen, clock)
                return

        # Collision check asteroid vs shot
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
        
        
if __name__ == "__main__":
    main()
