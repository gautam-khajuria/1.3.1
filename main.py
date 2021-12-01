import turtle as trtl
import random as rng

# 0.1.1

# Instantiate objects
pen = trtl.Turtle()
obj = trtl.Turtle()
wn = trtl.Screen()

amount_of_coins = 5
coins = []

# Set Speed Fastest
obj.speed(0)

# This creates an object as a hot air balloon
pear_image = 'pear.gif'
wn.addshape(pear_image)
obj.shape(pear_image)


# Setup coins
coin_image = 'coin.gif'
wn.addshape(coin_image)

# Generates a list of coins with random locations
def generate_coins():
  for i in range(amount_of_coins):
    coin = trtl.Turtle(shape=coin_image)
    coin.penup()
    coins.append(coin)








  


# This block controls the main loop for the game, including the scrolling background.
if __name__ == '__main__':
  image_width = 742

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
      
    pen.goto(camera_x-image_width, 0)
    pen.shape(background_image)
    pen.stamp()
      
    pen.goto(camera_x, 0)
    pen.shape(background_image)
    pen.stamp()

      
    # Work here #
    generate_coins()


    for coin in coins:
      coin.backward(1)

    def movement_up():
      obj.penup()
      obj.right(90)
      obj.forward(10)
      obj.pendown()
      obj.left(90)

    def movement_down():
      obj.penup()
      obj.left(90)
      obj.forward(10)
      obj.pendown()
      obj.right(90)

      # --- #


    wn.update()

    pen.clear()

wn.onkeypress(movement_up, "W")
wn.onkeypress(movement_down, "S")
wn.listen()