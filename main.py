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

done = False
mouse_is_down = False
clicked_pos = None

grid_size = int(min(SCREEN_WIDTH, SCREEN_HEIGHT)*0.8)
horizontal_margin = (SCREEN_WIDTH-grid_size)//2
vertical_margin = (SCREEN_HEIGHT-grid_size)//2
def pygame_loop ():
    global done
    global mouse_is_down
    global clicked_pos

    draw_background()

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

    # screen.blit(text, textRect)
    # for i in range(10):
    #    screen.blit(texts[i], textRects[i])
    # for row in cells:
    #    for cell in row:
    #        pygame.draw.rect(screen, cell.color, (cell.x - cell.size[0]/2, cell.y - cell.size[1]/2, cell.size[0], cell.size[1]))
    # pygame.draw.rect(screen, BLUE, (0,0, 500,500))
    pygame.draw.line(screen, BLACK, (horizontal_margin, vertical_margin),
                     (SCREEN_WIDTH - horizontal_margin, vertical_margin))
    for i, j in zip(range(vertical_margin, grid_size + 1 + vertical_margin, grid_size // 3),
                    range(horizontal_margin, grid_size + 1 + horizontal_margin, grid_size // 3)):
        pygame.draw.line(screen, BLACK, (horizontal_margin, i), (SCREEN_WIDTH - horizontal_margin, i))
        pygame.draw.line(screen, BLACK, (j, vertical_margin), (j, SCREEN_HEIGHT - vertical_margin))
    for i in range(vertical_margin, grid_size + vertical_margin - 10, grid_size // 3):
        for j in range(horizontal_margin, grid_size + horizontal_margin - 10, grid_size // 3):
            drawtictactoe(j, i)

def draw_game (game):
    draw_background()

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


if __name__=="__main__":
    pygame_loop()