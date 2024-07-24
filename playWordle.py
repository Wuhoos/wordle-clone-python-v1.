from wordle import Wordle
from colorama import Fore
from letterState import LetterState
import random

def main():

    wordSet = loadWordSet('data/wordsSource.txt')
    secret = random.choice(list(wordSet))

    wordle = Wordle(secret)

    while wordle.canAttempt:
        x = input("\n Type yout guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f'Word must be {wordle.WORD_LENGTH} characters long' + Fore.RESET)
            continue

        wordle.attempt(x)
        displayResults(wordle)
        
    if wordle.isSolved:
        print('Puzzle solved')
    else:
        print(f'Could not solved: {wordle.secret}')

    print (wordle)

def displayResults(wordle: Wordle):
    print('\nResult so far...')
    print(f'You have {wordle.remainingAttempts} attempts left\n')

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        coloredResultStr = convertResultToColor(result)
        lines.append(coloredResultStr)
    
    for _ in range(wordle.remainingAttempts):
        lines.append(" ".join('_' * wordle.WORD_LENGTH))

    drawBorder(lines)

def loadWordSet(path: str):
    wordSet = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            wordSet.add(word)
    return wordSet

def convertResultToColor(result: list[LetterState]):
    resultWithColor = []
    for letter in result:
        if letter.isInPosition:
            color = Fore.GREEN
        elif letter.isInWord:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        coloredLetter = color + letter.character + Fore.RESET
        resultWithColor.append(coloredLetter)
    return " ".join(resultWithColor)
    

def drawBorder(lines:list[str], size: int = 9, pad: int = 1):

    contentLength = size + pad * 2
    topBorder = '┌' + '─' * contentLength + '┐'
    bottomBorder = '└' + '─' * contentLength + '┘'
    space = " " * pad
    print(topBorder)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottomBorder)



if __name__ == '__main__':
    main()