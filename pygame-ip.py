# Pygame Final
# Author: Ian Poon
# Date: 14 January 2026

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


class Bread(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/杰哥 麵包 - Google 搜尋.png")
        self.image = pygame.transform.scale_by(self.image, 0.15)

        self.rect = self.image.get_rect()
        self.point_value = 1

    def level_up(self, val: int):
        self.point_value *= val


class Way(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image_right = pygame.image.load("assets/IMG_2448.JPG")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.2)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.previous_x = 0
        self.health = 100
        self.points = 0

    def calc_damage(self, amt: int):
        self.health -= amt

    def incr_score(self, amt: int):
        self.points += amt

    def get_damage_percentage(self):
        return max(self.health / 100, 0)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/IMG_2447.WEBP")
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()

        self.vel_x = random.choice([-5, -3, -1, 1, 3, 5])
        self.vel_y = random.choice([-5, -3, -1, 1, 3, 5])
        self.damage = 1

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        self.damage *= 2


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/images.steamusercontent.jpg")
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()

        self.vel_x = random.choice([-5, -3, -1, 1, 3, 5])
        self.vel_y = random.choice([-5, -3, -1, 1, 3, 5])
        self.damage = 1

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        self.damage *= 2


class HealthBar(pygame.Surface):
    def __init__(self, width, height):
        super().__init__((width, height))
        self.width = width
        self.height = height

    def update_info(self, percentage):
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, self.width * percentage, self.height))


def game():
    pygame.init()

    font = pygame.font.Font(None, 36)  # Default font, size 36
    big_font = pygame.font.Font(None, 72)
    score_font = pygame.font.Font(None, 48)  # BIGGER score font

    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Collect Breads")

    background = pygame.image.load("assets/IMG_2450.JPG").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    done = False
    level = 1

    all_sprites = pygame.sprite.Group()
    bread_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_two_group = pygame.sprite.Group()

    health_bar = HealthBar(150, 10)

    # Player
    player = Way()
    player.rect.center = (WIDTH // 2, HEIGHT // 2)
    all_sprites.add(player)

    # Enemies
    for _ in range(3):
        enemy = Enemy()
        enemy.rect.center = (WIDTH // 2, HEIGHT // 2)
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    # Enemies 2
    for _ in range(2):
        enemy2 = Enemy2()
        enemy2.rect.center = (WIDTH // 2, HEIGHT // 2)
        all_sprites.add(enemy2)
        enemy_two_group.add(enemy2)

    # Bread
    for _ in range(100):
        bread = Bread()
        bread.rect.center = (
            random.randrange(WIDTH),
            random.randrange(HEIGHT),
        )
        all_sprites.add(bread)
        bread_group.add(bread)

    display_score = 0

    # ---------------- MAIN LOOP ----------------
    if display_score < player.points:
        display_score += min(5, player.points - display_score)

    score_text = score_font.render(f"Score: {display_score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    while not done:
        for event in pygame.event.get():
            if player.health <= 0:
                done = True

        # --- GAME LOGIC ---
        all_sprites.update()

        for enemy in enemy_group:
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x *= -1
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y *= -1

        for enemy2 in enemy_two_group:
            if enemy2.rect.left < 0 or enemy2.rect.right > WIDTH:
                enemy2.vel_x *= -1
            if enemy2.rect.top < 0 or enemy2.rect.bottom > HEIGHT:
                enemy2.vel_y *= -1

        # Player & Bread collision
        breads = pygame.sprite.spritecollide(player, bread_group, True)
        for bread in breads:
            player.incr_score(bread.point_value)

        # Level up
        if len(bread_group) == 0:
            level += 1

            for _ in range(100):
                bread = Bread()
                bread.level_up(level)
                bread.rect.center = (
                    random.randrange(WIDTH),
                    random.randrange(HEIGHT),
                )
                all_sprites.add(bread)
                bread_group.add(bread)

        # Enemy collision
        enemies = pygame.sprite.spritecollide(player, enemy_group, False)
        for enemy in enemies:
            player.calc_damage(enemy.damage)

        health_bar.update_info(player.get_damage_percentage())

        if player.health <= 0:
            done = True

        # Enemy 2 collision
        enemies2 = pygame.sprite.spritecollide(player, enemy_two_group, False)
        for enemy2 in enemies2:
            player.calc_damage(enemy2.damage)

            health_bar.update_info(player.get_damage_percentage())

            if player.health <= 0:
                done = True

        # --- DRAW ---
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        screen.blit(health_bar, (10, 10))
        screen.blit(score_text, (10, 35))
        screen.blit(level_text, (10, 85))
        pygame.display.flip()

        clock.tick(60)

    # Display final score:
    print("Thanks for playing!")
    print("Final score is:", player.points)

    pygame.quit()


if __name__ == "__main__":
    game()
