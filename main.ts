input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # # . . .
        . . # # .
        . . # . .
        . . . # .
        . . . # #
        `)
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 9; index++) {
        basic.pause(100)
        turtle.forward(1)
    }
})
