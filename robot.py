

import numpy as np

class Robot:

    def __init__(self, x, y, max_speed, width, height, id):
        # arena information
        self.width = width
        self.height = height

        # robot information
        self.position = np.array([x, y])
        self.max_speed = max_speed
        self.velocity = np.array([0, 0])

        self.id = id

        self.radius = 15

        np.random.seed = id


    def wall_bounce(self):
        if self.position[0] > self.width - self.radius or self.position[0] < self.radius:
            self.velocity[0] = -self.velocity[0]
        elif self.position[1] > self.height - self.radius or self.position[1] < self.radius:
            self.velocity[1] = -self.velocity[1]

        # if bounce still ends up past wall, edit position
        next_x = self.position[0] + self.velocity[0]
        next_y = self.position[1] + self.velocity[1]

        if next_x > self.width - self.radius:
            self.position[0] = self.width - self.radius
        elif next_x < self.radius:
            self.position[0] = self.radius

        if next_y > self.height - self.radius:
            self.position[1] = self.height - self.radius
        elif next_y < self.radius:
            self.position[1] = self.radius

    def random_walk(self):
        self.velocity = (np.random.rand(2) - 0.5) * self.max_speed



    def update(self):
        self.position = self.position + self.velocity



