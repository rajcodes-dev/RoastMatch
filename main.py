import random

class GameController:
    """Control the main game loop."""

    roasts = [
        "Yeh dono ek dusre ko dekh ke hi bolenge 'yaar thoda space de na'.\n",
        "Inka future: ek dusre ko block karke mutual friends se status "
        "poochna.\n",
        "Saath mein photo khinchwayenge aur dono hi delete kar denge.\n",
        "Inka biggest fight: 'tu hi sorry bol na pehle' pe 3 din ka seen "
        "zone.\n",
        "Yeh dono plan banayenge aur last minute 'mood nahi hai' bolke "
        "cancel.\n",
        "Inka love/friendship language: 'thik hai' bolke conversation "
        "khatam.\n",
        "Saath mein khana order karenge aur bill aane pe ek dusre ko dekh "
        "lenge.\n",
        "Inka dream date/hangout: ghar pe baithe phone pe lage rehna.\n",
        "Saath mein trip jayenge aur photos mein alag-alag pose karenge.\n",
        "Inka biggest flex: ek dusre ko blue tick maarna aur phir 'busy tha' "
        "bolna.\n",
        "Yeh dono anniversary/birthday bhool jayenge aur bolenge 'arrey yaad "
        "tha but network issue'.\n",
        "Inka chemistry: chai banane mein jhagda ki kitni cheeni daalni "
        "hai.\n",
        "True bond matlab: ek dusre ke liye reel save karna aur kabhi na "
        "bhejna.\n",
        "Yeh dono couple/friends banenge aur end mein 'we're better as "
        "strangers' bol denge.\n",
        "Inka couple/bro goal: ek dusre ko silently judge karte rehna.\n",
        "Made for each other — dono ko 'sorry' bolna zindagi mein ek baar "
        "bhi nahi aayega.\n"
    ]

    def run(self):
        print("----- Welcome to RoastMatch -----")

        while(True):

            user_1 = input("Enter first name: \n").strip().capitalize()
            user_2 = input("Enter second name: \n").strip().capitalize()

            if not user_1 or not user_2:
                print("What are you doing man? Atleast input the name so that i " \
                "can predict your broken relationship.\n")
                continue

            else:
                seed = len(user_1) + len(user_2) 
                + ord(user_1[0].lower()) + ord(user_2[0].lower())

                selected_roast = seed % len(self.roasts)

                print(self.roasts[selected_roast])

            play = input("Do you want to play again(y/n):\n")
            print('\n')

            if play.lower() == 'n':
                    print("Goodbye! Be happy with your relationship.\n")
                    break
            print("Oho!, You dare to play this game again.")

if __name__ == "__main__":
    controller = GameController()
    controller.run()