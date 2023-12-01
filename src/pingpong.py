import pygame
import random
from bot import move_opposite_paddle

# Initialize Pygame
pygame.init()

# Set the initial state for the game loop
running = True

def ping_pong(screen, clock, width, height):
    """
    Main Function for the Ping Pong game.

    Parameters:
    - screen: Pygame display surface
    - clock: Pygame clock object
    - width: Width of the game window
    - height: Height of the game window
    """

    ### Initialize variables for the paddles, ball, and scores ###
    paddle_xsize = 25
    paddle_ysize = 150
    paddle_color = (255, 255, 255)
    paddle_x = 50
    paddle_y = height // 2
    paddle_speed = 500

    opposite_paddle_x = width - paddle_x - paddle_xsize
    opposite_paddle_y = 50

    pressed_keys = {}
    
    ball_radius = 15
    ball_color = (255, 255, 255)
    ball_x = width // 2
    ball_y = height // 2
    ball_speed = 400
    ball_velocity = [-ball_speed / 2, ball_speed / 2]

    paddle_score = 0
    opposite_paddle_score = 0

    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 70)

    running = True
    #################################################################

    # Main Game Loop
    while running:
        # Calculate the time passed since the last frame ###
        dt = clock.tick(60) / 1000.0
        ####################################################

        ### Handle Pygame events ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                pressed_keys[event.key] = True
            elif event.type == pygame.KEYUP:
                pressed_keys[event.key] = False
        ##############################

        ### Move the player's paddle based on key presses ###
        if pressed_keys.get(pygame.K_UP):
            paddle_y -= paddle_speed * dt
        if pressed_keys.get(pygame.K_DOWN):
            paddle_y += paddle_speed * dt
            paddle_y = max(0, min(height - paddle_ysize, paddle_y))
        ######################################################


        ### Update the ball's position ###
        ball_x += ball_velocity[0] * dt
        ball_y += ball_velocity[1] * dt
        ##################################

        ### Check for collisions with paddles ###
        if (
            paddle_x < ball_x < paddle_x + paddle_xsize and
            paddle_y < ball_y < paddle_y + paddle_ysize
        ):
            ball_velocity[0] = -ball_velocity[0]  # Bounce off the paddles
            ball_velocity[1] += random.randint(-1, 1) * ball_speed

        elif (
            opposite_paddle_x < ball_x < opposite_paddle_x + paddle_xsize and
            opposite_paddle_y < ball_y < opposite_paddle_y + paddle_ysize
        ):
            # Bounce off the opposite paddle
            ball_velocity[0] = -ball_velocity[0]  # Bounce in the opposite x-direction
            ball_velocity[1] += random.uniform(-0.5, 0.5) * ball_speed  # Use random.uniform for smoother bouncing
        ##############################################

        ### Check for collisions with walls ###
        if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
            ball_velocity[1] = -ball_velocity[1]

        ### Check for scoring ###
        if ball_x + ball_radius < 0:
            opposite_paddle_score += 1
            ball_x = width // 2
            ball_y = height // 2
            ball_velocity = [-ball_speed, 0]
        elif ball_x - ball_radius > width:
            paddle_score += 1
            ball_x = width // 2
            ball_y = height // 2
            ball_velocity = [ball_speed, 0]


        ### Moving the bot using the move_opposite_paddle function inside the bot.py file ###
        opposite_paddle_y = move_opposite_paddle(opposite_paddle_y, ball_y, paddle_speed, dt)
        #####################################################################################

        ### Clear the screen ###
        screen.fill((0, 0, 0))
        ########################

        ### Drawing the center line ###
        pygame.draw.line(screen, (255, 255, 255), (width // 2, 0), (width // 2, height), 2)
        ###############################

        ### Draw the paddles and ball ###
        pygame.draw.rect(screen, paddle_color, (paddle_x, paddle_y, paddle_xsize, paddle_ysize))
        pygame.draw.rect(screen, paddle_color, (opposite_paddle_x, opposite_paddle_y, paddle_xsize, paddle_ysize))
        pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
        #################################

        ### Rendering Text for the score ###
        paddle_text = font.render(str(paddle_score), True, (255, 255, 255))
        opposite_paddle_text = font.render(str(opposite_paddle_score), True, (255, 255, 255))
        screen.blit(paddle_text, (width // 4, 20))
        screen.blit(opposite_paddle_text, (3 * width // 4 - paddle_text.get_width(), 50))
        ######################################

        ### Update the display ###
        pygame.display.flip()
        ##########################

pygame.quit() # Application shut down when exiting the while loop