import random
#import random so that we can assign random attack points to the Pokemon in the battle

from pokemon import create_default
from person import Person
from pokemon import Pokemon
from data_handling import table_print
#Importing all of the code from the other files so that we can run the program properly

# Battle Class
class Battle:

    # Create two class attributes
    # 1. A list to store the details of every instance of the Battle class. Creating this list grants us the ability
    #to easily access the details of every battle.
    __all_battles = []
    # 2. An integer of the amount of battles. Allows us to check to see if any battles have occurred.
    __battles_count = 0


    # A static method to print all battles
    # We use a static method because it doesn't require an instance of the class to be called, meaning we do not
    # have to create additional useless objects. Additionally, static methods can be called straight from the class,
    #making it easy to be called throughout the program
    @staticmethod
    def print_all_battles():
        # Check to see if there are no battles
        if Battle.__battles_count == 0:
            return print("A battle has not occurred yet!")

        # Create a list of the data from each battle:
        battle_info = []

        # The battle number, and the name, owner, and kind of the two pokemon. This information is gathered
        # using a loop that iterates through __all_battles, creating a tuple that can easily be passed into the
        # table_print function
        for battle in Battle.__all_battles:
            poke_combatant0 = battle.get_combatant(0)
            poke_combatant1 = battle.get_combatant(1)

            battle_info.append((battle.get_battle_num(),
                                poke_combatant0.get_name(),
                                poke_combatant0.get_owner(),
                                poke_combatant0.get_kind(),
                                poke_combatant1.get_name(),
                                poke_combatant1.get_owner(),
                                poke_combatant1.get_kind(),
                                battle.get_result()))
                      
        # Table print it (headers, data, widths); allows for the user to view battle data in
        # a cohesive manner. Table_print will display all the data gathered in the loop above.
        return(table_print(("Battle #", "Pokemon 1", "P1 Owner", "P1 Kind",
                    "Pokemon 2", "P2 Owner", "P2 Kind", "Final Result"),
                    battle_info, (15, 15, 15, 15, 15, 15, 15, 15)))

    # Initialize a battle object that takes in 2 pokemon objects
    def __init__(self, pokemon1, pokemon2):
        # Track both pokemon in a list
        # Allows for me to easily access the information regarding whichever Pokemon are
        # engaged in battle.
        self.poke_battle = [pokemon1, pokemon2]

        # Create a variable that holds the result of the battle (initially set to say battle has not happened yet)
        self.outcome = "These pokemon have not fought"

        # Create a variable to get battle number (using class attribute for total amount of battles)
        self.count_battle = Battle.__battles_count

        # Update the class attribute integer and list
        Battle.__all_battles.append(self)
        Battle.__battles_count += 1
       

    # Create to-string method (use this when you do print(battle_object)
    # Includes the battle's number, names, and result prior to the actual battle
    # This helps the user know that the Pokemon numbers they entered represents the Pokemon they want to see fight
    # I added error handling in the event that the user inputs the number of a Pokemon that does not exist
    # It will prompt the user to input a number from the table. I chose to explicitly mention
    # AttributeErrors because that is what occurs if you input a number that isn't from the table
    def __str__(self):
        try:
            return f"\nBattle Number: {self.get_battle_num()}\n" \
                   f"{self.poke_battle[0].get_name()} vs {self.poke_battle[1].get_name()}\n" \
                   f"Result: {self.get_result()}\n"
        except AttributeError:
            return "The number you entered doesn't exist; make sure you are using the Pokemon in the list!"


    # Starts the battle
    def start_battle(self):

        # I created this function to add lines to properly divide the contents of the battle
        # section so that it is easier for the users and myself to read. The reason why I created
        # a function is because I need to print these lines multiple times throughout this function.
        def line_print(length):
            for _ in range(length):
                print('-', end='')

        # Create convenience variables for the two combatants
        poke_combatant0 = self.get_combatant(0)
        poke_combatant1 = self.get_combatant(1)

        # Let the user know that two pokemon have appeared and their names
        print(poke_combatant0.get_kind(), 'and', poke_combatant1.get_kind(), 'have appeared!')

        if (poke_combatant0.get_owner() == "None" and poke_combatant1.get_owner() == "None"):
            # If neither pokemon are owned say two 'wild' pokemon are battling
            print("There are two wild Pokemon battling!")
        elif poke_combatant0.get_owner() == 'None':
            # If only one pokemon is owned let the user know that the owned pokemon was attacked by a 'wild' pokemon.
            print(f"{poke_combatant1.get_owner()}'s {poke_combatant1.get_name()} is getting attacked by a wild Pokemon!")
        elif poke_combatant1.get_owner() == 'None':
            # If only one pokemon is owned let the user know that the owned pokemon was attacked by a 'wild' pokemon.
            print(f"{poke_combatant0.get_owner()}'s {poke_combatant0.get_name()} is getting attacked by a wild Pokemon!")
        else:
            # If both pokemon are owned, say the name of each pokemon's owner and let the user know that the pokemon are battling.
            print(f"{poke_combatant0.get_owner()}'s {poke_combatant0.get_name()} is getting attacked by {poke_combatant1.get_owner()}'s {poke_combatant1.get_name()}!")

        # Print lines to seperate the introductory section from the rest of the battle
        line_print(45)

        # Start the battle with round 0
        count_round = 0

        # Get both Pokemon's HP so that both Pokemon are at full health prior to the beginning of the battle
        # We'll also heal both pokemon back to their starting values
        # Even if one of the Pokemon were engaged in a prior battle, these lines of code ensure that their health
        # is fully restored for their next battle.
        poke_health0 = poke_combatant0.get_hp()
        poke_health1 = poke_combatant1.get_hp()
        
        # Have the pokemon battle!
        # This continues as long as both pokemon have more than 0 hp
        while poke_health0 > 0 and poke_health1 > 0:
            # Have each pokemon randomly choose a value between 1-3 to represent their attack
            poke_attack0 = random.randint(0, 3)
            poke_attack1 = random.randint(0, 3)
            

            # BONUS Solution
            # Try to change damage based on the type of pokemon.
            # Divide the 18 types of pokemon in 4 different groups that do different amounts of random damage
            
            # Show the Round number and the name, kind, and HP of each pokemon
            print(f"\nRound {count_round}")
            print(f"{poke_combatant0.get_name()} ({poke_combatant0.get_kind()})'s HP: {poke_health0}")
            print(f"{poke_combatant1.get_name()} ({poke_combatant1.get_kind()})'s HP: {poke_health1}\n")
  
            # Pokemon 1 attacks first
            print(f"{poke_combatant1.get_name()} ({poke_combatant1.get_kind()}) is attacking and did {poke_attack1} damage!")
            # Subtract pokemon1's random value from pokemon0's hp
            poke_health0 = poke_health0 - poke_attack1
            # Output status of pokemon0
            print(f"{poke_combatant0.get_name()} ({poke_combatant0.get_kind()})'s new HP is {poke_health0}\n")
                       
            # Pokemon0 attacks next
            print(f"{poke_combatant0.get_name()} ({poke_combatant0.get_kind()}) is attacking and did {poke_attack0} damage!")
            # Subtract pokemon0's random value from pokemon1's hp
            poke_health1 = poke_health1 - poke_attack0
            # Output status of pokemon1
            print(f"{poke_combatant1.get_name()} ({poke_combatant1.get_kind()})'s new HP is {poke_health1}")

            # Did another line print so that my output closely matches what was shown in the instructions.
            line_print(45)
                       
            # This round is now over, return to the top of the loop
            count_round += 1
                       
        # The loop is over - time to find out why!
        # We'll return the winning pokemon or a list of both pokemon if there is a tie using a series of conditionals
        # Additionally we will need to call the "update_result" method so that the outcome of this battle is properly
        # displayed in the "View Battles" segment of the program.
            if poke_health0 <= 0 and poke_health1 <= 0:
                print("\nThis battle has ended in a tie!")
                self.update_result("This battle has ended in a tie!")
            elif poke_health0 <= 0:
                print(f"\n{poke_combatant1.get_name()} ({poke_combatant1.get_kind()}) has defeated {poke_combatant0.get_name()} ({poke_combatant0.get_kind()})")
                self.update_result(f"{poke_combatant1.get_name()} ({poke_combatant1.get_kind()}) has defeated {poke_combatant0.get_name()} ({poke_combatant0.get_kind()})")
            elif poke_health1 <= 0:
                print(f"\n{poke_combatant0.get_name()} ({poke_combatant0.get_kind()}) has defeated {poke_combatant1.get_name()} ({poke_combatant1.get_kind()})")
                self.update_result(f"{poke_combatant0.get_name()} ({poke_combatant0.get_kind()}) has defeated {poke_combatant1.get_name()} ({poke_combatant1.get_kind()})")
                
    # Getters and Setters for the Battle class
    # These will be very useful for print_all_battles and start_battle

    # Update the pokemon battling
    # Takes pokemon1 and pokemon2 parameters and assigns them to poke_battle attribute
    def update_pokemon(self, pokemon1, pokemon2):
        self.poke_battle = [pokemon1, pokemon2]

    # Update result of battle
    # Takes the result parameter and assigns it to the outcome attribute
    def update_result(self, result):
        self.outcome = result

    # Get battle result
    # Simply returns whatever value is stored in the outcome attribute
    def get_result(self):
        return self.outcome

    # Get battle number
    # Returns whatever value is stored in the count_battle attribute
    def get_battle_num(self):
        return self.count_battle

    # Get one of the pokemon objects
    # Takes in the number parameter and returns whatever Pokemon is identified at that specific spot in poke_battle
    def get_combatant(self, number):
        return self.poke_battle[number]

