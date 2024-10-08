import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong')

# Clock
clock = pygame.time.Clock()

# Player paddles
player1 = pygame.Rect(50, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect((SCREEN_WIDTH - BALL_SIZE) // 2, (SCREEN_HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)

# Ball velocity
ball_vel_x = BALL_SPEED_X
ball_vel_y = BALL_SPEED_Y

# Scores
score1 = 0
score2 = 0

def draw_objects():
    """Draw the game objects on the screen."""
    screen.fill(BLACK)  # Fill the screen with black color
    pygame.draw.rect(screen, WHITE, player1)  # Draw player 1 paddle
    pygame.draw.rect(screen, WHITE, player2)  # Draw player 2 paddle
    pygame.draw.ellipse(screen, RED, ball)  # Draw the ball
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))  # Draw the center line
    display_score()  # Display the score
    pygame.display.flip()  # Update the display

def display_score():
    """Display the current score on the screen."""
    font = pygame.font.Font(None, 36)  # Set the font for the score
    score_text = font.render(f'{score1} - {score2}', True, WHITE)  # Render the score text
    text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 50))  # Center the score text
    screen.blit(score_text, text_rect)  # Draw the score text on the screen

def move_paddles():
    """Move the paddles based on user input."""
    keys = pygame.key.get_pressed()  # Get the current state of all keyboard keys
    # Move player 1 paddle
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.y += PADDLE_SPEED
    # Move player 2 paddle
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
        player2.y += PADDLE_SPEED

def move_ball():
    """Move the ball and handle collisions."""
    global ball_vel_x, ball_vel_y, score1, score2
    ball.x += ball_vel_x  # Move the ball horizontally
    ball.y += ball_vel_y  # Move the ball vertically

    # Bounce the ball off the top or bottom of the screen
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_vel_y = -ball_vel_y

    # Bounce the ball off the paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_vel_x = -ball_vel_x

    # Handle scoring
    if ball.left <= 0:  # Player 2 scores
        score2 += 1
        reset_ball()
    if ball.right >= SCREEN_WIDTH:  # Player 1 scores
        score1 += 1
        reset_ball()

def reset_ball():
    """Reset the ball to the center of the screen and randomize its direction."""
    global ball_vel_x, ball_vel_y
    ball.x = (SCREEN_WIDTH - BALL_SIZE) // 2
    ball.y = (SCREEN_HEIGHT - BALL_SIZE) // 2
    ball_vel_x = BALL_SPEED_X * random.choice((1, -1))  # Randomize the horizontal direction
    ball_vel_y = BALL_SPEED_Y * random.choice((1, -1))  # Randomize the vertical direction

def main():
    """Main game loop."""
    running = True
    while running:
        for event in pygame.event.get():  # Handle events
            if event.type == pygame.QUIT:  # Exit the game if the quit event is triggered
                running = False

        move_paddles()  # Move the paddles
        move_ball()  # Move the ball
        draw_objects()  # Draw the game objects
        clock.tick(60)  # Cap the frame rate to 60 FPS

    pygame.quit()  # Quit Pygame

if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly