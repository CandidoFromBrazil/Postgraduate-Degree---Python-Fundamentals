class MarioCharacter:
    def __init__(self, name, outfit_color):
        # Attributes (Data)
        self.name = name
        self.outfit_color = outfit_color
        self.is_big = False
        self.lives = 3

    # Methods (Behaviors)
    def jump(self):
        print(f"{self.name} jumps into the air! Wahoo!")

    def eat_mushroom(self):
        self.is_big = True
        print(f"{self.name} ate a mushroom and grew bigger!")

    def show_stats(self):
        status = "Super" if self.is_big else "Small"
        print(f"--- {self.name} Stats ---")
        print(f"Status: {status}")
        print(f"Lives: {self.lives}")
        print(f"Outfit: {self.outfit_color}")

# --- Using the Class ---

# 1. Create an "instance" (Object) of the class
hero = MarioCharacter("Mario", "Red")

# 2. Access attributes and call methods
hero.show_stats()
hero.jump()
hero.eat_mushroom()
hero.show_stats()
