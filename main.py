import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger")

BG = pygame.transform.scale(pygame.image.load("bd.jpeg"), (WIDTH, HEIGHT))

PLAYER_W, PLAYER_H = 40, 60
PLAYER_V = 5

FONT = pygame.font.SysFont("comicsans", 30)

STAR_W, STAR_H = 10, 20
STAR_V = 3

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))
    pygame.draw.rect(WIN, "red", player)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text,(10,10))

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT-PLAYER_H,
                         PLAYER_W, PLAYER_H)

    clock = pygame.time.Clock()
    start_time = time.time()

    star_add_increament = 2000
    star_count = 0
    stars = []
    hit = False

    while run:
        clock.tick(100)
        elapsed_time = time.time() - start_time

        star_count += clock.tick(100)
        if star_count > star_add_increament:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_W)
                star = pygame.Rect(star_x, -STAR_H, STAR_W, STAR_H)
                stars.append(star)

            star_add_increament = max(200, star_add_increament - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame. K_LEFT] and player.x - PLAYER_V >= 0:
            player.x -= PLAYER_V
        if keys[pygame. K_RIGHT] and player.x + PLAYER_W + PLAYER_V <= WIDTH:
            player.x += PLAYER_V

        for star in stars[:]:
            star.y += STAR_V
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("Game Over!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2,
                                 HEIGHT/2-lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)
    pygame.quit()

if __name__ == "__main__":
    main()

