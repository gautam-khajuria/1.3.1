file_name = 'lb.txt'

# Returns the leaderboard text file as a list
def read_lb(permissions):
  return open(file_name, permissions) # Open the file name with read permissions

def load_lb():
  lb = read_lb('w') # Get the lb

  arr = []

  for line in lb:
    # Parse the data. Data is in format 'name<::>score' (to not restrict user names)
    # Because of this, we can split by '<::>'
    arr.append(line)

  return arr
    
      

# Inserts a player into the leaderboard
def insert_player(player_name, player_score):
  data = load_lb()

  for line in data:
    # Parse the data. Data is in format 'name<::>score' (to not restrict user names)
    # Because of this, we can split by '<::>'
    player = line.split('<::>')
    if player[1] <= player_score: # Check if player's score is higher than lb score
      # If so, set current lb to this player
      line = player_name + '<::>' + str(player_score)

  lb = read_lb('w')

  # Overwrite the data in the leaderboard
  for i in range(len(lb)):
    lb[i] = data[i]