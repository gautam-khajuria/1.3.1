import turtle as trtl
import random as rng
import threading as thr

# 0.1.1

# Instantiate objects
obj = trtl.Turtle()
wn = trtl.Screen()

amount_of_coins = 5
coins = []

# Setup coins
coin_image = 'apple.gif'
wn.addshape(coin_image)


# Generates a list of coins with random locations
def generate_coins():
    for i in range(amount_of_coins):
        coin = trtl.Turtle(shape=coin_image)
        coin.penup()
        coin.speed(0)
        coin.setpos(350, rng.randint(-160, 160))
        coins.append(coin)


def bkgrnd_scroll():
    image_width = 742
    pen = trtl.Turtle()

    # backround image set up
    background_image = "background.gif"
    wn.addshape(background_image)
    wn.tracer(0)
    camera_dx = -3
    camera_x = 0

    wn.setup(height=320, width=image_width)

    while True:
        camera_x += camera_dx
        camera_x %= image_width

        pen.goto(camera_x - image_width, 0)
        pen.shape(background_image)
        pen.stamp()

        pen.goto(camera_x, 0)
        pen.shape(background_image)
        pen.stamp()

        wn.update()
        pen.clear()

    
# This block controls the main loop for the game, including the scrolling background.
if __name__ == '__main__':
    x = thr.Thread(target=bkgrnd_scroll, daemon=True)
    x.start()
