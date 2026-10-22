
def get_pokemon(df, name):
    
    row = df[df["Name"] == name].iloc[0]
    
    # Build the list of types, ignoring NaN in Type2
    types = [row["Type1"]]
    if row["Type2"] == row["Type2"] and row["Type2"] is not None:
        types.append(row["Type2"])
        
    return {
        "name": row["Name"],
        "types": types,
        "hp": int(row["HP"]),
        "attack": int(row["Attack"]),
        "defense": int(row["Defense"]),
        "sp_atk": int(row["SpAtk"]),
        "sp_def": int(row["SpDef"]),
        "speed": int(row["Speed"])
    }
