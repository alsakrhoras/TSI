# a space invader game like the arcade game

import random
import math
import sys
import pygame


pygame.init()
# make a variable (time) from the pygame clock
time = pygame.time.Clock()

# set the screen dimentions
screen = pygame.display.set_mode((1600, 900))

# the background of the game
background = pygame.image.load("images/starry.bmp")

# the sound track ### It does not work in Linux ###
pygame.mixer.music.load("tracks/background.mp3")
pygame.mixer.music.set_volume(0.7)  ### IT IS VERY LAOUD ###
pygame.mixer.music.play(-1)

# the title of the game
pygame.display.set_caption("The Space Invader")
## the game's icon
pygame.display.set_icon(pygame.image.load("images/gameicon.bmp"))


# the player class and all its properities
class Player:
    def __init__(self, image) -> None:
        self.playerimg = pygame.image.load(image)
        self.playerx = 780
        self.playery = 768
        self.plx_chng = 0
        self.ply_chng = 0
        self.current_health = 500
        self.max_health = 500
        self.score = 0


# the alien (opponents) class and their properties
class Alien:
    def __init__(self, image) -> None:
        self.alienimg = pygame.image.load(image)
        self.alienx = random.randint(0, 1536)
        self.alieny = random.randint(10, 250)
        self.alx_chng = random.randint(1, 5)
        self.aly_chng = random.randint(8, 24)

    def alien_new_move(self) -> None:
        """
        make the alien reapper after hit
        args: none
        returns: none
        """
        self.alienx = random.randint(0, 1536)
        self.alieny = random.randint(10, 250)
        self.alx_chng = random.randint(1, 5) + (p.score // 10)
        self.aly_chng = random.randint(6, 12) + (p.score // 10)


# the rocket (the opject that will be shot at the alien from the ship "player") and its proprties
class Rocket:
    def __init__(self, image) -> None:
        self.rocketimg = pygame.image.load(image)
        self.rocketx = p.playerx - 16
        self.rockety = p.playery - 32
        self.rokx_chng = 0
        self.roky_chng = 16
        self.rocket_state = "quite"


# the game
class TheGame:
    def __init__(self) -> None:
        pass

    # the method that mange the game
    def play_game(self):
        # displaying the background on screen
        screen.blit(background, (0, 0))

        # to get out of the loop and close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # setting the keyboard keys that will control the game
            if event.type == pygame.KEYDOWN:
                # to close
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                # to movement
                if event.key == pygame.K_LEFT:
                    p.plx_chng = -4 - p.score // 20
                if event.key == pygame.K_RIGHT:
                    p.plx_chng = 4 + p.score // 20
                if event.key == pygame.K_UP:
                    p.ply_chng = -4 - p.score // 20
                if event.key == pygame.K_DOWN:
                    p.ply_chng = 4 + p.score // 20

                # to pause
                if event.key == pygame.K_p:
                    halt_screen(
                        "c",
                        "images/starry.bmp",
                        "PAUSED",
                        640,
                        420,
                        128,
                        "italic",
                        "yellow",
                        "Press C to Continue or Q to quit",
                        430,
                        64,
                    )
                # to shoot
                if event.key == pygame.K_SPACE:
                    if r.rocket_state == "quite":
                        pygame.mixer.Sound("tracks/warexplosion.wav").play()
                        r.rocketx = p.playerx + 16
                        r.rockety = p.playery - 30
                        r.rocket_state = "shoot"

            # to set the player x, y change to zero if the keys stoped beeing pressed
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    p.plx_chng = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    p.ply_chng = 0

        # to limit the aliens motion to ourscreen so they do not move beyound it
        for i, _ in enumerate(a):
            a[i].alienx += a[i].alx_chng
            if a[i].alienx <= 0:
                a[i].alx_chng += 1
                a[i].alieny += a[i].aly_chng
            elif a[i].alienx >= 1536:
                a[i].alx_chng -= 1
                a[i].alieny += a[i].aly_chng
            elif a[i].alieny > 900:
                a[i].alien_new_move()
                # deducting from the player's health if the alien passed him
                p.current_health -= 25

            # maneging the situation in case of the rocket hit the target
            if (
                r.rocket_state == "shoot"
            ):  # so the function will not be ablied if the player did not shoot
                if rok_collide(a[i].alienx, r.rocketx, a[i].alieny, r.rockety):
                    pygame.mixer.Sound("tracks/pixelexplosion.wav").play()
                    # returning the rocket to its posision and state
                    r.rockety = p.playery - 30
                    r.rocket_state = "quite"
                    # reapearing the alien
                    a[i].alien_new_move()
                    # rewarding the player
                    p.score += 1
                    p.current_health += 5

            # maniging the situation if the player and the alien collided
            if ply_collide(a[i].alienx, p.playerx, a[i].alieny, p.playery):
                # returning the player to its original position and "punishing him"
                p.playerx = 780
                p.playery = 768
                p.current_health -= 50
                pygame.mixer.Sound("tracks/denseimpact.wav").play()  # sound effict
                # reapearing the alien
                a[i].alien_new_move()

            # make the alien appear on screen by blint
            alien(a[i].alienx, a[i].alieny, i)

        # manging win
        # and returning the game to its original state if the player continue
        if p.score > 149:
            pygame.display.update()
            halt_screen(
                "r",
                "images/milkyway.bmp",
                "WILL DONE YOU WON",
                300,
                460,
                96,
                "roman",
                "green",
                "Press R to RePlay or Q to Quit",
                440,
                64,
                scr=True,
            )
            start_new()

        # manging loss (game over)
        elif p.current_health < 0:
            pygame.display.update()
            halt_screen(
                "r",
                "images/starrysky.bmp",
                "GAME OVER",
                460,
                420,
                128,
                "gadugi",
                "red",
                "Press R to RePlay or Q to Quit",
                450,
                64,
                scr=True,
            )
            start_new()

        # displaying and handling the rocket in case it has been shot
        if r.rocket_state == "shoot":
            # displaying by blint
            shoot_rocket(r.rocketx, r.rockety)
            r.rockety -= r.roky_chng + p.score // 20
            # returning the rocket to its original possition and state if it goes off screen
            if r.rockety < 0:
                r.rockety = p.playery - 30
                r.rocket_state = "quite"

        # making the player move by adding (and subbstracting by negative adding) its x, y change
        p.playerx += p.plx_chng
        p.playery += p.ply_chng

        # so the player will not go of screen
        if p.playerx <= -64:
            p.playerx = 1600
        elif p.playerx >= 1600:
            p.playerx = -64

        if p.playery <= -64:
            p.playery = 900
        elif p.playery >= 900:
            p.playery = -64

        # displaying the player's health
        health_bar()

        # displaying the player
        player(p.playerx, p.playery)

        # displaying the player score
        show_text(1420, 10, f"SCORE: {p.score}", (255, 215, 0), 32, "Carlito")

        # updating the game (making changes that occur in the loop appear on the screen)
        pygame.display.update()


# making a list of the aliens to handle their movment and collision more affictevely
aliens = [
    Alien("images/alien0.bmp"),
    Alien("images/alien1.bmp"),
    Alien("images/alien2.bmp"),
    Alien("images/alien3.bmp"),
    Alien("images/alien4.bmp"),
    Alien("images/alien5.bmp"),
    Alien("images/alien6.bmp"),
    Alien("images/alien7.bmp"),
    Alien("images/alien8.bmp"),
    Alien("images/alien9.bmp"),
    Alien("images/alien10.bmp"),
    Alien("images/alien11.bmp"),
]


a = aliens
p = Player("images/spaceship.bmp")
r = Rocket("images/rocket1.bmp")
g = TheGame()


def main():
    # show the game name
    halt_screen(
        "s",
        "images/space.bmp",
        "THE SPACE INVADER",
        340,
        420,
        128,
        "italik",
        "cyan",
        "Press S to Start, P to Pause or Q to quit, move by ARWS and shoot by SPACE",
        250,
        40,
    )
    while True:
        g.play_game()

        time.tick(60)


def start_new():
    p.score = 0
    p.current_health = 500
    p.playerx = 780
    p.playery = 768
    p.plx_chng = 0
    p.ply_chng = 0
    for _, an_alien in enumerate(a):
        an_alien.alien_new_move()


def player(x, y):
    """
    displays the player on the screen
    args (x, y) ints: the position of the player on the screen
    returns: none
    """
    screen.blit(p.playerimg, (x, y))


def alien(x, y, i):
    """
    displays the alien(s)"the opponents" on the screen
    args (x, y) ints: the position of the alien(s) on the screen
    i (int) : index into the "aliens" list
    returns: none
    """
    screen.blit(a[i].alienimg, (x, y))


def shoot_rocket(x, y):
    """
    displays the rocket on the screen (when it is called)
    args (x, y) ints: the position of the rocket on the screen (when it is called)
    returns: none
    """
    screen.blit(r.rocketimg, (x, y))


def health_bar() -> None:
    pygame.draw.rect(screen, (255, 0, 0), (30, 20, p.max_health, 15))
    pygame.draw.rect(screen, (0, 255, 0), (30, 20, p.current_health, 15))


def rok_collide(ax, rx, ay, ry) -> bool | None:
    """
    calculates the distance between the alien and the rocket
    args (ax, rx, ay, ry) ints: the possitions of the alien and the rocket
    returns: bool(True) if the distance less than 50, else returns None
    """
    return math.sqrt(math.pow(ax - rx, 2) + math.pow(ay - ry, 2)) < 50


def ply_collide(ax, px, ay, py) -> bool | None:
    """
    calculates the distance between the palyer and the alien
    args (ax, rx, ay, ry) ints: the possitions of the player and the alien
    returns: bool(True) if the distance less than 50, else returns None
    """
    return math.sqrt(math.pow(ax - px, 2) + math.pow(ay - py, 2)) < 50


def show_text(x, y, txt, color, size, ttype) -> None:
    """
    show text on screen
    args: (x, y) screen positions (int)
    txt (str): prints on the screen what have been typed
    color: (int) type color of text in RGB or (str) type name of the color
    size (int): the size of the text
    returns: none
    """
    font = pygame.font.SysFont(ttype, size)
    strr = font.render(txt, True, color)
    screen.blit(strr, (x, y))


def halt_screen(
    knam, image, btxt, bx, by, bsz, bfnt, bc, stxt, sx, ssz, scr=False
) -> None:
    """
    halts the screen in the begining, pausing and game over
    args: Knam (str): identefy the key that will be pressed to get out of the loop
        image: the image that will be displayed
        btxt (str): the string that will be displaed in a big font
        bx, by (int): the x, y coarrdints of the big text
        bsz (int): its size
        bfont (str): its font
        stxt (str): the string that will be displayed in small font
        sx, sy (int): the x, y coarrdints of the small text
        ssz (int): its size
        scr (bool) or any or none: if bool is true the player score will be displayed other wise it will not
    returns: None
    """
    thing = True
    while thing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == getattr(pygame, f"K_{knam}"):
                    thing = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            screen.blit(pygame.image.load(image), (0, 0))
            if scr is True:
                show_text(740, 260, f"SCORE: {p.score}", "gold", 48, "Carlito")
            show_text(
                470,
                50,
                "Thank you Professor David Malan and all CS50 Team",
                "white",
                32,
                "Carlito",
            )

            show_text(bx, by, btxt, bc, bsz, bfnt)
            show_text(
                sx,
                800,
                stxt,
                "yellow",
                ssz,
                "arial",
            )

            pygame.display.update()
            time.tick(15)


if __name__ == "__main__":
    main()
