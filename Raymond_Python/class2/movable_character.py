# Import the pygame library so we can use it
import pygame

# Initialize pygame (this sets up everything we need to use it)
pygame.init()

# Set up the size of the window (width, height in pixels)
screen_width = 800  # Width of the screen in pixels
screen_height = 600  # Height of the screen in pixels
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Character Movement with Pygame")

# Choose a color for the screen background
background_color = (135, 206, 235)  # Light blue

# Choose a color for the character (a simple rectangle)
character_color = (255, 0, 0)  # Red

# Set the size of the character
character_width = 50  # Width of the rectangle
character_height = 50  # Height of the rectangle

# Set the starting position of the character
character_x = screen_width // 2  # Start in the middle of the screen (horizontally)
character_y = screen_height // 2  # Start in the middle of the screen (vertically)

# Set the speed of the character (how many pixels it moves per key press)
character_speed = 1

# This variable will keep our game loop running
running = True

# Main game loop
while running == True:
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
    if keys[pygame.K_UP]:  # Move up
        character_y -= character_speed
    if keys[pygame.K_DOWN]:  # Move down
        character_y += character_speed

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the character (a red rectangle)
    pygame.draw.rect(screen, character_color, (character_x, character_y, character_width, character_height))

    # Update the display to show changes
    pygame.display.flip()

# Quit pygame when the game loop is done
pygame.quit()