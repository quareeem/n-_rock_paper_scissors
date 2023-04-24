import random
import math
import pygame

from game_constants import ROCK, PAPER, SCISSORS, SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_COLLISION_ITERATIONS, RED, GREEN, BLUE

class Object:
    def __init__(self, x, y, obj_type):
        self.x = x
        self.y = y
        self.obj_type = obj_type
        self.radius = 10
        self.speed = SPEED
        self.direction = random.uniform(0, 2*math.pi) # random direction in radians
        self.collided_this_frame = False

    def move(self, objects, screen):
        dx = self.speed * math.cos(self.direction)
        dy = self.speed * math.sin(self.direction)
        new_x = self.x + dx
        new_y = self.y + dy

        # Bounce from screen edges
        if new_x - self.radius < 0:
            new_x = self.radius
            self.direction = math.pi - self.direction
        elif new_x + self.radius > SCREEN_WIDTH:
            new_x = SCREEN_WIDTH - self.radius
            self.direction = math.pi - self.direction
        if new_y - self.radius < 0:
            new_y = self.radius
            self.direction = -self.direction
        elif new_y + self.radius > SCREEN_HEIGHT:
            new_y = SCREEN_HEIGHT - self.radius
            self.direction = -self.direction


        # Circle-circle collision detection and response
        if not self.collided_this_frame:
            for i in range(MAX_COLLISION_ITERATIONS):
                for obj in objects:
                    if obj != self and self.obj_type != obj.obj_type and self.collide(obj):

                        # Determine the collision outcome based on the types of the objects
                        if self.obj_type == ROCK and obj.obj_type == SCISSORS:
                            obj.obj_type = ROCK
                        elif self.obj_type == PAPER and obj.obj_type == ROCK:
                            obj.obj_type = PAPER
                        elif self.obj_type == SCISSORS and obj.obj_type == PAPER:
                            obj.obj_type = SCISSORS


                        # Calculate vector between centers of circles
                        dx = obj.x - self.x
                        dy = obj.y - self.y
                        distance = math.sqrt(dx**2 + dy**2)
                        overlap = self.radius + obj.radius - distance + 10

                        # Move circles apart to eliminate overlap
                        if distance > 0:
                            self.x -= overlap/2 * dx/distance
                            self.y -= overlap/2 * dy/distance
                            obj.x += overlap/2 * dx/distance
                            obj.y += overlap/2 * dy/distance

                        # Calculate new directions
                        angle = math.atan2(dy, dx)
                        self_direction = angle - (self.direction - angle)
                        obj_direction = angle - (obj.direction - angle)

                        # Update directions
                        self.direction = angle + self_direction
                        obj.direction = angle + obj_direction

                        self.collided_this_frame = True
                        obj.collided_this_frame = True
                        break
                else:
                    # No collisions, break out of loop
                    break
        else:
            self.collided_this_frame = False


        # Update position of object
        self.x = new_x
        self.y = new_y

        # Draw object
        if self.obj_type == ROCK:
            color = RED
        elif self.obj_type == PAPER:
            color = GREEN
        elif self.obj_type == SCISSORS:
            color = BLUE
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
    
    def collide(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance <= self.radius + other.radius
