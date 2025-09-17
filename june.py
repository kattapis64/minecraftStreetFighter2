import subprocess
import sys
import time
import pygame
import random
import requests
import io
from PIL import Image

# ----------------- Install required packages -----------------
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")

install_package("pygame")
install_package("requests")
install_package("Pillow")
time.sleep(1)

# ----------------- Helper function to load image from URL -----------------
def load_image_from_url(url, size=None, flip=False):
    img_bytes = requests.get(url).content
    image = Image.open(io.BytesIO(img_bytes)).convert("RGBA")
    if size:
        # Ensure positive dimensions
        width = max(1, size[0])
        height = max(1, size[1])
        image = image.resize((width, height))
    if flip:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    return pygame.image.fromstring(image.tobytes(), image.size, image.mode)

# ----------------- Initialize Pygame -----------------
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# ----------------- Game Variables -----------------
gravity = 0.5
bird_movement = 0
game_active = True
score = 0
pipe_list = []
pipe_width = 80
pipe_gap = 250
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
BLUE = (135, 206, 250)

# ----------------- Load Images -----------------
url_bird = 'https://raw.githubusercontent.com/kattapis64/flappyBirdClone/main/1757940339607.png'
url_pipe = 'https://raw.githubusercontent.com/kattapis64/flappyBirdClone/main/pipe.png'

bird_surf = load_image_from_url(url_bird, size=(68*2, 39*2))
bird = bird_surf.get_rect(center=(50, HEIGHT // 2))

# ----------------- Functions -----------------
def create_pipe():
    # Ensure pipes have positive height
    min_height = pipe_gap + 50
    max_height = HEIGHT - 50
    height = random.randint(min_height, max_height)

    # Top pipe
    top_height = max(10, height - pipe_gap)
    top_surf = load_image_from_url(url_pipe, size=(pipe_width, top_height), flip=True)
    top_rect = top_surf.get_rect(midbottom=(WIDTH + pipe_width//2, height - pipe_gap))

    # Bottom pipe
    bottom_height = max(10, HEIGHT - height)
    bottom_surf = load_image_from_url(url_pipe, size=(pipe_width, bottom_height))
    bottom_rect = bottom_surf.get_rect(midtop=(WIDTH + pipe_width//2, height))

    top = {"rect": top_rect, "surface": top_surf, "scored": False}
    bottom = {"rect": bottom_rect, "surface": bottom_surf, "scored": False}
    return top, bottom

def move_pipes(pipes):
    for pipe in pipes:
        pipe["rect"].centerx -= 4
    return [pipe for pipe in pipes if pipe["rect"].right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe["surface"], pipe["rect"])

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe["rect"]):
            return False
    if bird.top <= 0 or bird.bottom >= HEIGHT:
        return False
    return True

def reset_game():
    global bird_movement, score, pipe_list, game_active
    bird.center = (50, HEIGHT // 2)
    bird_movement = 0
    score = 0
    pipe_list.clear()
    game_active = True

# ----------------- Main Game Loop -----------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_movement = -8
                else:
                    reset_game()
        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

    screen.fill(BLUE)

    if game_active:
        # Bird movement
        bird_movement += gravity
        bird.centery += int(bird_movement)
        screen.blit(bird_surf, bird)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Score
        for pipe in pipe_list:
            if pipe["rect"].centerx < bird.centerx and not pipe["scored"]:
                score += 0.5
                pipe["scored"] = True
        score_text = font.render(f"Score: {int(score)}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
    else:
        game_over_text = font.render(f"Game Over! Score: {int(score)} \n\tPress SPACE", True, (0, 0, 0))
        screen.blit(game_over_text, (20, HEIGHT // 2))

    pygame.display.update()
    clock.tick(60)
