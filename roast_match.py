# Relationship Predictor Game (RoastMatch)

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
                user_interface.show_roast(user_1, user_2, roast)

            play = user_interface.play_again()

            if play == 'n':
                    user_interface.show_goodbye()
                    break
            user_interface.show_continue_message()

class RoastEngine:
    """Generate and maintain the roast."""

    roasts = [
    "Yeh dono message karte hain lekin reply 3 din baad aata hai.\n",
    "Inka idea of date: ek dusre ka story dekh ke like nahi karna.\n",
    "Saath mein plan banate hain aur last minute 'thak gaya' bol dete hain.\n",
    "Inka love language: 'seen' pe chod dena.\n",
    "Yeh dono fight ke baad bhi mutual friends se ek dusre ki khabar "
    "lete hain.\n",
    "Inka future: shaadi ke baad bhi alag-alag Netflix accounts.\n",
    "Flirting style: 'haha' react kar ke conversation khatam.\n",
    "Yeh dono birthday wish mein bhi copy-paste karte hain.\n",
    "Inka couple goal: ek dusre ko blue tick maar ke 'busy tha' bolna.\n",
    "Saath mein photo khinchate hain aur dono ko hi pasand nahi aati.\n",
    "Inka romance: bijli jaane pe candle jalana aur phone charge karna.\n",
    "Yeh dono reel save karte hain ek dusre ke liye aur kabhi bhejte nahi.\n",
    "Inka biggest fight: 'tu hi text kar na pehle'.\n",
    "Saath mein trip plan karte hain aur end mein ghar pe baithe reh "
    "jaate hain.\n",
    "Inka communication: sirf emoji se baat karna.\n",
    "Yeh dono good morning message mein bhi 'gm' likhte hain.\n",
    "Inka relationship status: 'it's complicated' since day 1.\n",
    "Saath mein grocery jaate hain aur bill pe lad padte hain.\n",
    "Inka idea of surprise: birthday pe bhi 'happy birthday' copy karna.\n",
    "Yeh dono call karne se pehle 10 baar sochte hain.\n",
    "Inka love: ek dusre ke phone mein last seen check karna.\n",
    "Saath mein movie dekhne baithe aur poora time phone pe lage rehna.\n",
    "Inka future plan: ek dusre ko block kar ke status poochna.\n",
    "Yeh dono 'sorry' bolne se allergy hai lekin expect karte hain.\n",
    "Inka flirting: 'thik hai' bol ke conversation end kar dena.\n",
    "Saath mein khana order karte hain aur cancel kar dete hain.\n",
    "Inka couple selfie: dono alag direction mein dekh rahe hote hain.\n",
    "Yeh dono anniversary bhool jaate hain aur bolte hain "
    "'network issue tha'.\n",
    "Inka romance level: chai thandi hone tak wait karna.\n",
    "Saath mein gym join karte hain aur first day ke baad 'kal se'.\n",
    "Inka true bond: ek dusre ko judge karte rehna silently.\n",
    "Yeh dono plan banate hain aur mood nahi hone pe cancel.\n",
    "Inka biggest flex: ek dusre ko read receipts on rakh ke torture karna.\n",
    "Saath mein canteen jaate hain aur ek plate maggi share karne pe ladai.\n",
    "Inka relationship goal: ek dusre ka Insta story dekh ke like na karna.\n",
    "Yeh dono 'call karun?' soch ke 2 ghante nikal jaate hain.\n",
    "Inka love language: passive-aggressive 'kuch nahi' bolna.\n",
    "Saath mein bike pe ghumte hain aur petrol khatam hone pe blame game.\n",
    "Inka future: alag-alag rooms mein Netflix dekhna shaadi ke baad.\n",
    "Yeh dono 'I miss you' bolne se pehle 100 baar sochte hain.\n",
    "Inka communication: raised eyebrow aur silence.\n",
    "Saath mein PUBG khelte hain aur last zone mein report kar dete hain.\n",
    "Inka couple goal: ek dusre ko silently roast karte rehna.\n",
    "Yeh dono 'tu hi sorry bol' pe 3 din tak baat nahi karte.\n",
    "Inka romance: reel dekh ke tag karna aur comment mein 'bhai' likh dena.\n",
    "Saath mein exam padhte hain aur notes maang ke 'tu hi padh le' "
    "bol dete hain.\n",
    "Inka true love: ek dusre ke memes forward karna bina credit diye.\n",
    "Yeh dono fight ke baad bhi ek dusre ka story dekh lete hain.\n",
    "Inka dream date: AC on karke bahar ki garmi discuss karna.\n",
    "Made for each other — dono ko time pe reply karne se allergy hai.\n",
    "Yeh dono ek dusre ko dekh ke hi 'kuch nahi' bol dete hain.\n",
    "Inka relationship: typing... likh ke cancel kar dena.\n"
]
    
    def generate_roast(self, user_1, user_2):
        """Return roast to game controller."""
        seed = sum(ord(c.lower()) for c in user_1 if c.isalpha()) +\
        sum(ord(c.lower()) for c in user_2 if c.isalpha()) 

        seed += len(user_1) * 10 + len(user_2) * 10 

        selected_roast = seed % len(self.roasts)
        return self.roasts[selected_roast]

class UserInterface:
    """Display the roast and overall user interface."""

    def greet(self):
        print("=" * 60)
        print("🔥🔥 ROASTMATCH 🔥🔥".center(60))
        print("The most savage relationship & friendship roaster".center(60))
        print("Do naam daalo... agar himmat hai toh 😈".center(60))
        print("=" * 60)
        print()  

    def users(self):
        user1 = input("😈 Pehla victim ka naam daal: ").strip().capitalize()
        user2 = input("😈 Dusra victim ka naam daal: ").strip().capitalize()
        return user1, user2

    # def empty_names(self):
    #     print("Arre bhai! Invisible naam nahi chalega 💀")
    #     print("Proper naam daal na, warna kaise roast karun? 😏\n")

    empty_names = lambda self: print("Arre bhai! Invisible naam nahi "
                                     "chalega 💀 \nProper naam daal na, "
                                     "warna kaise roast karun? 😏\n"
                                     )
    
    def loading(self):
        print("\n🔮 Compatibility analyze kar raha hoon...")
        print("Ancient shade scrolls khol raha hoon...")
        print("Maximum emotional damage calculate ho raha hai...")
        print("Ultimate burn ready kar raha hoon... 💀\n")

    def show_roast(self, user_1, user_2, roast):
        print("═" * 70)
        print("💥💥 ULTIMATE ROAST RESULT 💥💥".center(70))
        print(f"🔥 {user_1} + {user_2} 🔥".center(70))
        print("═" * 70)
        print()
        print(roast.strip().center(70))
        print()
        print("═" * 70)
        print("😈 Share kar apne doston ke saath... "
              "agar himmat hai! 😏".center(70)
              )
        print("═" * 70)
        print()

    play_again = lambda self: input("🔥 Ek aur pair ki beizzati "
        "karwaayega? (y/n): ").strip().lower()

    def show_continue_message(self):
        print("Arre waah! Phir se apni izzat lootne aaya?")
        print("Confidence level: PRO MAX 😈🔥\n")

    def show_goodbye(self):
        print("👋 Bhaag gaya? Smart move tha bro.")
        print("Goodbye! Relationship mein khush raho... "
              "ya try karte raho 😘\n"
              )

if __name__ == "__main__":
    roast_engine = RoastEngine()
    user_interface = UserInterface()
    controller = GameController(roast_engine, user_interface)
    controller.run()