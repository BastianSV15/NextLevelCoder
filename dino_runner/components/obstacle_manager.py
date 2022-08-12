import pygame
from pygame import mixer
import random
from .large_cactus import LargeCactus
from .small_cactus import SmallCactus
from .bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

        numeros = random.randint(0, 2)
        if len(self.obstacles) == 0:

            if numeros == 0: 
                self.obstacles.append(Bird(BIRD))

            elif numeros == 1:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))

            elif numeros == 2:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(100)
                    game.playing = False
                    mixer.music.load("Dead.wav")
                    mixer.music.play(1)
                    mixer.music.set_volume(0.1)
      
                    game.death_count += 1
                else:
                    self.obstacles.remove(obstacle)
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

