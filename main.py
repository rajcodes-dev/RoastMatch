import random
print("----- Welcome to the RoastMatch -----")
roast = ["You both get divorce in 2 months.\n",
         "You both are getting married in 2 months.\n"]
while(True):
    ran = random.choice(roast)
    user_1 = input("Enter first name: \n")
    user_2 = input("Enter second name: \n")
    print(ran)
    play = input("Do you want to play again(y/n):\n")
    print('\n')
    if play.lower() == 'n':
        print("Goodbye! Be happy with your relationship.\n")
        break
    print("Oho!, You dare to play this game again.")