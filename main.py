import pygame
import time

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

pygame.init()

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic-tac-toe ++")

clock = pygame.time.Clock()

BLUE = (61, 178, 255)
BEIGE = (255, 237, 218)
YELLOW = (255, 184, 48)
RED = (255, 36, 66)
BLACK = (0, 0, 0)
GREEN_OF_WIN = (20,99,86)
done = False
mouse_is_down = False
clicked_pos = None

grid_size = int(min(SCREEN_WIDTH, SCREEN_HEIGHT)*0.8)
horizontal_margin = (SCREEN_WIDTH-grid_size)//2
vertical_margin = (SCREEN_HEIGHT-grid_size)//2

font = pygame.font.Font('freesansbold.ttf', vertical_margin//2)
text = font.render('Waiting for player', True, BLACK)
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH//2, vertical_margin//2)

def pygame_loop ():
    global done
    global mouse_is_down
    global clicked_pos

    draw_background()
    screen.blit(text, textRect)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_down = True
                clicked_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_is_down = False

        clock.tick(60)

        pygame.display.flip()

def drawtictactoe (x, y):
    small_grid_size = grid_size//3
    pygame.draw.line(screen, BLACK, (x + small_grid_size//7, y + small_grid_size//3), (x + small_grid_size*6//7, y + small_grid_size//3))
    pygame.draw.line(screen, BLACK, (x + small_grid_size//7, y + small_grid_size*2//3), (x + small_grid_size*6//7, y + small_grid_size*2//3))
    pygame.draw.line(screen, BLACK, (x + small_grid_size//3, y + small_grid_size//7), (x + small_grid_size//3, y + small_grid_size*6//7))
    pygame.draw.line(screen, BLACK, (x + small_grid_size*2//3, y + small_grid_size//7), (x + small_grid_size*2//3, y + small_grid_size*6//7))

def get_action ():
    global done
    global mouse_is_down
    global clicked_pos

    clicked_pos = None

    while True:
        time.sleep(0.25)
        if clicked_pos is not None:
            x, y = clicked_pos
            if x > horizontal_margin and x < grid_size+horizontal_margin and y > vertical_margin and y < vertical_margin + grid_size:
                relative_x = x - horizontal_margin
                relative_y = y - vertical_margin

                return f"{(relative_x*9//grid_size)} {(relative_y*9//grid_size)}"
            clicked_pos = None

def draw_background():
    screen.fill(BEIGE)

    pygame.draw.line(screen, BLACK, (horizontal_margin, vertical_margin),
                     (SCREEN_WIDTH - horizontal_margin, vertical_margin))
    for i, j in zip(range(vertical_margin, grid_size + 1 + vertical_margin, grid_size // 3),
                    range(horizontal_margin, grid_size + 1 + horizontal_margin, grid_size // 3)):
        pygame.draw.line(screen, BLACK, (horizontal_margin, i), (SCREEN_WIDTH - horizontal_margin, i))
        pygame.draw.line(screen, BLACK, (j, vertical_margin), (j, SCREEN_HEIGHT - vertical_margin))
    for i in range(vertical_margin, grid_size + vertical_margin - 10, grid_size // 3):
        for j in range(horizontal_margin, grid_size + horizontal_margin - 10, grid_size // 3):
            drawtictactoe(j, i)

def draw_game (game, player_number):
    global text
    draw_background()

    if game.turn == player_number:
        text = font.render("It's your turn", True, BLACK)
    else:
        text = font.render("It's the opponent's turn", True, BLACK)
    if game.winner is not None:
        if game.winner == -1:
            text = font.render("IT'S A TIE !", True, BLACK)
        elif game.winner == player_number:
            text = font.render("YOU WON THE GAME ! :)", True, GREEN_OF_WIN)
        else:
            text = font.render("YOU LOST THE GAME :(", True, RED)
    screen.blit(text, textRect)
    for i in range(len(game.grid)):
        for j in range(len(game.grid[0])):
            element = game.grid[i][j]
            x = int(horizontal_margin + grid_size//18 + (j*grid_size)//9)
            y = int(vertical_margin + grid_size//18 + (i*grid_size)//9)

            if element == '0':
                # Draw circle
                pygame.draw.circle(screen, BLUE, (x,y), grid_size/25)
                pygame.draw.circle(screen, BEIGE, (x, y), grid_size/35)
            if element == '1':
                # Draw cross
                pygame.draw.line(screen, RED, (x-grid_size//30, y-grid_size//30), (x+grid_size//30, y+grid_size//30), 10)
                pygame.draw.line(screen, RED, (x - grid_size // 30, y + grid_size // 30), (x + grid_size // 30, y - grid_size // 30), 10)

    for i in range(3):
        for j in range(3):
            winner = game.get_winner(game.get_subgrid((j, i)))
            if winner is not None:
                    pygame.draw.rect(screen, BEIGE, pygame.Rect(2+horizontal_margin+j*grid_size//3,2+vertical_margin+i*grid_size//3, -4+grid_size//3,-4+grid_size//3))
                    pygame.display.flip()
                    if winner == 0:
                        pygame.draw.circle(screen, BLUE, (grid_size//6+horizontal_margin+j*grid_size//3, grid_size//6+vertical_margin+i*grid_size//3), -4+grid_size//8)
                        pygame.draw.circle(screen, BEIGE, (grid_size//6+horizontal_margin+j*grid_size//3, grid_size//6+vertical_margin+i*grid_size//3), -4+grid_size /10)
                    if winner == 1:
                        x = int(horizontal_margin + grid_size // 6 + (j * grid_size) // 3)
                        y = int(vertical_margin + grid_size // 6 + (i * grid_size) // 3)
                        pygame.draw.line(screen, RED, (x-grid_size//10, y-grid_size//10), (x+grid_size//10, y+grid_size//10), 30)
                        pygame.draw.line(screen, RED, (x - grid_size // 10, y + grid_size // 10), (x + grid_size // 10, y - grid_size // 10), 30)
                    if winner == -1: #ToDo
                        x = int(horizontal_margin + grid_size // 6 + (j * grid_size) // 3)
                        y = int(vertical_margin + grid_size // 6 + (i * grid_size) // 3)
                        pygame.draw.line(screen, GREEN_OF_WIN, (x - grid_size // 10, y - grid_size // 10),
                                         (x + grid_size // 10, y - grid_size // 10), 30)
                        pygame.draw.line(screen, GREEN_OF_WIN, (x - grid_size // 10, y + grid_size // 10),
                                         (x + grid_size // 10, y + grid_size // 10), 30)

if __name__=="__main__":
    pygame_loop()
