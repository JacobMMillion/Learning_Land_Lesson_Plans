# Import the pygame library so we can use it
import pygame

# Initialize pygame (this sets up everything we need to use it)
pygame.init()

# Initialize fonts
pygame.font.init()

# Set up the size of the window (width, height in pixels)
screen_width = 800  # Width of the screen in pixels
screen_height = 600  # Height of the screen in pixels
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Enemy and Health with Pygame")

# Choose a color for the screen background
background_color = (135, 206, 235)  # Light blue

# Choose a color for the character (a simple rectangle)
character_color = (0, 255, 0)  # Green

# Set the size of the character
character_width = 50  # Width of the rectangle
character_height = 50  # Height of the rectangle

# Set the starting position of the character
# note: determined by upper left corner
character_x = 0  # Start on left of screen
character_y = screen_height - character_height  # Start on the ground

# Set the speed of the character (how many pixels it moves per frame)
character_speed = 5

# Player health
player_health = 100

# Gravity and jumping
gravity = 0.5
character_vy = 0  # vertical speed
jump_strength = 10
is_on_ground = False

# Initialize font
font = pygame.font.Font(None, 36)

# Enemy triangle
enemy_color = (255, 0, 0)  # Red
enemy_size = 50
enemy_x = 300
enemy_y = screen_height - enemy_size

# Damage cooldown (to prevent health from decreasing rapidly)
damage_cooldown = 0

# This variable will keep our game loop running
running = True

# To control the frame rate
clock = pygame.time.Clock()

# Main game loop
while running:
    # Set frame rate
    clock.tick(60)  # 60 frames per second

    # Check for events (like key presses or closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the close button was clicked
            running = False  # This will end the game loop

    # Get all the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Move the character based on arrow key input
    if keys[pygame.K_LEFT]:  # Move left
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:  # Move right
        character_x += character_speed
    if keys[pygame.K_SPACE] and is_on_ground:  # Jump
        character_vy = -jump_strength
        is_on_ground = False

    # Apply gravity
    character_vy += gravity
    character_y += character_vy

    # Check for ground collision
    if character_y >= screen_height - character_height:
        character_y = screen_height - character_height
        character_vy = 0
        is_on_ground = True

    # Keep the character within the screen bounds
    if character_x < 0:
        character_x = 0
    if character_x > screen_width - character_width:
        character_x = screen_width - character_width

    # Enemy triangle points
    enemy_points = [
        (enemy_x, enemy_y),  # Top point
        (enemy_x - enemy_size / 2, enemy_y + enemy_size),  # Bottom left
        (enemy_x + enemy_size / 2, enemy_y + enemy_size)  # Bottom right
    ]

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the character (a red rectangle)
    pygame.draw.rect(screen, character_color, (character_x, character_y, character_width, character_height))

    # Draw the enemy triangle
    pygame.draw.polygon(screen, enemy_color, enemy_points)

    # Check collision
    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)
    enemy_rect = pygame.Rect(enemy_x - enemy_size / 2, enemy_y, enemy_size, enemy_size)

    if character_rect.colliderect(enemy_rect) and damage_cooldown == 0:
        player_health -= 10
        if player_health < 0:
            player_health = 0
        damage_cooldown = 60  # Cooldown period to prevent rapid health loss

    if damage_cooldown > 0:
        damage_cooldown -= 1

    # Display health
    health_text = font.render(f'Health: {player_health}', True, (0, 0, 0))
    screen.blit(health_text, (10, 10))

    # Check if health <= 0
    if player_health <= 0:
        # Display game over message
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        screen.blit(game_over_text, (screen_width // 2 - 50, screen_height // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Update the display to show changes
    pygame.display.flip()

# Quit pygame when the game loop is done
pygame.quit()