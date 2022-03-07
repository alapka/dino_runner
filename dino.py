import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x = x_pos
        self.y = y_pos

        self.running_sprites = []
        self.ducking_sprites = []

        self.running_sprites.append(pygame.transform.scale(pygame.image.load("assets/Dino1.png"), (60, 80)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load("assets/Dino2.png"), (60, 80)))

        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load("assets/DinoDucking1.png"), (60, 80)))
        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load("assets/DinoDucking2.png"), (60, 80)))
        

        self.current_image_index = 0
        self.image = self.running_sprites[self.current_image_index]
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.ticks_elapsed = 0
        self.FRAME_RATE = 5

        self.velocity = 50
        self.gravity = 4.5
        self.ducking = False

    def update(self):
        if self.ticks_elapsed <  self.FRAME_RATE:
            self.ticks_elapsed += 1
            return
        self.animate()
        self.ticks_elapsed = 0

    def animate(self):
        self.current_image_index += 1
        if self.current_image_index > 1:
            self.current_image_index = 0
        self.image = self.running_sprites[self.current_image_index]

    def duck(self):
        self.ducking = True
        self.rect.centery = 380
    
    def unduck(self):
        self.ducking = False
        self.rect.center = 360
