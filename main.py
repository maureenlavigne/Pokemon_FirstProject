import time
def slow_writing(txt, speed=0.05):
    for c in txt:
        print(c, end="")
        time.sleep(speed)
    print()

slow_writing("Bienvenue dans le PokéCenter !")
time.sleep(1)

selected_pokemon=False
valid_answer=False
while not selected_pokemon:
    slow_writing("Choisis un chiffre entre 1 et 3. Et pas un autre. Attention.")

    number=input()

    if number==1:
        name="Salamouche"
        colour="orange"
        element="feu"
        size="petit"
        character="têtu"
        smell="puant"
        life_points=100
        slow_writing(f"Grou grou, je suis {name} je suis {size} {colour} {character} {smell}.\n"
                    f"Je suis un pokémon {element} et j'ai {life_points} points de vie.")

    elif number==2:
        name="Boulbizure"
        colour="vert"
        element="terre"
        size="petit"
        character="gentil"
        smell="odorant"
        life_points=100
        slow_writing(f"Poum poum, je suis {name} je suis {size} {colour} {character} {smell}.\n"
                    f"Je suis un pokémon {element} et j'ai {life_points} points de vie.")

    elif number==3:
        name="Cartapouce"
        colour="bleu"
        element="eau"
        size="petit"
        character="loyal"
        smell="rafraichissant"
        life_points=100
        slow_writing(f"Glou glou, je suis {name} je suis {size} {colour} {character} {smell}.\n"
                    f"Je suis un pokémon {element} et j'ai {life_points} points de vie.")


    else:
        name="Bartabé"
        colour="pourpre"
        element="vase"
        size="immense"
        character="fainéant"
        smell="nauséabond"
        life_points=2
        slow_writing(f"Petit malin ! Mouhahahaha ! Ploc ploc, je suis {name} je suis {size} {colour} {character} {smell}.\n"
                    f"Je suis un pokémon {element} et j'ai {life_points} points de vie.")

    time.sleep(1)
    slow_writing("\nVeux-tu me garder, ou m'échanger ? (pitié, garde moi s'il te plait)")
    slow_writing("Tu me gardes : tape JTM. \nTu m'échanges : tape OUSTE.")

    while not valid_answer:
        answer=input()

        if answer=="JTM":
            selected_pokemon=True
            valid_answer=True
            slow_writing("Merci ! Je vais rester avec toi toute ma vie <3")
        elif answer!="OUSTE":
            valid_answer = True
            slow_writing("Tu es horrible, adieu sac à patates pourries.")
        else:
            slow_writing("Tu parles français ou pas ? Allo ? JTM ou OUSTE.")

