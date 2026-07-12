import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self) -> None:
        pygame.sprite.Sprite.kill(self)

        # Asteroid size checker
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        angle1 = self.velocity.rotate(angle)
        angle2 = self.velocity.rotate(-angle)
        spawn_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn1 = Asteroid(self.position[0], self.position[1], spawn_radius)
        spawn2 = Asteroid(self.position[0], self.position[1], spawn_radius)
        spawn1.velocity = angle1 * 1.2
        spawn2.velocity = angle2 * 1.2

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = self.position + self.velocity * dt
