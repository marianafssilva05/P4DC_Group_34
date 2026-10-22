
def type_multiplier(attacker_types, defender_types, type_chart):
    multiplier = 1
    for atk_t in attacker_types:
        # loops throughout the attackers types and finds the deffender type
        for def_t in defender_types:
            multiplier *= type_chart.get(atk_t, {}).get(def_t, 1)
    return multiplier
