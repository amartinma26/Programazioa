import numpy as np

# Ariketa 5
notak = np.array([3, 5, 8, 4, 9, 6, 7, 2, 10, 5])
print(f"Nota maximoa: {notak.max()}")
print(f"Nota minimoa: {notak.min()}")
print(f"Nota media: {notak.mean()}")
print(f"Nota desviacion estandar: {notak.std()}")

print(notak[notak >= 5])
print(f"{(notak >= 5).sum()} Pertsona gainditu dute")
