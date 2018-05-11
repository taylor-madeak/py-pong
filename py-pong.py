from constants import *
import pygame
from playfield import *


pygame.init()

# Set the width and height of the screen [width, height)
screen = pygame.display.set_mode(DISPLAY_SIZE)

# Title bar text
pygame.display.set_caption("PyPong")

# Main game loop conditional
done = False

# Screen update
clock = pygame.time.Clock()

# Instantiate objects
ball = Ball(pygame.Surface(PLAYFIELD_SIZE).get_rect())
playfield = Playfield(PLAYFIELD_SIZE, ball)

# Main game loop
while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.event.pump()

    # Clear the screen

    # update all_sprites

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    screen.fill(BLACK)

    # Drawing code

    # draw the playfield to the screen
    playfield.draw(screen)

    # Check for player 1 inputs
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_w]:
        playfield.paddle1.move_up()
    if key_state[pygame.K_s]:
        playfield.paddle1.move_down()

    # Check for player 2 inputs
    if key_state[pygame.K_UP]:
        playfield.paddle2.move_up()
    if key_state[pygame.K_DOWN]:
        playfield.paddle2.move_down()


    # draw all_sprites group to the screen
    # all_sprites.draw(screen)

    # Update the screen with the draw
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Quit
pygame.quit()
