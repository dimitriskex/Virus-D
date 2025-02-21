import random 
from colorama import Fore, Style, init
import time
import sys 
import os

                                        #Virus - D Game 


def start_game():
    time.sleep(1)
    print(Fore.RED + "\t\t ██████╗ ██╗   ██╗███████╗███████╗██████╗      ██████╗ ")
    print(Fore.RED + "\t\t ██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝ ")
    print(Fore.RED + "\t\t ██████╔╝██║   ██║█████╗  █████╗  ██║  ██║    ██║  ███╗")
    print(Fore.RED + "\t\t ██╔═══╝ ██║   ██║██╔══╝  ██╔══╝  ██║  ██║    ██║   ██║")
    print(Fore.RED + "\t\t ██║     ╚██████╔╝███████╗██║     ███═███╔╝    ╚██████╔╝")
    print(Fore.RED + "\t\t ╚═╝      ╚═════╝ ╚══════╝╚═╝     ╚════╝      ╚═════╝ \n")
    time.sleep(1)
    print(Fore.YELLOW + "\t\t\t\t Welcome to Virus D!")
    time.sleep(1)
    print(Fore.YELLOW + "\nA deadly virus has ravaged the city, leaving chaos and destruction in its wake.")
    time.sleep(1)
    print(Fore.YELLOW + "As one of the last survivors, your mission is to escape the infected city and start a new.")
    time.sleep(1)
    print(Fore.YELLOW + "You must navigate dangerous areas, scavenge for supplies, and avoid the infected at all costs.")
    time.sleep(1)
    print(Fore.YELLOW + "Every choice you make will determine your survival. Can you make it out alive?")
    
    player = { 
        "health": 100,
        "score": 0,
        "supplies": 0,
        "medicine": 1
    }



    player_name=input(Fore.RED+"\n\nEnter your name:")

    print("\n\nTime to get the job done "+player_name)

    time.sleep(0.5)

    loading_animation(Fore.YELLOW+"\n\nLets start")

    os.system("cls" if os.name == "nt" else "clear")


    game_loop(player)




   


def game_loop(player):
    while player["health"] > 0 & player["score"]<100 :
        print(Fore.LIGHTYELLOW_EX+ "\nWhat do you want to do?")
        print(Fore.LIGHTYELLOW_EX + "\n1. Move to another area")
        print(Fore.LIGHTYELLOW_EX + "\n2. Check your status")
        print(Fore.LIGHTYELLOW_EX + "\n3. Use medicine")
        print(Fore.LIGHTYELLOW_EX + "\n4. Quit the game")
        
        choice = input(Fore.YELLOW + "\n\n\nEnter your choice: ")
        if choice == "1":
            os.system("cls" if os.name == "nt" else "clear")
            explore_area(player)

        elif choice == "2":
            os.system("cls" if os.name == "nt" else "clear")

            check_status(player)
        elif choice == "3":
            os.system("cls" if os.name == "nt" else "clear")

            use_medicine(player)
        elif choice == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.YELLOW + "Goodbye! Stay safe")
            break
        else:
            print(Fore.RED + "Invalid choice! Please try again")

    if player["health"] <= 0:
        print(Fore.YELLOW + "You died ")


    if player["score"]>=100:
        print(Fore.YELLOW + "You WONNNNNNN")

