import turtle as trtl
import random as rng
import time

# 0.1.1

# Instantiate objects
pen = trtl.Turtle()
pen.hideturtle()
obj = trtl.Turtle()
obj.penup()
wn = trtl.Screen()

amount_of_coins = 1
coins = []

# Set Speed Fastest
obj.speed(0)
pen.speed(0)

# This creates an object as a hot air balloon
pear_image = 'pear.gif'
apple_image = 'apple.gif'
wn.addshape(pear_image)
wn.addshape(apple_image)
obj.shape(apple_image)


# Setup coins
coin_image = 'pear.gif'
wn.addshape(coin_image)

# Generates a list of coins with random locations
def generate_coins():
  for i in range(amount_of_coins):
    coin = trtl.Turtle(shape=coin_image)
    coin.penup()
    rand_pos(coin)
    coins.append(coin)
    wn.update()

# Generate random position for a coin
def rand_pos(coin):
  x, y = rng.randint(300, 350), rng.randint(-140, 140)
  
  coin.setpos(x, 0)

# Starts a coins movement. This method also resets the coin.
def start_coin(coin):

  while True:
    distance_x = abs(coin.xcor() - obj.xcor())
    distance_y = abs(coin.ycor() - obj.ycor())

    coin.backward(1)
    if distance_x <= 20 and distance_y <= 20:
      coin.hideturtle()
      print("coll")
      # Increment the score
      break # collision
    if coin.xcor() <= -200:
      coin.hideturtle()
      print("end screen")
      break
  
  # Collision has occured, or screen has been reached
  coin.showturtle()
  rand_pos(coin)
  start_coin(coin)



def movement_up():
  obj.penup()
  obj.setpos(obj.xcor(), obj.ycor() +200)

def movement_down():
  obj.penup()
  obj.setpos(obj.xcor(), obj.ycor() - 200)

def press_Up():
    global seconds
    seconds = time.time()
    wn.onkeypress(movement_up, "Up")

def release_Up():
    if time.time() - seconds >= 0.1:
        wn.onkeyrelease(movement_up, 'Up')

def press_down():
  wn.onkeypress(movement_up, "Down")

def release_down():
  if time.time() - seconds >= 0.1:
    wn.onkeypress(movement_down, 'Down')

wn.onkeypress(press_Up, 'Up')
wn.onkeyrelease(release_Up, 'Up')
wn.onkeypress(press_Up, 'Down')
wn.onkeyrelease(release_Up, 'Down')

wn.onkeypress(movement_up, 'w')
wn.onkeypress(movement_down, 's')

wn.listen()




  # --- #

generate_coins()

for coin in coins:
  pass



# This block controls the main loop for the game, including the scrolling background.
if __name__ == '__main__':
  image_width = 400

  # backround image set up
  background_image = "background.gif"
  wn.addshape(background_image)
  wn.tracer(0)
  camera_dx = -3
  camera_x = 0

  wn.setup(height=320, width=image_width)


  trtl.mainloop()
''''
  while True:
    camera_x += camera_dx
    camera_x %= image_width
      
    pen.goto(camera_x-image_width, 0)
    pen.shape(background_image)
    pen.stamp()
      
    pen.goto(camera_x, 0)
    pen.shape(background_image)
    pen.stamp()

      


    wn.update()

    pen.clear()
'''