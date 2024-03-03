import pygame


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hover_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.font = font
        self.base_color = base_color
        self.hovering_color = hover_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return True

        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)