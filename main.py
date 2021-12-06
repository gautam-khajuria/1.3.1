import turtle as trtl
import random as rng
import time
import threading as thr

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

score = 0
timer_up = False

# Go to proper location
score_writer.goto(-200, 130)
score_writer.write(score, font=font_setup)  

amount_of_coins = 1
coins = []

# Set Speed Fastest
obj.speed(0)
pen.speed(0)

# This creates an object as a APPLE balloon
pear_image = 'pear.gif'
apple_image = 'apple.gif'
wn.addshape(pear_image)
wn.addshape(apple_image)
obj.shape(apple_image)

# Setup coins
coin_image = 'pear.gif'
wn.addshape(coin_image)

# Get player name for scoring
player_name = trtl.textinput("Enter your name", "Hi player! What is your name?")
# Updates the score 

def update_score():
    global score, score_writer, timer_up

    score += 1  # increment score
    score_writer.clear()
    if timer_up:
        return
    score_writer.write(score, font=font_setup)


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

    coin.setpos(x, y)


# Starts a coins movement. This method also resets the coin.
def start_coin(coin):
    time.sleep(0.0001)
    while True:
        distance_x = abs(coin.xcor() - obj.xcor())
        distance_y = abs(coin.ycor() - obj.ycor())

        coin.backward(1)
        if distance_x <= 20 and distance_y <= 20:
            coin.hideturtle()
            print("coll")
            update_score()
            break  # collision
        if coin.xcor() <= -200:
            coin.hideturtle()
            print("end screen")
            break

    # Collision has occured, or screen has been reached
    rand_pos(coin)
    coin.showturtle()
    start_coin(coin)


# 
def movement_up():
    global obj
    obj.penup()
    obj.goto(obj.xcor(), obj.ycor() + 1)


def movement_down():
    global obj
    obj.penup()
    obj.setpos(obj.xcor(), obj.ycor() - 1)

def movement():
    time.sleep(0.001)
    wn.onkeypress(movement_up, 'w')
    wn.onkeypress(movement_down, 's')


# --- #

#create threads for the functions generate_coins and movement
thread1 = thr.Thread(target=movement)
thread2 = thr.Thread(target=generate_coins)
thread1.setDaemon(True)
thread2.setDaemon(True)

#call the threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()

wn.listen()

thread3 = thr.Thread(target=start_coin, args=coin)
thread3.setDaemon(True)

threads = [thread3]
# create and call the setup for the coinn thread
for coin in range():
  threads[0]
  thread3.start()
  thread3.join()


wn.mainloop()
# This block controls the main loop for the game, including the scrolling background.
'''
if __name__ == '__main__':
    image_width = 400

    # backround image set up
    background_image = "background.gif"
    wn.addshape(background_image)
    camera_dx = -3
    camera_x = 0

    wn.setup(height=320, width=image_width)

    wn.mainloop()
    

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
