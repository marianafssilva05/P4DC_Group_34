import numpy as np

def imputer(df, dists, missing, k=3, col="Legendary"):
    df = df.copy()
    
    known_values = df.loc[~missing, col].to_numpy()
    
    # Get indices of the k smallest distances for each missing row
    k_nearest_idx = np.argpartition(dists, k, axis=1)[:, :k]
    nearest_labels = known_values[k_nearest_idx]
    
    # Majority vote: True if at least half of the k neighbours are True
    imputed_values = np.sum(nearest_labels == True, axis=1) >= (k / 2)
    
    df.loc[missing, col] = imputed_values
    return df
