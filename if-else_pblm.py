#GUESS THE NUMBER

print("Guess the number")
n = int(input())
i = 0
while(i<=9):
    i = i+1
    if n<18 or n>18 :
        print("guess is wrong")
        print("number of guesses left",9-i)
        break
    elif n==18:
        print("You won")
    else:
        print("Game over")


