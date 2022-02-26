def main():
    """
    This program displays the record that are in the golf.txt file
    """
    #Open the golf.txt file for reading.
    players_data = open('golf.txt', 'r')

    name = players_data.readline().rstrip()
    #While name is not empty, continue processing
    while name != '':
        score = eval(players_data.readline().rstrip('\n'))

        #Display the record.
        print('Name:', name)
        print('Score:', score)
        print()

        # Read the name field of the next record.
        name = players_data.readline().rstrip()

    #Close the file.
    players_data.close()

main()