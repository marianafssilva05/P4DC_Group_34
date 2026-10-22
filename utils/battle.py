from get_pokemon import get_pokemon
from take_turn import take_turn

def battle(df, name1, name2, type_chart):
    pokemon_1 = get_pokemon(df, name1)
    pokemon_2 = get_pokemon(df, name2)

    if pokemon_1["speed"] >= pokemon_2["speed"]: #determine who attacks first
        attacker = pokemon_1
        defender = pokemon_2
    elif pokemon_1["speed"] < pokemon_2["spreed"]:
        attacker = pokemon_2
        defender = pokemon_1

    while pokemon_1["hp"] > 0 and pokemon_2["hp"] > 0:
        take_turn(attacker, defender, type_chart)

        if defender["hp"] <= 0: # is the defender was hp < 0 it's the end of the battle
            break 

        attacker, defender = defender, attacker # swtich attacker and defender for the next turn

    if pokemon_1["hp"] > 0:
        return pokemon_1
    elif pokemon_2["hp"] < 0:
        return pokemon_2
