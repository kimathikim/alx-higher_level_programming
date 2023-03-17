#!/usr/bin/python3
import pygame
import random
import sys

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Farm Simulation Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 450
        self.money = 0

    def update(self):
        pass

class Crop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 750)
        self.rect.y = random.randint(50, 450)
        self.harvested = False

    def update(self):
        pass

class Animal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 750)
        self.rect.y = random.randint(50, 450)
        self.hunger = 0

    def update(self):
        pass

class Market(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 100

    def update(self):
        pass

class TomatoCrop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("tomato.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.growth_time = 5  # in seconds
        self.harvest_value = 15
        self.harvested = False
        self.grow_time = 0

    def update(self):
        if not self.harvested:
            self.grow_time += 1
            if self.grow_time >= self.growth_time:
                self.image = pygame.image.load("ripe_tomato.png")


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
crops = pygame.sprite.Group()
animals = pygame.sprite.Group()
market = pygame.sprite.Group()
market.add(Market())
all_sprites.add(market)

crop_frequency = 100
crop_counter = 0
animal_frequency = 200
animal_counter = 0
while True:
    # code to handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # code to update player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    # code to generate crops
    crop_counter += 1
    if crop_counter == crop_frequency:
        crop_counter = 0
        crop = Crop()
        crops.add(crop)
        all_sprites.add(crop)

    # code to update crops
   
    for crop in crops:
        if pygame.sprite.collide_rect(crop, player):
            if not crop.harvested:
                crop.harvested = True
                player.money += 10
                crops.remove(crop)
                all_sprites.remove(crop)

    # code to generate animals
    animal_counter += 1
    if animal_counter == animal_frequency:
        animal_counter = 0
        animal = Animal()
        animals.add(animal)
        all_sprites.add(animal)

    # code to update animals
    for animal in animals:
        animal.hunger += 1
        if animal.hunger >= 100:
            animals.remove(animal)
            all_sprites.remove(animal)
        if pygame.sprite.collide_rect(animal, player):
            player.money += 20
            animals.remove(animal)
            all_sprites.remove(animal)

    # code to update the screen
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    text = "Money: $" + str(player.money)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))
    pygame.display.flip()