def explore_area(player):
    loading_animation("Exploring the new area")
    areas = random.choice(["Town Hall🏫", "City Center 🛒", "Abandoned Hospital 🏥", "Gas Station ⛽"])
    print(Fore.GREEN + "You just entered " + areas)


    if areas == "Town Hall🏫":
        print(Fore.GREEN+"The historic place where most of city's events took place... Mayor and his staff are all dead because of this deadyly virus")
        print(Fore.GREEN+" A mysterious radio message plays from a speaker. Someone might still be inside…")
        



    elif areas == "City Center 🛒":
        print(Fore.GREEN+"The streets are full of abandoned cars and broken storefronts")

    elif areas == "Abandoned Hospital 🏥":
        print(Fore.GREEN+"💉 Inside a research lab, a sealed vial labeled --> Antidote Prototype <-- lies on a desk.🚷 \nA locked door rattles… someone (or something) is inside.")

        print(Fore.CYAN + "\nBackstory Drama: The Antidote Prototype 💉 - The Final Betrayal – Dr. Carter’s Last Log")
        print(Fore.LIGHTBLUE_EX + "\n🔬 Dr. Elias Carter’s Voice Recording – Found in a Blood-Stained Recorder.")
        print(Fore.LIGHTBLUE_EX + "\n\"This is Dr. Carter… If you're listening to this, then we failed. The city is lost. The virus was never meant to spread beyond containment, yet here we are—on the brink of extinction. We had one chance, one antidote, but…\"\n")
        time.sleep(2)
        print(Fore.LIGHTBLUE_EX + "(Static noise. Heavy breathing.) \"They took it from me. The military arrived last night. They stormed in, demanded the prototype, and when I refused, they… they shot Dr. Patel. Right in front of me. Said it was 'for the greater good'—that they were taking it to a 'secure facility.' But I know the truth. There is no facility. There is no cure for them. Only power.\"\n")
        time.sleep(2)
        print(Fore.LIGHTBLUE_EX + "\"I managed to make a second vial, a secret one. It’s here, in this lab. But it’s not perfect. It needs one final compound to stabilize… and without it, I don’t know what it will do. Could cure… could kill. Could be worse.\"\n")
        time.sleep(2)
        print(Fore.LIGHTBLUE_EX + "(A loud bang in the background. Screams. Gunfire.)\n")
        time.sleep(2)
        print(Fore.LIGHTBLUE_EX + "\"They’re here. I don’t have much time. If you find this recording… if you find the antidote… you have to finish what we started. You have to make a choice. Use it… or burn it.\"\n")
        print(Fore.LIGHTBLUE_EX + "(The recording cuts to silence.)")


    elif areas == "Gas Station ⛽":

        print (Fore.GREEN+"🛢️ The gas station is eerily silent, its fuel pumps long empty.🚘\n A car sits outside with keys in the ignition. The fuel gauge reads “Half-Full”.📜 \nA blood-stained note on the dashboard says: They're everywhere. If you find this, RUN.")



    events = random.choice(["infected", "supplies", "contaminated_zone", "safe_zone"])

    if events == "infected":


        print(Fore.LIGHTRED_EX + "\n\nAn infected person appears! They are aggressive!")
        choices_1 = input(Fore.LIGHTYELLOW_EX + "Fight or Run (F) or (R): ")


        if choices_1 == "F":
            r1 = random.choice(["decrease_health", "Kill_Infected"])

            if r1 == "decrease_health":
                player["score"]-=10
                print("You just lost 20 health")
                player["health"] -= 20
                
            elif r1 == "Kill_Infected":
                
                player["score"]+=random.randint(10,20)
                print("You just killed the infected Person. Nice Job!")

        elif choices_1 == "R":


            r2 =random.choice(["Successful","Death"])

            if r2 == "Successful":
                print(Fore.YELLOW + "You managed to escape safely!")

            elif r2 == "Death":
                player["health"]==0
                

            return
        
        else:
            print("Invalid choice! Type again")
        
    elif events == "supplies":

        print(Fore.BLUE + "\n\nYou found some valuable supplies!")
        player["supplies"] += random.randint(5, 20)
        player["score"] += 10


    elif events == "contaminated_zone":

        print(Fore.LIGHTMAGENTA_EX + "\n\nYou entered a contaminated area... Losing health!")
        player["health"] -= random.randint(10, 30)


    elif events == "safe_zone":

        print(Fore.LIGHTBLUE_EX + "\n\nYou found a temporary safe zone. Rest and gather your thoughts.")








def check_status(player):  

    loading_animation_check_status(Fore.LIGHTGREEN_EX + "\n\n\t\tPlayer's Current Status:")
    loading_animation_check_status(Fore.LIGHTGREEN_EX + f"\n💖 Health: {player['health']}")
    loading_animation_check_status(Fore.LIGHTGREEN_EX+ f"🏆 Score: {player['score']}")
    loading_animation_check_status(Fore.LIGHTGREEN_EX+ f"🎒 Supplies: {player['supplies']}")
    loading_animation_check_status(Fore.LIGHTGREEN_EX+ f"💊 Medicine: {player['medicine']}")






def use_medicine(player):

    if player["medicine"] > 0:
        
        print(Fore.CYAN + "You use medicine to heal 30 health points.")
        player["health"] += 30
        player["medicine"] -= 1
        print(Fore.LIGHTCYAN_EX+"Health:"+player["health"])
    else:
        print(Fore.RED + "You have no medicine left!")







def loading_animation(message="Loading", duration=3):
    print(Fore.YELLOW + message, end="", flush=True)
    for _ in range(duration):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n")


def loading_animation_check_status(message="Loading", duration=3):
    print(Fore.YELLOW + message, end="", flush=True)
    for _ in range(duration):
        time.sleep(0.2)
        sys.stdout.write("")
        sys.stdout.flush()
        
    print("\n")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    start_game()
