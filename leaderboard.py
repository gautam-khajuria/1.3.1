file_name = 'lb.txt'

# Returns the leaderboard text file as a list
def read_lb(permissions):
  return open(file_name, permissions) # Open the file name with read permissions

def load_lb():
  lb = read_lb('w') # Get the lb

  for line in lb:
    # Parse the data. Data is in format 'name<::>score' (to not restrict user names)
    # Because of this, we can split by '<::>'
    player = line.split('<::>')
    if player[1] <= player_score:
      pass # More work needs to be done

# Inserts a player into the leaderboard
def insert_player(player_name, player_score):
  lb = read_lb('w') # Get the lb

  for line in lb:
    # Parse the data. Data is in format 'name<::>score' (to not restrict user names)
    # Because of this, we can split by '<::>'
    player = line.split('<::>')
    if player[1] <= player_score:

