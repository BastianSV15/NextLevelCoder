import pygame
<<<<<<< HEAD
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING
=======
from dino_runner.utils.constants import RUNNING, JUMPING
>>>>>>> b7fd7ff408950c3410e2e967ca13f0cb1d748ca7
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310 
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
<<<<<<< HEAD
        self.dino_duck = False
=======
>>>>>>> b7fd7ff408950c3410e2e967ca13f0cb1d748ca7

    def update(self, user_input):
        if self.dino_run:
            self.run()
        
        elif self.dino_jump:
            self.jump()

<<<<<<< HEAD
        elif self.dino_duck:
            self.duck()
  
=======

        
>>>>>>> b7fd7ff408950c3410e2e967ca13f0cb1d748ca7
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_jump = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

<<<<<<< HEAD
        if user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_duck = True
            self.dino_duck = False
        elif not self.dino_duck:
            self.dino_duck = False
            self.dino_run = True

=======
>>>>>>> b7fd7ff408950c3410e2e967ca13f0cb1d748ca7
        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.image = self.X_POS
        self.image = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if  self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

<<<<<<< HEAD
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.image = self.X_POS
        self.image = self.Y_POS
        self.step_index += 1
        

    def draw(self, screen: pygame.Surface):
=======
    def draw(self, screen: pygame.surface):
>>>>>>> b7fd7ff408950c3410e2e967ca13f0cb1d748ca7
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y ))