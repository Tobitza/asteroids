import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def game_over(screen, clock):
    # Text generation
    title_font = pygame.font.Font(None, 80)
    info_font = pygame.font.Font(None, 36)

    title = title_font.render("GAME OVER", False, "white")
    info = info_font.render("Press Escape to quit", False, "white")

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    info_rect = info.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

    # Game Over screen loop
    while True:
        # Exit game via window's X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # Screen refresh & generation
        screen.fill("black")
        screen.blit(title, title_rect)
        screen.blit(info, info_rect)

        pygame.display.flip()
        clock.tick(60)