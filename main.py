import time

# Fonctions
def slow_writing(txt, speed=0.05):
    for c in txt:
        print(c, end="")
        time.sleep(speed)
    print()

# Class
class Pokemon:

    def __init__(self, name, colour, element, size, character, smell, life_points, hook):
        self.name = name
        self.colour = colour
        self.element = element
        self.size = size
        self.character = character
        self.smell = smell
        self.life_points = life_points
        self.hook = hook

    def __str__(self):
        return f"{self.hook}, je suis {self.name} je suis {self.size} {self.colour} {self.character} {self.smell}.\nJe suis un pokémon {self.element} et j'ai {self.life_points} points de vie."

# Choix des pokémons
# Choix pokémon 1

slow_writing("Bienvenue dans le PokéCenter !")
time.sleep(1)

choosing_pokemon=True

while choosing_pokemon:
    valid_answer=False
    slow_writing("Choisis un chiffre entre 1 et 3. Et pas un autre. Attention.")

    number = input()

    if number == "1":
        pokemon1 = Pokemon("Salamouche","orange","feu","petit","têtu","puant",100,"Grou grou")
        slow_writing(str(pokemon1))

    elif number == "2":
        pokemon1 = Pokemon("Boulbizure", "vert", "terre", "petit", "gentil", "odorant", 100, "Poum poum")
        slow_writing(str(pokemon1))


    elif number == "3":
        pokemon1 = Pokemon("Cartapouce", "bleu", "eau", "petit", "loyal", "rafraichissant", 100, "Glou glou")
        slow_writing(str(pokemon1))


    else:
        pokemon1 = Pokemon("Bartabé", "pourpre", "vase", "immense", "fainéant", "nauséabond", 2, "Petit malin ! Mouhahahaha ! Ploc ploc")
        slow_writing(str(pokemon1))

    time.sleep(1)
    slow_writing("\nVeux-tu me garder, ou m'échanger ? (pitié, garde moi s'il te plait)")
    slow_writing("Tu me gardes : tape JTM \nTu m'échanges : tape OUSTE")

    while not valid_answer:
        answer=input()

        if answer=="JTM":
            choosing_pokemon=False
            valid_answer=True
            slow_writing("Merci ! Je vais rester avec toi toute ma vie <3")
        elif answer=="OUSTE":
            valid_answer = True
            slow_writing("Tu es horrible, adieu sac à patates pourries.")
        else:
            slow_writing("Tu parles français ou pas ? Allo ? JTM ou OUSTE")


# Choix pokémon 2
