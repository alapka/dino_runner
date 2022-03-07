import pygame, sys, random, dino

WIDTH, HEIGHT = 1280, 720
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino runner")

ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground, (1280,20))
ground_pos_x = 0
ground_rect = ground.get_rect(center=(640, 400))

game_speed = 5
# Groups
dino_group = pygame.sprite.GroupSingle()
# Objects
dinosaur = dino.Dino(100, 360)

dino_group.add(dinosaur)

def draw_window():
    window.fill((255,255,255))
    dino_group.update()
    dino_group.draw(window)
    global ground_pos_x
    ground_pos_x -= 1
    window.blit(ground, (ground_pos_x, 360))
    window.blit(ground, (ground_pos_x + 1280, 360))

    if ground_pos_x <= -1280:
        ground_pos_x = 0
    pygame.display.update()

def main():
    global game_speed

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        game_speed += 0.0025
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()