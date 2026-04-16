class Pokemon:
    def __init__(self, name, p_type, health):
        """
        The __init__ method is the 'constructor.' 
        It sets up the initial attributes of your Pokemon.
        """
        self.name = name
        self.p_type = p_type
        self.health = health
        self.max_health = health

    def attack(self, other_pokemon, damage):
        """A simple method to simulate a battle."""
        print(f"{self.name} attacks {other_pokemon.name}!")
        other_pokemon.health -= damage
        
        if other_pokemon.health < 0:
            other_pokemon.health = 0
            
        print(f"{other_pokemon.name} has {other_pokemon.health} HP left.")

    def heal(self):
        """Restores health to the original maximum."""
        self.health = self.max_health
        print(f"{self.name} was fully healed!")

# --- Creating instances (Objects) ---

# We create a specific Pokemon named 'Pikachu'
pikachu = Pokemon("Pikachu", "Electric", 100)

# We create another specific Pokemon named 'Squirtle'
squirtle = Pokemon("Squirtle", "Water", 120)

# --- Using the class methods ---

print(f"A wild {pikachu.name} appeared!")
pikachu.attack(squirtle, 30)