import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 50
TRIANGLE_SIZE = 40
SQUARE_COLOR = (0, 255, 0)  # Green
TRIANGLE_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black
HEALTH_COLOR = (255, 255, 255)  # White
GRAVITY = 0.8
JUMP_STRENGTH = -15
MOVE_SPEED = 5
MAX_HEALTH = 100

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Green Square Game")

# Font for health
font = pygame.font.SysFont("Arial", 24)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill(SQUARE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - SQUARE_SIZE)
        self.vel_y = 0
        self.health = MAX_HEALTH

    def update(self):
        # Gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Prevent falling through the ground
        if self.rect.bottom > SCREEN_HEIGHT - 50:  # Ground level
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.vel_y = 0

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += MOVE_SPEED

        # Ensure the player stays within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def jump(self):
        if self.rect.bottom == SCREEN_HEIGHT - 50:  # Only jump if on the ground
            self.vel_y = JUMP_STRENGTH

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

# Triangle class (red)
class Triangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TRIANGLE_SIZE, TRIANGLE_SIZE))
        self.image.fill(0)  # Transparent background
        pygame.draw.polygon(self.image, TRIANGLE_COLOR, [(0, TRIANGLE_SIZE), (TRIANGLE_SIZE // 2, 0), (TRIANGLE_SIZE, TRIANGLE_SIZE)])
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

# Set up sprite groups
player = Player()
triangle = Triangle()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(triangle)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update game state
    all_sprites.update()

    # Check for collisions
    if player.rect.colliderect(triangle.rect):
        player.take_damage(10)

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw all sprites
    all_sprites.draw(screen)

    # Draw health
    health_text = font.render(f"Health: {player.health}", True, HEALTH_COLOR)
    screen.blit(health_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()