# This function is used to print all of the people in our system
def print_people_list(person_list):
    # Initialize local variables

    # This list is designed to store information about the players
    people_data = []
    # A counter to keep track of the number of players
    number = 0

    # Check to see if there are no people
    if len(person_list) == 0:
        print("No people to list.")
        return

    # Add all the people to our list
    for person in person_list:
        # Appends a tuple storing each player's information to people_data
        # I used a tuple because the three stored values must not be changed
        # Because these values must remain unchanged, I decided to use a tuple
        people_data.append((number, person.get_name(), person.get_email()))
        #update the counter
        number += 1

    # Table print the list
    return(table_print( ("Number", "Name", "Email"), people_data, (10,10,10) ))
 
    
# DO NOT DELETE - creates starting pokemon/people
# and adds people to a list to keep track of people
person_list = create_default()

# Create a user menu
# Make sure you work through the user menu and complete all the missing code
if __name__ == "__main__":
    
    while True:
        # Output a user menu with 8 Menu options
        print("\nWelcome to the Pokemon Battle Program!")
        print("Your options are:")
        print("1 - Add a Pokemon\n2 - See all Pokemon\n3 - Add a Person\n4 - See all People \
              \n5 - Adopt a Pokemon\n6 - Create a Battle\n7 - See all Battles\n8 - Quit")
        user_input = input("Choose an option: ")
        
        # Add a pokemon
        if user_input == "1":
            print("\nAdd a Pokemon\n")

            # Ask the user for info regarding the new Pokemon
            name = input("What is the pokemon's name? ")
            kind = input("What is the pokemon's kind? ")
            pokemon_type = input("What is the pokemon's type? ")

            #Add a pokemon with the above attributes
            new_pokemon = Pokemon(name,kind,pokemon_type)
            

        # See all pokemon
        elif user_input == "2":
            print("\nSee all Pokemon\n")
            #print all pokemon
            Pokemon.print_all_pokemon()

        # Add a person
        elif user_input == "3":
            print("\nAdd a Person\n")

            # Get person's name/email
            new_name = input("What is the person's name? ")
            new_email = input("What is the person's email? ")

            # Create person object and add to person list
            new_person = Person(new_name, new_email)
            person_list.append(new_person)
                       

            # Let user know person has been added
            print(f"{new_name} has joined the game!")
            

        # See all people
        elif user_input == "4":
            print("\nSee all People\n")
            #print all the people
            print_people_list(person_list)

            
        #Adopt a pokemon
        elif user_input == "5":
            print("\nAdopt a Pokemon\n")

            # Show the available people to adopt
            print_people_list(person_list)

            try:
                # Identify and select the player that is adopting the Pokemon
                person_num = int(input("Enter the number of the Person adopting: "))
            except:
                # Handle errors in the event that the user inputs anything that isn't an integer
                print("Please select a valid number!")
                continue

            # Is the person number valid?
            if (int(person_num) < 0 or int(person_num) > len(person_list)):
                print("This person doesn't exist")
                continue


            # Are there pokemon to be adopted?

            # The creation of this list is explained in the Pokemon file
            Pokemon.print_non_owned_pokemon()

            # Flag is used to check to see if there exists unadopted Pokemon
            # The idea to use flags and my understanding of them comes from
            # https://www.geeksforgeeks.org/use-of-flag-in-programming/
            # False is set as the default, and it will remain false unless turned true
            no_owned_flag = False

            # This loop goes through all the Pokemon in the list to check to see if any of the Pokemon
            # Do not have an owner.
            for pokemon in Pokemon._Pokemon__all_pokemon_list:
                if pokemon._Pokemon__person is None:
                    # If even one Pokemon has no owner, then the flag is changed to True
                    no_owned_flag = True

            # Conditional to handle instance where flag remains false
            if no_owned_flag is False:
                print("Sorry, all Pokemon have been adopted!")
                continue

            # Is the pokemon number a number?
            # Error handling in the event that user inputs anything that isn't an integer
            try:
                adoption_number = int(input('Number of the Pokemon you want to adopt: '))
            except:
                print('Not a valid number.')
                continue
            
            # Check to see if the number is valid.
            if adoption_number < 0 or adoption_number > len(Pokemon._Pokemon__all_pokemon_list):
                print('This Pokemon does not exist')
                continue
            
            # Check to see if the pokemon is un-owned
            pokemon_adoption = Pokemon.find_pokemon(adoption_number)
            if not (pokemon_adoption.get_owner() == 'None'):
                print("This Pokemon has already been adopted")
                continue
            
            # If these are true, adopt!
            pokemon_adoption.set_owner(person_list[person_num])
            print(f'{pokemon_adoption.get_owner()} has adopted {pokemon_adoption.get_name()}!')
            
            


        #Create a battle (list all pokemon, ask them to choose 2 pokemon battling)
        elif user_input == "6":
            print("\nCreate a Battle\n")

            # Check to see if there are pokemon
            if Pokemon._Pokemon__total_pokemon == 0:
                print('The Pokemon list is empty; there are no Pokemon :(')
                continue            

            # Try to get two pokemon by name and look them up, then create a Battle
            Pokemon.print_all_pokemon()
            print('Choose the 2 Pokemon you want to see fight!')

            # User selects the Pokemon they want to see fight
            user_fighter1 = int(input('Pokemon 1: '))
            user_fighter2 = int(input('Pokemon 2: '))

            # Find the Pokemon objects based off the input
            poke_fighter1 = Pokemon.find_pokemon(user_fighter1)
            poke_fighter2 = Pokemon.find_pokemon(user_fighter2)

            # Create a Battle object using the selected Pokemon
            battle_time = Battle(poke_fighter1, poke_fighter2)

            # Print information regarding the battle
            (print(str(battle_time)))

            # When the user hits Enter, start the battle
            input("Press Enter to Start the Battle!\n")

            battle_time.start_battle()

        # See all battles, print out battle data
        elif user_input == "7":
            print("\nSee all Battles\n")
            Battle.print_all_battles()            
            
        # End Program
        elif user_input == "8":
            print("\nGoodbye!\n")
            break

        # Error handling for bad input
        elif user_input != "":
            print("\nPlease enter a valid menu option\n")
        
                    
        
       
        
     

