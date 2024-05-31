import sys
import random
import pygame
from grid import adjust_grid, gen, draw_grid
from settings import *


def handle_events(positions):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(positions)

        if event.type == pygame.KEYDOWN:
            handle_key_down(event, positions)

    return True


def handle_mouse_click(positions):
    logger.debug("Handling mouse click...")
    x, y = pygame.mouse.get_pos()
    col = x // TILE_SIZE
    row = y // TILE_SIZE
    pos = (col, row)

    if pos in positions:
        positions.remove(pos)
    else:
        positions.add(pos)


def handle_key_down(event, positions):
    logger.debug("Handling key down...")
    global playing, count, update_freq, max_iterations

    if event.key == pygame.K_SPACE:
        playing = not playing

    if event.key == pygame.K_c:
        positions.clear()
        playing = False
        count = 0

    if event.key == pygame.K_g:
        positions.clear()
        playing = False
        count = 0
        positions.update(gen(random.randrange(4, 10) * GRID_WIDTH, sys.argv[1] if len(sys.argv) > 2 else None))


def main():
    logger.debug("Starting main function...")
    global playing, count, update_freq, max_iterations

    running = True
    playing = False
    count = 0
    update_freq = 100

    positions = set()
    current_iteration = 0
    max_iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_freq:
            count = 0
            positions = adjust_grid(positions)
            current_iteration += 1

            if current_iteration >= max_iterations:
                playing = False

        pygame.display.set_caption("Playing" if playing else "Paused")

        running = handle_events(positions)

        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()
