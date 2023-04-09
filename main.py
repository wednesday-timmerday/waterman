def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global hoi22, score
    if game.score() == hoi22 or game.score() > hoi22:
        hoi22 = hoi22 * 1.5
        game.add_score(game.score() * -1)
        score += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Enemy: game.LedSprite = None
player: game.LedSprite = None
hoi22 = 0
score = 1
hoi22 = 6
basic.show_string("Waterman")
Level = 1
player = game.create_sprite(2, 4)
Live = 3

def on_forever():
    global Enemy, Live
    Enemy = game.create_sprite(randint(0, 4), 0)
    for index in range(4):
        Enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
    Enemy.delete()
    Live += -1
basic.forever(on_forever)

def on_forever2():
    global Live
    if Enemy.is_touching(player):
        game.add_score(score)
        Enemy.delete()
        Live += 1
basic.forever(on_forever2)

def on_forever3():
    if Live == 0:
        player.delete()
        basic.pause(100)
        game.game_over()
basic.forever(on_forever3)

def on_forever4():
    if not (game.is_game_over()):
        music.play_melody("B A G A G F A C5 ", 120)
basic.forever(on_forever4)
