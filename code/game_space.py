import pygame, controls
from code2.gun import Gun
from pygame.sprite import Group
from code2.Stats import Stats
from code2.score import Score

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space war")
    bg_color = (0, 0, 0)

    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Score(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.updateGUN()
            controls.displeyUpdate(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.Update_bullets(screen,stats, sc, inos, bullets)
            controls.updateRun(stats, screen, sc, gun, inos, bullets)



run()