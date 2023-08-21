import pygame, sys
import time
from code2.Bullet import Bullet
from code2.ino import Ino

def events(screen, gun, bullets):
    """processing events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            #right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
                #left
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        #right
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
                #left
            elif event.key == pygame.K_a:
                gun.mleft = False

def displeyUpdate(bg_color, screen, stats, sc, gun,inos, bullets):
    """update display"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bul()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def Update_bullets(screen,stats,sc, inos, bullets):
    """update position bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collections = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collections:
        for inos in collections.values():
            stats.score += 1 * len(inos)
        stats.score += 1
        sc.image_score()
        check_Score(stats, sc)
        sc.image_guns()

    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def gun_kill(stats, screen, sc, gun, inos, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()

        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def updateRun(stats, screen, sc, gun, inos, bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc, gun, inos, bullets):
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break

def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 600 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            ino.add(inos)


def check_Score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('HighScore.txt', 'w') as f:
            f.write(str(stats.high_score))

