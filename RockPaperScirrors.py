from random import randint

num = int(input("Choose no of rounds"))
notover = True
your_score = 0
bot_score = 0
for i in range(num):
    con = input("Do you want to continue")
    if con.lower() == "yes":
        rps = int(input("Choose Rock | Paper | Scissors: "))
        bot_rps = randint(1,3)

        if rps == bot_rps:
            if rps == 1:
                print("You Choose Rock")
                print("Bot Choose Rock")
            if rps == 2:
                print("You Choose Paper")
                print("Bot Choose Paper")
            if rps == 3:
                print("You Choose Scissors")
                print("Bot Choose Scissors")
            print("Its a Draw")
#             if you choose Rock
        elif rps == 1 and bot_rps == 3:
            print(f"You Choose Rock")
            print(f"Bot Choose Scissors")
            print("You Won")
            your_score+=1
            i
        elif rps == 1 and bot_rps == 2:
            print(f"You Choose Rock")
            print(f"Bot Choose Paper")
            print("You Lost")
            bot_score += 1
#             if you choose Paper
        elif rps == 2 and bot_rps == 1:
            print(f"You Choose Paper")
            print(f"Bot Choose Rock")
            print("You Won")
            your_score+=1
        elif rps == 2 and bot_rps == 3:
            print(f"You Choose Paper")
            print(f"Bot Choose Scissors")
            print("You Lost")
            bot_score += 1
#             if you choose Scissors
        elif rps == 3 and bot_rps == 1:
            print(f"You Choose Scissors")
            print(f"Bot Choose Rock")
            print("You Lost")
            bot_score += 1
        elif rps == 3 and bot_rps == 2:
            print(f"You Choose Scissors")
            print(f"Bot Choose Paper")
            print("You Win")
            your_score += 1

    if con.lower() == "no":
        print("--------Thanks for playing--------")
        break

print(f"{your_score} | {bot_score}")

if your_score > bot_score:
    print("Congrats, You Win..")
if your_score == bot_score:
    print("It was a draw.Better luck next time")
if your_score < bot_score:
    print("You Lost.Better luck next time")
