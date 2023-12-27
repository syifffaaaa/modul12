import pandas as pd

df = pd.read_csv('Negara.csv')

mean = df.groupby("Benua").mean()[["Luas", "Populasi"]]
std = df.groupby("Benua").std()[["Luas", "Populasi"]]

mean.to_csv("mean.csv")
std.to_csv("std.csv")

print("Berikut Data Mean:")
print(mean)
print("Berikut Data Standard Deviation:")
print(std)
print("File Berhasil Dibuat")
