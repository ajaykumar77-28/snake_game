import pygame
import random
from screen import player_name, resource_path
from sound import play_background_music, play_sound, button_click_sound, play_clock_sound, stop_clock_sound, stop_background_music, death_sound, eat_sound  #  Include clock_sound

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set up fullscreen
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h - 50  # Subtract HEADER_HEIGHT to accommodate top bar

BLOCK_SIZE = 10
SPEED = 15
HEADER_HEIGHT = 50
BORDER_THICKNESS = 5

# Create fullscreen window
screen = pygame.display.set_mode((WIDTH, HEIGHT + HEADER_HEIGHT), pygame.FULLSCREEN)


# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Load background image
gameplay_img = pygame.image.load(resource_path("Img/snake.png"))
gameplay_img = pygame.transform.scale(gameplay_img, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)
button_font = pygame.font.SysFont(None, 40)

# Initialize high score
highest_score = 0


def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1] + HEADER_HEIGHT, BLOCK_SIZE, BLOCK_SIZE))


def display_score(score, highest_score):
    screen.fill(BLACK, (0, 0, WIDTH, HEADER_HEIGHT))
    text = font.render(f"{player_name} | Score: {score}  High Score: {highest_score}", True, WHITE)
    screen.blit(text, [10, 10])


def draw_border():
    """Draws a white border around the playable area."""
    pygame.draw.rect(screen, WHITE, (0, HEADER_HEIGHT , WIDTH, BORDER_THICKNESS - 4))  # Top border
    pygame.draw.rect(screen, WHITE, (0, HEADER_HEIGHT, BORDER_THICKNESS, HEIGHT -4))  # Left border
    pygame.draw.rect(screen, WHITE, (WIDTH - BORDER_THICKNESS, HEADER_HEIGHT, BORDER_THICKNESS -4, HEIGHT))  # Right border
    pygame.draw.rect(screen, WHITE, (0, HEIGHT + HEADER_HEIGHT - BORDER_THICKNESS, WIDTH, BORDER_THICKNESS -4))  # Bottom border


