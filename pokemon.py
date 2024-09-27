from data_handling import table_print
from person import Person

class Pokemon():

    # Create two class attributes
    # 1. A list to track all pokemon
    __all_pokemon_list = []
    # 2. An integer of the amount of pokemon
    __total_pokemon = 0

    # A static method to print all the pokemon
    @staticmethod
    def print_all_pokemon():
        pokemon_list = []

        # Check to see if there are no pokemon
        if len(Pokemon.__all_pokemon_list) == 0:
            print("No pokemon to present.")
            return 0

        # Create a list of the data from each pokemon:       
        # The pokemon number, the name, kind, type, hp, and owner
        for pokemon in Pokemon.__all_pokemon_list:            
            pokemon_list.append((pokemon.get_num(), pokemon.get_name(), pokemon.get_kind(),
                                 pokemon.get_pokemon_type(), pokemon.get_hp(), pokemon.get_owner()))

        # Table print it (headers, data, widths)
        table_print( ("Number", "Name", "Pokemon", "Type", "HP", "Owner"),
                     pokemon_list,
                     (10, 10, 10, 10, 10, 10) )

        return 1            

    # A static method to print all the non-owned pokemon
    @staticmethod
    def print_non_owned_pokemon():
        pokemon_list_non_owned = []

        # Check to see if there are no pokemon
        if len(Pokemon.__all_pokemon_list) == 0:
            print("No pokemon to present.")
            return 0

        # Check to see if the Pokemon doesn't have an owner
        # Create a list of the data from each pokemon:       
        # The pokemon number, the name, kind, type, hp, and owner
        for pokemon in Pokemon.__all_pokemon_list:
            if pokemon.get_owner() == "None":
                pokemon_list_non_owned.append((pokemon.get_num(), pokemon.get_name(), pokemon.get_kind(),
                                               pokemon.get_pokemon_type(), pokemon.get_hp()))

        #print(pokemon_list_non_owned)

        #Table print it (headers, data, widths)
        table_print( ("Number", "Name", "Pokemon", "Type", "HP"),
                     pokemon_list_non_owned,
                     (10, 10, 10, 10, 10) )
        return 1            
        

    # A static method to find a pokemon object using its number
    # Returns -1 if no pokemon is found
    @staticmethod
    def find_pokemon(number):
        # Iterate through all of the Pokemon list
        for i in range(len(Pokemon.__all_pokemon_list)):
            # Check to see if the number matches the index
            if number == i:
                # Return the matched Pokemon object
                return Pokemon.__all_pokemon_list[i]
        
        return -1
            
        


    # Initalizing a pokemon object
    def __init__(self, name, kind, pokemon_type, person = None):
        self.__name = name
        self.__kind = kind
        self.__pokemon_type = pokemon_type
        self.__person = person

        #BONUS Solution
        #Divide 18 types of Pokemon into 4 groups, give each group a different HP value
        self.__hp = 4
        
        # Use the class attribute for the number
        self.__num = Pokemon.__total_pokemon

        # Update the class attribute integer and list
        Pokemon.__total_pokemon += 1
        Pokemon.__all_pokemon_list.append(self)

    # To-string method
    def __str__(self):
        reply = "---Pokemon---\n"
        reply += "Number: " + str(self.__num) + "\n"
        reply += "Name: " + str(self.__name)+ "\n"
        reply += "Kind: " + str(self.__kind)+ "\n"
        reply += "Type: " + str(self.__pokemon_type)+ "\n"

        if self.get_owner() != "None":
            reply += "Owned by " + str(self.get_owner())+ "\n"
            
        reply += "HP: " + str(self.__hp)+ "\n"
            
        return reply

    # Getters and Setters for the Pokemon class
    
    # Adopting pokemon
    def adopt(self, person):
        self.set_owner(person)

    # Get pokemon num
    def get_num(self):
        return self.__num

    # Get pokemon name
    def get_name(self):
        return self.__name

    # Get pokemon type
    def get_pokemon_type(self):
        return self.__pokemon_type

    # Get pokemon kind
    def get_kind(self):
        return self.__kind

    # Get pokemon owner name
    # Returns 'None' if none
    def get_owner(self):
        if self.__person:
            return (self.__person).get_name()
        else:
            return "None"

    # Get pokemon hp
    def get_hp(self):
        return (self.__hp)

    # Set pokemon name
    def set_name(self, name):
        self.__name = name

    # Set pokemon type
    def set_name(self, pokemon_type):
        self.__pokemon_type = pokemon_type

    # Set kind
    def set_name(self, age):
        self.__age = age
        
    # Set owner
    def set_owner(self, person):
        self.__person = person

    # Set hp
    def set_hp(self, hp):
        self.__hp = hp

    # Remove owner
    def remove_owner(person):
        self.__person = None

# DO NOT DELETE - creates starting pokemon/people
# and adds people to a list to keep track of people
def create_default():

    person_list = []

    person1 = Person("Ash", "ash@gmail.com")
    person2 = Person("Misty", "misty@gmail.com")
    person3 = Person("Brock", "brock@gmail.com")

    person_list.append(person1)
    person_list.append(person2)
    person_list.append(person3)

    pokemon1 = Pokemon("Piky", "Pikachu", "Electric", person = person1)
    pokemon2 = Pokemon("Stary", "Staryu", "Water", person = person2)
    pokemon3 = Pokemon("Ony", "Onix", "Rock", person = person3)
    pokemon4 = Pokemon("Bulby", "Bulbasaur", "Grass", person = None)
    pokemon5 = Pokemon("Charmy", "Charmander", "Fire", person = None)
    pokemon6 = Pokemon("Squirty", "Squirtle", "Water", person = None)
    pokemon7 = Pokemon("Diggy", "Diglett", "Ground", person = None)
    pokemon8 = Pokemon("Sprout", "Bellsprout", "Grass", person = None)
    pokemon9 = Pokemon("Electro", "Electrode", "Electric", person = None)
    pokemon10 = Pokemon("Cu-tie", "Cubone", "Ground", person = None)

    # Instantiate 4 Additional Pokemon from https://www.pokemon.com/us/pokedex
    
    return person_list

# Test code - creates people and pokemon, then outputs them
if __name__ == "__main__":
    
    create_default()
    
    Pokemon.print_all_pokemon()

    # Comment these in for Part 1b
    print(Pokemon.find_pokemon(9))
    print(Pokemon.find_pokemon(100))

    # Comment this in for Part 1c
    Pokemon.print_non_owned_pokemon()
    
