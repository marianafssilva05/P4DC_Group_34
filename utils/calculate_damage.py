from type_multiplier import type_multiplier
import random

def calculate_damage(attacker, defender, type_chart):
    # Confirming which attack and deffense to use
    if attacker["attack"] >= attacker["sp_atk"]:
        damage = ((42 * 60 * attacker["attack"] / defender["defense"]) / 50) + 2
    else:
        damage = ((42 * 60 * attacker["sp_atk"] / defender["sp_def"]) / 50) + 2

    multiplier = type_multiplier(attacker["types"], defender["types"], type_chart)
    damage *= multiplier * random.uniform(0.85, 1)
    damage = max(int(damage), 1)
    
    return damage, multiplier
