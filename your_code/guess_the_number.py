# Guess the number game

import random

level = [10, 20, 40]
easy = level[0]
medium = level[1]
hard = level[2]

game_over = True
name = input("Please type your name: ")

while game_over:
    num = input(
        "Choose the level of the game. \nType E for easy; M for medium; or H for hard): ")
    if num == "E" or num == "M" or num == "H":
        print("Let's play!")
        game_over = False
        for x in level:
            if num == "E":
                x = easy
            elif num == "M":
                x = medium
            elif num == "H":
                x = hard
    else:
        print("Invalid input! Try again! \nPlease type E for easy; M for medium; or H for hard when choosing the level of the game.")

# print(x)
secrect_number = random.randint(1, x)

# print(secrect_number)

guess = None
count = 1
# print(type(count))


while guess != secrect_number:
    guess = input("Please type a number between 1 and " + str(x) + ": ")
    # print(guess)
    # print(type(guess))
    if guess.isdigit():
        guess = int(guess)

    if guess == secrect_number:
        # count = 1
        print("Congratulations, " + str(name) + ". You got it!")
        print("It took you " + str(count) + " times!")
        break
    elif guess < secrect_number:
        print(
            "The number you guessed is too low! Please try again with a greater number!")
        count = count + 1
    elif guess > secrect_number:
        print(
            "The number you guessed is too high! Please try again with a lesser number!")
        count = count + 1
    if count == 5:
        print("YOUR LAST CHANCE!")
    elif count > 5:
        print("Sorry, you failed!")
        print("The secret number is: ", str(secrect_number))
        break


def final_score(count):
    if count == 1:
        return 100
    if count > 1 and count <= 5:
        return 100 - (20 * int(count))
    if count > 5:
        return 0


score = final_score(count)
print("Your final score is: " + str(score))
