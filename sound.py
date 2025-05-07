import os
import sys
import pygame

pygame.mixer.init()

# Global flag
background_music_playing = False

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Load sounds
try:
    pygame.mixer.music.load(resource_path("sounds/background.wav"))
    eat_sound = pygame.mixer.Sound(resource_path("sounds/eat.wav"))
    death_sound = pygame.mixer.Sound(resource_path("sounds/death.wav"))
    button_click_sound = pygame.mixer.Sound(resource_path("sounds/button_click.wav"))
    clock_sound = pygame.mixer.Sound(resource_path("sounds/soundscrate-clock2.mp3"))
except pygame.error as e:
    print(f"[Sound Load Error] {e}")
    eat_sound = None
    death_sound = None
    button_click_sound = None
    clock_sound = None

def play_background_music():
    global background_music_playing
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)
        background_music_playing = True

def stop_background_music():
    global background_music_playing
    pygame.mixer.music.stop()
    background_music_playing = False

def play_clock_sound():
    if clock_sound:
        clock_sound.play(loops=-1)

def stop_clock_sound():
    if clock_sound:
        clock_sound.stop()

def play_sound(sound):
    if sound:
        sound.play()
