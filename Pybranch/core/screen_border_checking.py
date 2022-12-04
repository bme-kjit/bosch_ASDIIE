import pygame


class ScreenBorderChecking:

    def __init__(self):
        self.screen_height = int
        self.screen_width = int
        self.sprite = pygame.sprite.Sprite

    def border_checking(self, sprite: pygame.sprite.Sprite, screen_height: int, screen_width: int) -> None:
        """
            The other side of the screen displays the movable sprite
        @args:
            sprite [pygame.sprite.Sprite] - the movable sprite
            (screen_height, screen_width) [int, int]-the screen sizes
        """
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.sprite = sprite

        if self.sprite.rect.top < 0:
            self.sprite.rect.move_ip(0, self.screen_height)
        if self.sprite.rect.bottom > self.screen_height:
            self.sprite.rect.move_ip(0, -self.screen_height)
        if self.sprite.rect.left < 0:
            self.sprite.rect.move_ip(self.screen_width, 0)
        if self.sprite.rect.right > self.screen_width:
            self.sprite.rect.move_ip(- self.screen_width, 0)
