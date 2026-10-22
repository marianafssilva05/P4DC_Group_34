from calculate_damage import calculate_damage

def take_turn(attacker, defender, type_chart):
    damage, mult = calculate_damage(attacker, defender, type_chart)

    defender["hp"] = defender["hp"] - damage

    if defender["hp"] < 0:
        defender["hp"] = 0 

    print(f'{attacker["name"]} attacks {defender["name"]} for {damage} damage')

    if mult > 1:
        print("Super Effective")
    elif 0 < mult < 1:
        print("Not very effective")
    elif mult == 0:
        print("No effect")

    print(f'{defender["name"]}\'s remaining HP {defender["hp"]}')
