import pygame
import os
import sys
from sound import play_background_music, play_sound, button_click_sound, play_clock_sound, stop_clock_sound, stop_background_music  #  Include clock_sound

# Initialize pygame
pygame.init()

# tart background music immediately
play_background_music()

# Create fullscreen game window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Global player name
player_name = "Name"

# Handle paths correctly in EXE mode
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Load background image
BACKGROUND_IMG = pygame.image.load(resource_path("Img/background.jpg"))
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

# Load snake background image
SNAK_IMG = pygame.image.load(resource_path("Img/snake.png"))
SNAK_IMG = pygame.transform.scale(SNAK_IMG, (WIDTH, HEIGHT))

# Load only snake icon
snake_icon = pygame.image.load(resource_path("Img/snake_icon.png"))
snake_icon = pygame.transform.scale(snake_icon, (80, 80))

# Create game window
pygame.display.set_caption("Snake Game")

# Font setup
font = pygame.font.SysFont(None, 40)

# Snake game button
button_size = 100
snake_button = pygame.Rect((WIDTH - button_size) // 2, (HEIGHT - button_size) // 2, button_size, button_size)

def snake_screen_hold(high_score=0):
    global player_name
    while True:
        screen.blit(SNAK_IMG, (0, 0))

        # Layout box dimensions
        layout_width = WIDTH * 0.3
        layout_height = HEIGHT * 0.4
        layout_x = (WIDTH - layout_width) // 2
        layout_y = (HEIGHT - layout_height) // 2
        layout_rect = pygame.Rect(layout_x, layout_y, layout_width, layout_height)

        # Draw layout background rectangle
        pygame.draw.rect(screen, BLACK, layout_rect, border_radius=20)

        # Texts and buttons inside layout
        title_text = font.render("Snake Game", True, WHITE)
        screen.blit(title_text, (layout_rect.centerx - title_text.get_width() // 2, layout_y + 30))

        name_text = font.render(f"{player_name}", True, WHITE)
        screen.blit(name_text, (layout_rect.centerx - name_text.get_width() // 2, layout_y + 80))

        high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(high_score_text, (layout_rect.centerx - high_score_text.get_width() // 2, layout_y + 130))

        # New Game Button
        new_game_button = pygame.Rect(layout_rect.centerx - 100, layout_y + 200, 200, 60)
        pygame.draw.rect(screen, GREEN, new_game_button, border_radius=20)
        new_game_text = font.render("New Game", True, WHITE)
        screen.blit(new_game_text, (new_game_button.centerx - new_game_text.get_width() // 2, new_game_button.y + 15))

        # Quit Button
        quit_button = pygame.Rect(layout_rect.centerx - 100, layout_y + 280, 200, 60)
        pygame.draw.rect(screen, RED, quit_button, border_radius=20)
        quit_text = font.render("Quit", True, WHITE)
        screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.y + 15))

        # Exit Button
        exit_button = pygame.Rect(layout_rect.centerx - 100, layout_y + 360, 200, 60)
        pygame.draw.rect(screen, RED, exit_button, border_radius=10)
        exit_text = font.render("Exit Game", True, WHITE)
        screen.blit(exit_text, (exit_button.centerx - exit_text.get_width() // 2, exit_button.y + 15))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_sound(button_click_sound)
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    import snake
                    snake.game_loop()
                    return
                elif quit_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    start_screen()
                    return
                elif exit_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    exit_game()

def start_screen():
    while True:
        screen.blit(BACKGROUND_IMG, (0, 0))

        # Draw the snake button
        pygame.draw.rect(screen, GREEN, snake_button, border_radius=20)
        icon_rect = snake_icon.get_rect(center=snake_button.center)
        screen.blit(snake_icon, icon_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_sound(button_click_sound)
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if snake_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    snake_screen_hold()

def exit_game():
    pygame.quit()  # Close the pygame window
    sys.exit()

def info_screen():
    global player_name
    play_background_music()
    input_active = False

    # Input & button dimensions
    box_width, box_height = 300, 50
    button_width, button_height = 200, 50

    # Center positions
    input_box = pygame.Rect((WIDTH - box_width) // 2, HEIGHT // 2, box_width, box_height)
    enter_button = pygame.Rect((WIDTH - button_width) // 2, input_box.y + 80, button_width, button_height)

    while True:
        screen.blit(BACKGROUND_IMG, (0, 0))

        # Background layout rectangle
        layout_width = WIDTH * 0.3
        layout_height = HEIGHT * 0.3
        layout_rect = pygame.Rect(
            (WIDTH - layout_width) // 2,
            (HEIGHT - layout_height) // 2,
            layout_width,
            layout_height
        )

        layout_width = WIDTH * 0.29
        layout_height = HEIGHT * 0.29
        layout_rect1 = pygame.Rect(
            (WIDTH - layout_width) // 2,
            (HEIGHT - layout_height) // 2,
            layout_width,
            layout_height
        )

        pygame.draw.rect(screen, BLACK, layout_rect, border_radius=20)
        pygame.draw.rect(screen, RED, layout_rect1, border_radius=20)

        # Render title text
        text = font.render("Enter the name:", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, input_box.y - 40))
        screen.blit(text, text_rect)

        # Input box
        pygame.draw.rect(screen, WHITE, input_box, border_radius=10)
        if not input_active and player_name == "Name":
            placeholder_text = font.render(player_name, True, (100, 100, 100))  # Subtle gray
            screen.blit(placeholder_text, (input_box.x + 10, input_box.y + 10))
        else:
            input_text = font.render(player_name, True, BLACK)
            screen.blit(input_text, (input_box.x + 10, input_box.y + 10))

        # Enter button
        pygame.draw.rect(screen, GREEN, enter_button, border_radius=10)
        enter_text = font.render("Enter", True, WHITE)
        enter_text_rect = enter_text.get_rect(center=enter_button.center)
        screen.blit(enter_text, enter_text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_sound(button_click_sound)
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    input_active = True
                    player_name = ""
                elif enter_button.collidepoint(event.pos):
                    play_sound(button_click_sound)
                    start_screen()
                    return
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    play_sound(button_click_sound)
                    start_screen()
                    return
                elif event.key == pygame.K_BACKSPACE:
                    play_sound(button_click_sound)
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

#Start the game
info_screen()
