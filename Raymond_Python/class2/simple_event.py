import pygame

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Simple Game Simulation")

# Initialize the clock to control the frame rate
clock = pygame.time.Clock()

# Initialize a counter to simulate ticks in the game loop
counter = 0

# Game loop
running = True
while running == True:

    # Don't worry about this, we just add it to allow the user to close the program!
    # Check for any quit event (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # End of the "Don't worry about this" part

    # Increase the counter on each loop iteration
    counter += 1

    # Check if the counter is a multiple of 10 (every 10th frame)
    if counter % 10 == 0:
        print("This could be an event that occurs every 10 frames. Maybe an enemy shoots at the player.")

    # Simulate a game over after 50 iterations
    if counter >= 50:
        print("Game Over!")
        running = False

    # Fill the screen with a color (for example, maroon)
    screen.fill((128, 0, 0))

    # Display the current counter on the screen for the player to see
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Counter: {counter}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    # Update the screen to show the latest changes
    pygame.display.flip()

    # Don't worry about this too much
    # Control the frame rate to simulate realistic game timing
    clock.tick(10)  # 10 frames per second, ensures enough time (100 ms in this case) has passed since the last frame was rendered
    # End of the "Don't worry about this" part

# Quit Pygame
pygame.quit()