# Import the pygame library so we can use it
import pygame

# Initialize pygame (this sets up everything we need to use it)
pygame.init()

# Set up the size of the window (width, height in pixels)
screen_width = 800  # Width of the screen in pixels
screen_height = 600  # Height of the screen in pixels
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("The best game ever")

# Choose a color for the screen background
# Colors in pygame use the RGB format (Red, Green, Blue)
background_color = (255, 255, 255)  # This is a white color

# This variable will keep our game loop running
running = True

# Main game loop
while running == True:
    # Check for events (things like key presses or closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the close button was clicked
            running = False  # This will end the game loop

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display to show changes
    pygame.display.flip()

# Quit pygame when the game loop is done
pygame.quit()