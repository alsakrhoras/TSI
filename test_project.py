# to be honest tests for pygame is't very presise or sometimes even effective but, ... #

import pygame
from tsi.project import (
    The_game,
    Player,
    Rocket,
    Alien,
    player,
    shoot_rocket,
    ply_collide,
    show_text,
    rok_collide,
    halt_screen,
    alien
)
pygame.init()


def test_play_game():
    game = The_game()
    p = Player("images/spaceship.bmp")
    r = Rocket("images/rocket1.bmp")
    game.play_game()
    # Check evints
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                assert p.ply_chng == -4 - p.score // 20
            if event.key == pygame.K_RIGHT:
                assert p.plx_chng == 4 + p.score // 20
            if event.key == pygame.K_UP:
                assert p.ply_chng == -4 - p.score // 20
            if event.key == pygame.K_DOWN:
                assert p.ply_chng == 4 + p.score // 20
            if event.key == pygame.K_SPACE:
                if r.rocket_state == "quite":
                    assert pygame.mixer.Sound("tracks/warexplosion.wav").play()
                    assert r.rocketx == p.playerx + 16
                    assert r.rockety == p.playery - 30
                    assert r.rocket_state == "shoot"
            if event.key == pygame.K_p:
                halt_screen(
                    "c",
                    "image/starry.bmp",
                    "PAUSED",
                    640,
                    320,
                    128,
                    "italic",
                    "Press C to Continue or Q to quit",
                    420,
                    580,
                    64,
                )
    if r.rocket_state == "shoot":
        assert shoot_rocket(r.rocketx, r.rockety)
        assert r.rockety == r.rockety - r.roky_chng + p.score // 20
        if r.rockety < 0:
            assert r.rockety == p.playery - 30
            assert r.rocket_state == "quite"
    if p.current_health == 2:
        halt_screen(
            "r",
            "images/starrysky.bmp",
            "GAME OVER",
            460,
            350,
            128,
            "gadugi",
            "Press R to RePlay or Q to Quit",
            450,
            640,
            64,
            scr=False,
        )
        assert p.score == 0
        assert p.current_health == 500
        assert p.playerx == 780
        assert p.playery == 768
        assert p.plx_chng == 0
        assert p.ply_chng == 0


def test_player():
    assert player(0, 0) == None
    assert player(100, 100) == None
    screen = pygame.display.set_mode((640, 480))
    p = Player("images/spaceship.bmp")
    x = 0
    y = 0
    p.playerimg = pygame.image.load("images/spaceship.bmp")
    screen.blit(p.playerimg, (x, y))
    assert screen.get_at((x, y)) == (0, 0, 0, 255)


def test_ply_collide():
    assert ply_collide(10, 15, 20, 25) == True
    assert ply_collide(0, 100, 0, 100) == None
def test_show_text():
    assert show_text(0, 0, "Hello World!", "red", 20, "Arial") == None
def test_rok_collide():
    assert rok_collide(0, 0, 0, 0) == True
    assert rok_collide(0, 0, 100, 0) == None
    assert ply_collide(20, 0, 40, 30) == True
    assert ply_collide(50, 0, -40, 30) == None
def test_alien():
    screen = pygame.display.set_mode((640, 480))
    a = [Alien("images/alien0.bmp")]
    x = 0
    y = 0
    i = 0
    a[i].alienimg = pygame.image.load("images/alien0.bmp")
    screen.blit(a[i].alienimg, (x, y))
    assert screen.get_at((x, y)) == (0, 0, 0, 255)

