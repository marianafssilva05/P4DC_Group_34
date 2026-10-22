
def type_multiplier(attacker_types, defender_types, type_chart):
    # Your code goes here
    multiplier = 1
    for atk_t in attacker_types:
        for def_t in defender_types:
            multiplier *= type_chart.get(atk_t, {}).get(def_t, 1)
    return multiplier
