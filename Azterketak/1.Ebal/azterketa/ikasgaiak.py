ikasgaiak = ["Esukera","Historia","Filosofia","Gaztelania","Soinketa","fisika","Geografia"]
def ikasgaia(gaia):
    for i in range(len(gaia)):
        print(f"{i+1}.{gaia[i]}")

print(ikasgaia(ikasgaiak))