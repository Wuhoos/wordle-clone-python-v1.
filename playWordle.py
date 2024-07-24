from wordle import Wordle
from colorama import Fore

def main():
    print ("Hello Wordle")
    wordle = Wordle('Apple')

    while wordle.canAttempt:
        x = input("Type yout guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f'Word must be {wordle.WORD_LENGTH} characters long' + Fore.RESET)
            continue

        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result , sep='\n')
        
    if wordle.isSolved:
        print('Puzzle solved')
    else:
        print('not solved')

    print (wordle)




if __name__ == '__main__':
    main()