def on_button_pressed_a():
    basic.show_leds("""
        # # . . .
        . . # # .
        . . # . .
        . . . # .
        . . . # #
        """)
    music.ring_tone(392)
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)
