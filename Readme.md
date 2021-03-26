<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Guess The Number

Marcelo Motta
DAPT Mar 2021

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
In this project, I created a guessing game called 'Guess The Number' using most of the python commands I've learned so far. The game which I created takes multilple inputs from the player - name, level of the game, and the guessing number -, and interacts with the player proving tips when the player don't guess the correct number, and the final score.

## Rules
The game consists of guessing the correct number out of an universe that can be of 10, 20, or 40 numbers, depending on the level that the player chooses (easy, medium, hard).
The player will have 5 attempts to guess the correct number.
While the player hasn't exceeded his/her 5 attemps, for every wrong attempt there is going to be a tip which will inform the player if the secret number is higher of lower than the number the player has last guessed (input).
A final score will be displayed at the end of the game according to the following criteria:

* Scores are added by 20 points
* Guess the number in the first attempt = 100
* Game over (not guessing after 5 attempts) = 0

## Workflow
During this project I used the following work flow:
* As the first step, I wanted to give the player the opportunity to choose the level of the game. Therefore I created a while loop that will only breaks once the player chooses a game level between the available choices.
* Once the player picks the game-level, the code exits the while loop and enters a second block of code. In this part, I used a python package (random) that allows the code to generate a random number within a set boundary.
* Once the number has been choosen, a new block of codes compares the code generated number (described above) with the number input by the player.
* The game ends if certain conditions stablished by compared the numbers (as described above) are met.

## Organization
I organized my work manually, creating to-do list on my notebook.
My repository consists of a readme file and a coding file.

## Links
* Hereyby the link of the repository (https://github.com/marcelohmotta/data_analytics202103_project1)

