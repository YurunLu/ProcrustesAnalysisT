import numpy as np
import pandas as pd
from scipy.linalg import svd
from scipy.spatial import procrustes

# Load the PCA data
file_path = './PCA.data.txt'
data = pd.read_csv(file_path, sep="\t")

# Extract X and Y matrices (latitude/longitude and PC1/PC2)
X = data[['pc1', 'pc2']].values
Y = data[['latitude', 'longitude']].values
N = 10000
def procrustes_statistic(X, Y):
    Xc = X - np.mean(X, axis=0)
    Yc = Y - np.mean(Y, axis=0)
    U, S, Vt = np.linalg.svd(np.dot(Yc.T,Xc), full_matrices=False)
    R = Vt.T @ U.T
    rotation_angle_rad = np.arctan2(R[1, 0], R[0, 0])
    rotation_angle_deg = np.degrees(rotation_angle_rad)
    tr_S = np.sum(S)
    D = 1-(tr_S)**2/(np.trace(np.dot(Yc.T,Yc))*np.trace(np.dot(Xc.T,Xc)))
    t_statistic = np.sqrt(1 - D)
    return t_statistic,rotation_angle_deg


# Compute t0 and D for the given X and Y
t0,theta = procrustes_statistic(X, Y)
print('t =',t0,'theta =',theta)

# Permutation test to calculate p-value
def permutation_test(X, Y, num_permutations=N):
    t_original= procrustes_statistic(X, Y)[0]
    n = X.shape[0]
    t_perm = []

    for _ in range(num_permutations):
        permuted_Y = Y[np.random.permutation(n), :]
        t_perm.append(procrustes_statistic(X, permuted_Y)[0])

    # Calculate p-value
    t_perm = np.array(t_perm)
    p_value = np.sum(t_perm >= t_original) / num_permutations
    return t_original,p_value,t_perm

# permutation test
t_original,p_value,t_perm = permutation_test(X, Y)

import matplotlib.pyplot as plt
plt.figure(figsize=(3,3))
#print(len(t_perm))
plt.hist(t_perm, bins=40, color='white', alpha=0.7, edgecolor='black',lw=1,range=(0,0.5))
plt.axvline(x=t_original, color='red', linestyle='--', label=f'Observed t0 = {t_original:.4f}')
#plt.title('Distribution of t-values from Permutations')
plt.xlabel('t-value')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
plt.savefig('./Distribution_t0_Permutations.pdf')
print('p=',p_value,f'After {N} permutations')
