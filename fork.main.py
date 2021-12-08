import turtle as trtl
import random as rng
import leaderboard as lb
import time

'''
Instructions: Press 'w' or 's' to move up or down, and collect all of the moving coins. However, DO NOT collect objects that are red or are a triangle. If you do, you lose a point.
'''

# 0.3.2

# Instantiate objects
pen = trtl.Turtle()
pen.hideturtle()
obj = trtl.Turtle()
obj.penup()
wn = trtl.Screen()

font_setup = ("Arial", 20, "bold")

# Timer drawing turtle
counter = trtl.Turtle()
counter.speed(0)
counter.penup()
counter.hideturtle()

# lb turtle
leaderboard_turtle = trtl.Turtle()
leaderboard_turtle.speed(0)
leaderboard_turtle.penup()
leaderboard_turtle.hideturtle()

# Score turtle
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.speed(0)
score_writer.penup()

# The player name will not be allowed to contain <::>
# This is to prevent an injection attack on the leaderboard
# In which a user would input their name, the sequence, and a really high score to be put into the leaderboard
# (Basic security lol)

# Get player name for scoring
player_name = None
error = 'Enter your name'
while player_name == "" or player_name == None or '<::>' in player_name: # Input validation
  player_name = trtl.textinput(error, "Hi player! What is your name?")
  
  # If the window is displayed again, there was an error so we can ensure that this will always need to happen
  error += " (Cannot contain sequence '<::>' or be empty)"

# Score/timer config
score = 0
timer = 10
timer_up = False

# Go to proper location
score_writer.goto(-200, 130)
score_writer.write("Score starts at 0", font=font_setup)  

# Coins control
amount_of_coins = 1
coins = []

# Leaderboard config
leaderboard_file_name = "lb.txt"
leader_names_list = []
leader_scores_list = []

# Following lists control the shape, size, and colors of the coins. This makes the game more interesting, and makes it harder to discern whether or not it is a coin or obstacle
coin_colors = ['green', 'blue', 'yellow', 'orange', 'pink', 'red']
coin_shapes = ['turtle', 'square', 'circle', 'arrow', 'classic', 'triangle']
coin_sizes = [0.5, 1, 2]

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

# Manages the leaderboard by checking when the timer is over and then adding the score to the leaderboard
def manage_lb():
    global leader_scores_list
    global leader_names_list
    global score
    global leaderboard_turtle

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    if len(leader_scores_list) < 5 or score > leader_scores_list[4]:
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, leaderboard_turtle, score)
    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, leaderboard_turtle, score)

# Manages the timer, and also counts it down
def countdown():
    global timer, timer_up, score, player_name
    counter.clear()
    if timer <= 0:
        counter.goto(-25, 0)
        timer_up = True
        manage_lb()
    else:
        counter.goto(150, 130)
        counter.write(str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, 1000)

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
    global timer_up

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


    while True:
        if timer_up:
          return

        # Calculate distance from coin to player
        distance_x = abs(coin.xcor() - obj.xcor())
        distance_y = abs(coin.ycor() - obj.ycor())


        coin.backward(2.5)
        # Check for collision or screen end
        if distance_x <= 20 and distance_y <= 45:
            coin.hideturtle()
            print("coll")
            # Update the score if this is a coin, or reduce it if this is an obstacle
            update_score() if not is_obstacle else decrement_score() # python ternary gives me a stroke

            break  # collision
        if coin.xcor() <= -200:
            coin.hideturtle()
            print("end screen")
            break

        wn.update()

    # Collision has occured, or screen has been reached
    rand_pos(coin)

    # Return the chosen back to the array
    coin_shapes.append(shape)
    coin_colors.append(color)
    coin_sizes.append(size)

    # Restart its movement
    if not timer_up:
      start_coin(coin)


# Moves the apple object up by 5 pixels
def movement_up():
    global obj, timer_up
    if timer_up:
      return
    obj.penup()
    if obj.ycor() <= 150: # Boundary
      obj.goto(obj.xcor(), obj.ycor() + 5)

# Moves the apple object down by 5 pixels
def movement_down():
    global obj, timer_up
    if timer_up:
      return
    obj.penup()
    if obj.ycor() >= -150: # Boundary bottom
      obj.setpos(obj.xcor(), obj.ycor() - 5)

# Creates key listeners for the up and down keys (either w/s, or arrow keys)
def movement():
  # Get mode of input
  mode = ''
  while True:
    mode = trtl.textinput('Key Input Type', "Do you prefer arrow keys (up and down) or keyboard keys (w and s) for movement? \nEnter 'keyboard' for keyboard keys and 'arrow' for arrow keys.")

    # Check if valid input has been entered, and if so break out of the loop
    if mode == 'keyboard' or mode == 'arrow':
      break

  # User chose keyboard input
  if mode == 'keyboard':
    wn.onkeypress(movement_up, 'w')
    wn.onkeypress(movement_down, 's')
  
  # User chose arrow input
  if mode == 'arrow':
    wn.onkeypress(movement_up, 'Up')
    wn.onkeypress(movement_down, 'Down')

# --- #

# Starts and listens for key presses
movement()
wn.listen()

# Start the timer
countdown()

# Controls main loop for game, including background, dimensions, etc
if __name__ == '__main__':
    image_width = 400

    # backround image set up
    background_image = "background.gif"
    wn.addshape(background_image)
    wn.bgpic(background_image)
    wn.setup(height=320, width=image_width)

    # Generates, and starts all coins
    generate_coins()

    for coin in coins:
      start_coin(coin)

    print("end of game")
    # Hide everyone
    obj.hideturtle()
    for coin in coins:
      coin.hideturtle()
    score_writer.clear()

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
