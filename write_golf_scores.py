#  Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club president 
# has asked you to write two programs:
# 1. A program that will read each player’s name and golf score as keyboard input, then 
# save these as records in a file named golf.txt. (Each record will have a field for the 
# player’s name and a field for the player’s score.)
# 2. A program that reads the records from the golf.txt file and displays them.

def main():
    """This function accepts input from the user and saves them in a txt file."""
    #Get the number of players
    no_of_players = int(input('How many players are contesting? ')) 

    #Open a file for writing.
    players_data = open('golf.txt', 'w')

    #Get input for each player
    for player in range(1, no_of_players+1):
        print('Enter data for player #', player, sep='')
        name = input("Name: ")
        score = eval(input("Score: "))
        print()

        #Write each player data into the golf.txt file.
        players_data.write(name + '\n')
        players_data.write(str(score) + '\n')

    #Close the file
    players_data.close()
    print('Data added to golf.txt file.')

main()