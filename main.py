import pygame

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

grid_size = int(min(SCREEN_WIDTH, SCREEN_HEIGHT)*0.8)
horizontal_margin = (SCREEN_WIDTH-grid_size)//2
vertical_margin = (SCREEN_HEIGHT-grid_size)//2
def pygame_loop ():
    global done
    global mouse_is_down

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_is_down = False

        if mouse_is_down:
            x, y = pygame.mouse.get_pos()
            #play_at(x,y)



        draw_background()


        clock.tick(60)

        pygame.display.flip()



def draw_background ():
    screen.fill(BEIGE)

    #screen.blit(text, textRect)
    #for i in range(10):
    #    screen.blit(texts[i], textRects[i])
    #for row in cells:
    #    for cell in row:
    #        pygame.draw.rect(screen, cell.color, (cell.x - cell.size[0]/2, cell.y - cell.size[1]/2, cell.size[0], cell.size[1]))
    #pygame.draw.rect(screen, BLUE, (0,0, 500,500))
    pygame.draw.line(screen, BLACK, (horizontal_margin, vertical_margin), (SCREEN_WIDTH-horizontal_margin, vertical_margin))
    for i, j in zip(range(vertical_margin, grid_size+1+vertical_margin, grid_size//3),range(horizontal_margin, grid_size+1+horizontal_margin, grid_size//3)):
        pygame.draw.line(screen, BLACK, (horizontal_margin, i), (SCREEN_WIDTH - horizontal_margin, i))
        pygame.draw.line(screen, BLACK, (j, vertical_margin), (j, SCREEN_HEIGHT - vertical_margin))
    for i in range(vertical_margin, grid_size+vertical_margin-10,grid_size//3):
        for j in range(horizontal_margin, grid_size+horizontal_margin-10,grid_size//3):
            drawtictactoe(j, i)

def drawtictactoe (x, y):
    small_grid_size = grid_size//3
    pygame.draw.line(screen, BLACK, (x + small_grid_size//7, y + small_grid_size//3), (x + small_grid_size*6//7, y + small_grid_size//3))
    pygame.draw.line(screen, BLACK, (x + small_grid_size//7, y + small_grid_size*2//3), (x + small_grid_size*6//7, y + small_grid_size*2//3))
    pygame.draw.line(screen, BLACK, (x + small_grid_size//3, y + small_grid_size//7), (x + small_grid_size//3, y + small_grid_size*6//7))
    pygame.draw.line(screen, BLACK, (x + small_grid_size*2//3, y + small_grid_size//7), (x + small_grid_size*2//3, y + small_grid_size*6//7))

def get_action (game):
    pass

def draw_game (game):
    pass