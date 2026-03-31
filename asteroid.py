from circleshape import CircleShape
import pygame
import random
from logger import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)

            first_velocity = self.velocity.rotate(angle)
            second_velocity = -1 * (self.velocity.rotate(angle))

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

            first_new_asteroid.velocity = first_velocity * 1.2
            second_new_asteroid.velocity = second_velocity * 1.2




    