import random

coins = 1000
print("You have 1000 coins")
print("Choose a number between 1 and 3")
print("A correct guess Triples your money while a wrong guess halves it")
print("Typing 0 ends the game")

while True:
    
    Winning_Number = random.randint(1,3)

    #Take suitable player input
    try:
        Player_Guess = int(input("Take a Guess: "))
    except ValueError:
        print("Choose a suitable guess")
        continue

    if (Player_Guess == Winning_Number):
        coins = coins*3
        print("Right Guess!!!")

    #Quit Game
    elif (Player_Guess == 0):
        print("You quit with", coins, "coins")
        break

    elif ((Player_Guess != 3) and (Player_Guess != 2) and (Player_Guess != 1)):
        print("Choose a suitable guess")

    else :
        coins = coins/2
        print("Wrong Guess!")

    coins = round(coins)

    #Lose Game
    if (coins <= 10):
        print("You have 10 coins or less")
        print("You lost")
        break

    print("You have", coins, "coins remaining")