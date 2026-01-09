# Your Title Here
# Author: Ian Poon
# Date: 7 January 2026

import random

import pygame

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        """A blue block"""
        super().__init__()

        self.image = pygame.Surface((20, 15))
        # change the colour of our image to blue
        self.image.fill(BLUE)

        # rect represents the hitbox of our sprite
        # the hitbox gives information about:
        # - location of the sprite x, y
        # - the size of the sprite width, height
        self.rect = self.image.get_rect()
        # change the location of our hitbox
        self.rect.centerx = 100
        self.rect.centery = 100


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """Player sprite"""
        super().__init__()
        self.image = pygame.image.load("assets/mario-snes.png")

        self.rect = self.image.get_rect()

    def update(self):
        """Have Mario follow the mouse"""
        self.rect.center = pygame.mouse.get_pos()


class Enermy(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()

        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()
        # No inital location -> (0, 0)

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        # movement in the x-axis
        self.rect.x += self.vel_x
        # movement in the y-axis
        self.rect.y += self.vel_y
        # randomize movement


def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # create a sprite group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enermy_sprites_group = pygame.sprite.Group()

    # Create player sprite
    player = Mario()
    # place Mario in the middle of the screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    all_sprites_group.add(player)

    # Create enemy sprite
    for _ in range(3):
        enermy_one = Enermy()

        random_x = random.randrange(20, 100)
        random_y = random.randrange(HEIGHT - 100, HEIGHT - 20)
        enermy_one.rect.center = random_x, random_y
        # Randomize velocity
        enermy_one.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        enermy_one.vel_y = random.choice([-3, -2, -1, 1, 2, 3])

        all_sprites_group.add(enermy_one)
        enermy_sprites_group.add(enermy_one)

    # create 100 blocks
    for _ in range(100):
        block = Block()
        # rendomize their location
        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)
        # add them to the sprite group
        all_sprites_group.add(block)
        block_sprites_group.add(block)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        # Keep the enemies inside the screen
        for enermy in enermy_sprites_group:
            if enermy.rect.left < 0 or enermy.rect.right > WIDTH:
                enermy.vel_x = -enermy.vel_x
            if enermy.rect.top < 0 or enermy.rect.bottom > HEIGHT:
                enermy.vel_y = -enermy.vel_y

        # Make a group of just BLOCKS
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        if blocks_collided:
            print("-----")
            print("Mario has collided with a block!")
            print(blocks_collided)

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        # Draw all the sprites
        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
