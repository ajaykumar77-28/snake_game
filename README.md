# snake_game
Snake Game (Python + Pygame) This project is a feature-rich Snake Game implemented using Pygame, designed for fullscreen gameplay with immersive graphics and sound effects. The game is modularized across multiple files for better structure and maintainability.

_**Core Features**_

**Game Mechanics (snake.py)**

Classic snake gameplay: the snake moves in a grid, eats food to grow longer, and the game ends if it collides with itself or the screen boundaries.

Snake and food are drawn using pygame.Rect, with food randomly repositioned on consumption.

Real-time score and high score display above the game area.

Adjustable block size and game speed for tuning difficulty.

White border around the playable area.

Maintains a per-session high score.

**Pause and Resume**
Pressing P pauses or resumes the game.

Pause screen with options:

Resume

Quit to Home

Exit Game

Background music plays during pause; ticking clock sound is paused.

**Game Over**
On collision, a Game Over screen appears with options:

Continue (restarts the game)

Quit to Home

Exit Game

Resets game variables upon restart.

**Sounds and Music**
Uses pygame.mixer for sound:

Background music

Clock ticking during gameplay

Clicks on button interactions

Eat sound when food is consumed

Death sound on game over

Sound functions are modularized in sound.py.

**GUI and Navigation (screen.py)**
Fullscreen UI using Pygame's display info for dynamic scaling.

Uses a layout box system for buttons and text in center-aligned UIs.

Start Screen:

A snake icon button that leads to the next screen.

Game Lobby Screen (snake_screen_hold):

Displays the player's name and high score.

Buttons: New Game, Quit, Exit Game

Uses background images (background.jpg, snake.png) and icons for immersive visuals.

**Structure and Flow**
1. main.py:
Launches the game via info_screen() from screen.py.

2. screen.py:
Manages all non-gameplay UI:

Start screen

Snake game lobby

Exit game logic

Loads images and handles UI interactions.

3. snake.py:
Manages all gameplay logic:

Game loop, snake behavior, food handling, collisions

Pause and game over screens

**Technical Highlights**
Modular Design: Clearly separated concerns:

main.py for entry point

screen.py for screens and UI

snake.py for core gameplay

sound.py for audio

Resource Pathing: Uses resource_path() to handle paths for compatibility with PyInstaller.

Fullscreen Adaptability: Uses the user's screen resolution dynamically for all rendering.
