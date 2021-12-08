#   leaderboard.py
# The leaderboard module to be used in a122 solution.

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25


# load leaderboard from file
def load_leaderboard(file_name, leader_names, leader_scores):
    leaderboard_file = open(file_name, "r")  # need to create the file ahead of time in same folder

    # use a for loop to iterate through the content of the file, one line at a time
    # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
    for line in leaderboard_file:
        # Split string, extract values
        line_split = line.split('<::>')
        leader_name = line_split[0]
        leader_score = line_split[1]

        # Append values to respective arrays
        leader_names.append(leader_name)
        leader_scores.append(int(leader_score))  # Cast score from string to int

    leaderboard_file.close()


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    leader_index = 0

    while leader_index < len(leader_names):
        if player_score >= leader_scores[leader_index]:
            break
        else:
            leader_index = leader_index + 1

    leader_names.insert(leader_index, player_name)
    leader_scores.insert(leader_index, player_score)

    if len(leader_names) >= 6:
        leader_names.pop()

    if len(leader_scores) >= 6:
        leader_scores.pop()

    # store the latest leaderboard back in the file
    leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
    leader_index = 0

    while leader_index < len(leader_names):
        leaderboard_file.write(leader_names[leader_index] + "<::>" + str(leader_scores[leader_index]) + "\n")
        leader_index = leader_index + 1

    leaderboard_file.close()


# draw leaderboard and display a message to player
def draw_leaderboard(leader_names, leader_scores, high_scorer, turtle_object, player_score):
    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-200, 100)
    turtle_object.hideturtle()
    turtle_object.down()
    leader_index = 0

    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab
    # space '\t'
    while leader_index < len(leader_names):
        turtle_object.write(
            str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]),
            font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
        turtle_object.down()
        leader_index = leader_index + 1

    # Display message about player making/not making leaderboard based on high_scorer
    if high_scorer:
        turtle_object.write("Congratulations! You made the leaderboard!", font=font_setup)
    else:
        turtle_object.write("Sorry, you didn't make the leaderboard. Maybe next time!\nScore: " + player_score, font=font_setup)

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    if bronze_score <= player_score < silver_score:
        turtle_object.write("You earned a bronze medal!", font=font_setup)
    elif silver_score <= player_score < gold_score:
        turtle_object.write("You earned a silver medal!", font=font_setup)
    elif gold_score <= player_score:
        turtle_object.write("You earned a gold medal!", font=font_setup)
