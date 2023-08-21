import pygame.font
from code2.gun import Gun
from pygame.sprite import Group

class Score():

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (237, 28, 35)
        self.font = pygame.font.SysFont(None, 30)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        self.score_i = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_i.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score.get_rect()
        self.high_score_centerx = self.score_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_guns(self):
        self.guns = Group()
        for gun_num in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_num * gun.rect.width
            gun.rect.top = 20
            self.guns.add(gun)

    def show_score(self):
        self.screen.blit(self.score_i, self.score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
        self.guns.draw(self.screen)

