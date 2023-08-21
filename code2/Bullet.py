import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        """bullet in gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 237, 28, 35
        self.speed = 5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """moving the bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bul(self):
        """bullet on display"""
        pygame.draw.rect(self.screen, self.color, self.rect)