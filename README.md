# Wordle Clone

## About

Wordle Game is a Python implementation of the popular word puzzle game. The goal of the game is to guess a secret five-letter word within six attempts. After each guess, the game provides feedback indicating which letters are in the correct position, which are in the word but in the wrong position, and which are not in the word at all.

git clone https://github.com/yourusername/wordle-game.git

## To start the game:
python playWordle 


## Rules
1. Objective: Guess the secret five-letter word within six attempts.

2. Feedback:
        Correct letter and correct position: Displayed as G (Green).
        Correct letter but wrong position: Displayed as Y (Yellow).
        Incorrect letter: Displayed as W (White).

3. Winning: If you guess the word correctly within six attempts, you win!

4. Losing: If you fail to guess the word within six attempts, you lose, and the correct word is revealed.


## Features
Random Word Selection: The game selects a random five-letter word from a predefined list located in the data directory.

User-Friendly Interface: Simple command-line interface for ease of use.

Feedback: Immediate feedback after each guess to help you narrow down the correct word.
