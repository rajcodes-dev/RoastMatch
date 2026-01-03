class GameController:
    """Control the main game loop."""

    def __init__(self, roast_engine, user_interface):
        self.roast_engine = roast_engine
        self.user_interface = user_interface

    def run(self):
        """Run the main loop of the game."""
        
        user_interface.greet()
        while(True):

            user_1, user_2 = user_interface.users()

            if not user_1 or not user_2:
                user_interface.empty_names()
                continue

            else:
                user_interface.loading()
                roast = roast_engine.generate_roast(user_1, user_2)
                user_interface.show_roast(roast)

            play = user_interface.play_again()

            if play == 'n':
                    user_interface.show_goodbye()
                    break
            user_interface.show_continue_message()

class RoastEngine:
    """Generate and maintain the roast."""

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
    
    def generate_roast(self, user_1, user_2):
        """Return roast to game controller."""
        seed = len(user_1) + len(user_2) 
        + ord(user_1[0].lower()) + ord(user_2[0].lower())

        selected_roast = seed % len(self.roasts)
        return self.roasts[selected_roast]

class UserInterface:
    """Display the roast and overall user interface."""

    def greet(self):
        print("----- Welcome to RoastMatch -----")  

    def users(self):
        user1 = input("Enter first name: \n").strip().capitalize()
        user2 = input("Enter second name: \n").strip().capitalize()
        return user1, user2

    def empty_names(self):
        print("What are you doing man? Atleast input the name so" 
                      " that i can predict your broken relationship.\n")
    
    def loading(self):
        print("Analyzing.......\n")

    def show_roast(self, roast):
        print(roast)

    def show_goodbye(self):
        print("Goodbye! Be happy with your relationship.\n")

    def play_again(self):
        return input("Do you want to play again(y/n):\n").lower()

    def show_continue_message(self):
        print("Oho!, You dare to play this game again.")

if __name__ == "__main__":
    roast_engine = RoastEngine()
    user_interface = UserInterface()
    controller = GameController(roast_engine, user_interface)
    controller.run()