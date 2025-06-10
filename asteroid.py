import random
import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_trajectory = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(new_trajectory)
        new_vel2 = self.velocity.rotate(-new_trajectory)

        child_ast1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        child_ast2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)

        child_ast1.velocity = new_vel1*1.2
        child_ast2.velocity = new_vel2*1.2