def game_over_screen():
    play_sound(death_sound)
    play_background_music()
    while True:
        # Fill the screen with the background image
        screen.blit(gameplay_img, (0, HEADER_HEIGHT))

        # Game Over Text (Centered)
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, [WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 6])

        # Player Name Text (Centered)
        player_text = font.render(f"Player: {player_name}", True, WHITE)
        screen.blit(player_text, [WIDTH // 2 - player_text.get_width() // 2, HEIGHT // 4])

        # Continue Button (Centered)
        continue_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 40, 200, 60)
        pygame.draw.rect(screen, GREEN, continue_button, border_radius=10)
        continue_text = button_font.render("Continue", True, WHITE)
        screen.blit(continue_text, [continue_button.x + (continue_button.width - continue_text.get_width()) // 2, continue_button.y + (continue_button.height - continue_text.get_height()) // 2])

        # Quit Button (Centered)
        quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 40, 200, 60)
        pygame.draw.rect(screen, RED, quit_button, border_radius=10)
        quit_text = button_font.render("Quit", True, WHITE)
        screen.blit(quit_text, [quit_button.x + (quit_button.width - quit_text.get_width()) // 2, quit_button.y + (quit_button.height - quit_text.get_height()) // 2])

        # Exit Button (Centered)
        exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 60)
        pygame.draw.rect(screen, RED, exit_button, border_radius=10)
        exit_text = button_font.render("Exit Game", True, WHITE)
        screen.blit(exit_text, [exit_button.x + (exit_button.width - exit_text.get_width()) // 2, exit_button.y + (exit_button.height - exit_text.get_height()) // 2])

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    if not stop_background_music():
                        stop_background_music()
                    game_loop()
                    return
                elif quit_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    from screen import start_screen
                    start_screen()
                    return
                elif exit_button.collidepoint(event.pos):
                    #play_sound(button_click_sound)
                    from screen import exit_game
                    exit_game()

def pause_screen():
    paused = True
    stop_clock_sound()
    play_background_music()

    # Button dimensions
    button_width, button_height = 200, 60
    # Calculate the positions of buttons (centered)
    resume_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 40, button_width, button_height)
    quit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 40, button_width, button_height)
    exit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 120, button_width, button_height)

    while paused:
        # Fill the screen with background image
        screen.blit(gameplay_img, (0, HEADER_HEIGHT))

        # Paused Text (Centered)
        pause_text = font.render("Game Paused", True, WHITE)
        screen.blit(pause_text, [WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 4])

        # Resume Button (Centered)
        pygame.draw.rect(screen, GREEN, resume_button, border_radius=10)
        resume_text = button_font.render("Resume", True, WHITE)
        screen.blit(resume_text, [resume_button.x + (resume_button.width - resume_text.get_width()) // 2, resume_button.y + (resume_button.height - resume_text.get_height()) // 2])

        # Quit Button (Centered)
        pygame.draw.rect(screen, RED, quit_button, border_radius=10)
        quit_text = button_font.render("Quit", True, WHITE)
        screen.blit(quit_text, [quit_button.x + (quit_button.width - quit_text.get_width()) // 2, quit_button.y + (quit_button.height - quit_text.get_height()) // 2])

        # Exit Button (Centered)
        pygame.draw.rect(screen, RED, exit_button, border_radius=10)
        exit_text = button_font.render("Exit Game", True, WHITE)
        screen.blit(exit_text, [exit_button.x + (exit_button.width - exit_text.get_width()) // 2, exit_button.y + (exit_button.height - exit_text.get_height()) // 2])

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    play_clock_sound()
                    stop_background_music()
                    paused = False
                elif quit_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    from screen import start_screen
                    start_screen()
                    return
                elif exit_button.collidepoint(event.pos):
                    #play_sound(button_click_sound)
                    from screen import exit_game
                    exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play_clock_sound()
                    stop_background_music()
                    paused = False



def game_loop():

    global highest_score
    if not stop_background_music():
        stop_background_music()
        play_clock_sound()


    game_over = False
    game_paused = False

    x, y = WIDTH // 2, (HEIGHT // 2) // BLOCK_SIZE * BLOCK_SIZE
    x_change, y_change = BLOCK_SIZE, 0  # Start moving right

    snake_body = [[x, y]]
    length_of_snake = 1
    score = 0

    food_x = random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
    food_y = random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE

    screen.blit(gameplay_img, (0, HEADER_HEIGHT))
    pygame.display.update()


    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_paused = not game_paused
                elif not game_paused:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and x_change == 0:
                        x_change = -BLOCK_SIZE
                        y_change = 0
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and x_change == 0:
                        x_change = BLOCK_SIZE
                        y_change = 0
                    elif (event.key == pygame.K_UP or event.key == pygame.K_w) and y_change == 0:
                        y_change = -BLOCK_SIZE
                        x_change = 0
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and y_change == 0:
                        y_change = BLOCK_SIZE
                        x_change = 0

        if game_paused:
            pause_screen()
            game_paused = False

        x += x_change
        y += y_change

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            stop_clock_sound()
            game_over_screen()
            return


        # Update snake body
        snake_body.append([x, y])
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check for collision with itself
        if [x, y] in snake_body[:-1]:
            game_over_screen()
            return

        # Check if snake eats food
        if x == food_x and y == food_y:
            play_sound(eat_sound)
            score += 1
            length_of_snake += 1
            food_x = random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
            food_y = random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
            if score > highest_score:
                highest_score = score

        screen.blit(gameplay_img, (0, HEADER_HEIGHT))
        draw_border()  # Draw the white border
        pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y + HEADER_HEIGHT, BLOCK_SIZE, BLOCK_SIZE))

        draw_snake(snake_body)
        display_score(score, highest_score)
        pygame.display.update()

        clock.tick(SPEED)
