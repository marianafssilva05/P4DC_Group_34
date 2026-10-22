import pandas as pd

def friends_per_gen(df):
    # Select friendship pairs with generation and legendary status for both sides
    pairs = df[["Generation_friend1", "Legendary_friend1", "Generation_friend2","Legendary_friend2"]].copy()

    # Split into two perspectives so every pokemon's connections are counted for their generation
    pair_1 = pairs[["Generation_friend1","Legendary_friend2"]].rename(
        columns={
            "Generation_friend1": "Generation",
            "Legendary_friend2": "Legendary"
            }
    )

    pair_2 = pairs[["Generation_friend2","Legendary_friend1"]].rename(
        columns={
            "Generation_friend2": "Generation",
            "Legendary_friend1": "Legendary"
        }
    )

    combined = pd.concat([pair_1,pair_2]) # Combine both parts together

    # Combine both parts together
    result = combined.groupby(["Generation","Legendary"]).size().unstack(fill_value=0)

    return result
