import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_ship = Player(x,y)

    end_loop = False

    while (end_loop == False):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            game_clock.tick(60) 
            dt = game_clock.tick(60) / 1000
        screen.fill("black")
        player_ship.draw(screen, "white", player_ship.triangle(), LINE_WIDTH)
        player_ship.update(dt)
        pygame.display.flip()



if __name__ == "__main__":
    main()
