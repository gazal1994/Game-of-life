import logging

import pygame

pygame.init()

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 170, 255)

WIDTH, HEIGHT = 400, 400
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
