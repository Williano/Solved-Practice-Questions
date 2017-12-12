# Script: GolfScores.py
# Description: This program that will read each player’s name and golf score as keyboard input, and then
#              save these as records in a file named golf.txt. (Each record will have a field for the
#              player’s name and a field for the player’s score.)
# Programmer: William Kpabitey Kwabla
# Date: 17.11.16


# Defining the main function of the program.
def main():
    # Asking for number of golf players.
    number_of_players = eval(input("Please Enter the number of players: ")

    # Opening the golf.txt file to write records to.
    golf_scores = open("golf.txt", 'w')

    # Looping to accept all records for players.
    for count in range(1, number_of_players + 1):
        # Displaying to user to enter records.
          print("Please Enter your records")

        # Asking user for his/her name.
          name = input("Please Enter your name: ")

        # Asking user for his/her golf score.
          scores = eval(input("Please Enter your score: ")

        # Writing users record to file.
          golf_scores.write(name + '\n')
          golf_socres.write(str(scores) + '\n')

    # Closing the file and writing to the golf.txt file.
    golf_scores.close()

# Calling the main function to execute the program.
main()
