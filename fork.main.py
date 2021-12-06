import turtle as trtl
import random as rng
import time

# 0.2.0

# Instantiate objects
pen = trtl.Turtle()
pen.hideturtle()
obj = trtl.Turtle()
obj.penup()
wn = trtl.Screen()

font_setup = ("Arial", 20, "bold")

# Score turtle
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.speed(0)
score_writer.penup()

# Get player name for scoring
player_name = None
while player_name == "" or player_name == None: # Input validation
  player_name = trtl.textinput("Enter your name", "Hi player! What is your name?")
  print (player_name)

# Score/timer config
score = 0
timer_up = False

# Go to proper location
score_writer.goto(-200, 130)
score_writer.write("Score starts at 0", font=font_setup)  

# Coins control
amount_of_coins = 1
coins = []

# Following lists control the shape, size, and colors of the coins. This makes the game more interesting, and makes it harder to discern whether or not it is a coin or obstacle
coin_colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'red']
coin_shapes = ['turtle', 'square', 'circle', 'arrow', 'classic', 'triangle']
coin_sizes = [1]

# Set Speed Fastest
obj.speed(0)
pen.speed(0)

# This creates an object as a APPLE balloon
apple_image = 'apple.gif'
wn.addshape(apple_image)
obj.shape(apple_image)

# Setup coins
coin_image = 'pear.gif'
wn.addshape(coin_image)


# Updates the score variable, checking to make sure the timer is not complete. This also prints the score to the screen
def update_score():
    global score, score_writer, timer_up

    score += 1  # increment score
    score_writer.clear()
    if timer_up:
        return
    score_writer.write(player_name + ": " + str(score), font=font_setup)

# Same thing as update_score(), except it decrements the variable. This is used in the case that an obstacle is hit
def decrement_score():
  global score, score_writer, timer_up

  score -= 1  # increment score
  score_writer.clear()
  if timer_up:
      return
  score_writer.write(player_name + ": " + str(score), font=font_setup)


# Generates a list of coins with random locations
def generate_coins():
    for i in range(amount_of_coins):
        coin = trtl.Turtle()
        coin.penup()
        rand_pos(coin)
        coins.append(coin)
        wn.update()


# Generate random position for a coin
def rand_pos(coin):
    x, y = rng.randint(300, 350), rng.randint(-140, 140)

    coin.setpos(x, y)

# Returns a random index for the given array
def randbound(arr):
  return rng.randint(0, len(arr)-1)

# Starts a coins movement. This method also resets the coin.
def start_coin(coin):
    time.sleep(0.0001)
    coin.showturtle()

    # Draw the coin with a random shape, size, and color 
    # Remove those chosen from the array as well
    shape = coin_shapes.pop(randbound(coin_shapes))
    size = coin_sizes.pop(randbound(coin_sizes))
    color = coin_colors.pop(randbound(coin_colors))

    is_obstacle = False

    if color == 'red' or shape == 'triangle':
      # Obstacle!
      is_obstacle = True


    # Assign coin to that 
    coin.shape(shape)
    coin.turtlesize(float(size))
    coin.color(color)

    print(color, shape)

    while True:
        # Calculate distance from coin to player
        distance_x = abs(coin.xcor() - obj.xcor())
        distance_y = abs(coin.ycor() - obj.ycor())

        coin.backward(1)
        # Check for collision or screen end
        if distance_x <= 20 and distance_y <= 60:
            coin.hideturtle()
            print("coll")
            # Update the score if this is a coin, or reduce it if this is an obstacle
            update_score() if not is_obstacle else decrement_score()
            break  # collision
        if coin.xcor() <= -200:
            coin.hideturtle()
            print("end screen")
            break

    # Collision has occured, or screen has been reached
    rand_pos(coin)

    # Return the chosen back to the array
    coin_shapes.append(shape)
    coin_colors.append(color)
    coin_sizes.append(size)

    # Restart its movement
    start_coin(coin)


# Moves the apple object up by 5 pixels
def movement_up():
    global obj
    obj.penup()
    obj.goto(obj.xcor(), obj.ycor() + 5)

# Moves the apple object down by 5 pixels
def movement_down():
    global obj
    obj.penup()
    obj.setpos(obj.xcor(), obj.ycor() - 5)

'''
def press_up():
    global seconds
    seconds = time.time()
    wn.onkeypress(movement_up, "Up")


def release_up():
    if time.time() - seconds >= 0.1:
        wn.onkeyrelease(movement_up, 'Up')


def press_down():
    wn.onkeypress(movement_up, "Down")


def release_down():
    if time.time() - seconds >= 0.1:
        wn.onkeypress(movement_down, 'Down')

'''

# Creates movement handlers for the up and down keys (w, s)
def movement():
    wn.onkeypress(movement_up, 'w')
    wn.onkeypress(movement_down, 's')


# --- #

# Starts and listens for key presses
movement()
wn.listen()

# Generates, and starts all coins
generate_coins()

for coin in coins:
  start_coin(coin)

# Controls main loop for game, including background, dimensions, etc
if __name__ == '__main__':
    image_width = 400

    # backround image set up
    background_image = "background.gif"
    wn.addshape(background_image)

    wn.setup(height=320, width=image_width)

    wn.mainloop()
    
'''' This was originally part of the scrolling background that was scrapped
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
