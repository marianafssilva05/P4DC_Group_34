from type_multiplier import type_multiplier
import random

def calculate_damage(attacker, defender, type_chart):
    # Your code goes here
    if attacker["attack"] >= attacker["sp_atk"]:
        damage = ((42 * 60 * attacker["attack"] / defender["defense"]) / 50) + 2
    else:
        damage = ((42 * 60 * attacker["sp_atk"] / defender["sp_def"]) / 50) + 2

    multiplier = type_multiplier(attacker["types"], defender["types"], type_chart) * random.uniform(0.85, 1)
    damage = damage if damage > 1 else 1
    
    return round(damage, 2), round(multiplier, 2)
