input.onButtonPressed(Button.A, function () {
    player.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    if (game.score() == hoi22 || game.score() > hoi22) {
        hoi22 = hoi22 * 1.5
        game.addScore(game.score() * -1)
        score += 1
    }
})
input.onButtonPressed(Button.B, function () {
    player.move(1)
})
let Enemy: game.LedSprite = null
let player: game.LedSprite = null
let hoi22 = 0
let score = 1
hoi22 = 6
basic.showString("Waterman")
let Level = 1
player = game.createSprite(2, 4)
let Live = 3
basic.forever(function () {
    Enemy = game.createSprite(randint(0, 4), 0)
    for (let index = 0; index < 4; index++) {
        Enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
    }
    Enemy.delete()
    Live += -1
})
basic.forever(function () {
    if (Enemy.isTouching(player)) {
        game.addScore(score)
        Enemy.delete()
        Live += 1
    }
})
basic.forever(function () {
    if (Live == 0) {
        player.delete()
        basic.pause(100)
        game.gameOver()
    }
})
basic.forever(function () {
    if (!(game.isGameOver())) {
        music.playMelody("E B C5 A B G A F ", 120)
    }
})
