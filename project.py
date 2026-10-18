import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class car():
        def __init__(self, x, y, width, height):
            self.car_surface = pygame.Surface((width, height), pygame.SRCALPHA)
            pygame.draw.rect(
                self.car_surface,
                (255, 0, 0),
                (0, 0, width, height)
            )
            self.position_x = float(x)
            self.position_y = float(y)
            self.speed = 0
            self.angle = 0
            

        def move(self):
            keys = pygame.key.get_pressed()
            import math
            if keys[pygame.K_w] and self.speed < 5:
                self.speed += 0.1
            if keys[pygame.K_s] and self.speed > -1:
                self.speed -= 0.1
            steering_strenght = 2 / (1 + abs(self.speed) * 0.5)
            if abs(self.speed) > 0.05:
                if keys[pygame.K_d]:
                    self.angle -= steering_strenght
                if keys[pygame.K_a]:
                    self.angle += steering_strenght
            self.car_rotated = pygame.transform.rotate(self.car_surface, self.angle)
            self.rotated_position = self.car_rotated.get_rect(center=(round(self.position_x), round(self.position_y)))
            dx = math.cos(math.radians(self.angle)) * self.speed
            dy = -math.sin(math.radians(self.angle)) * self.speed
            self.position_x += dx 
            self.position_y += dy 

car1 = car(100, 100, 50, 30)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
    

    
    car1.move()
    screen.blit(car1.car_rotated, car1.rotated_position)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(144)  

pygame.quit()