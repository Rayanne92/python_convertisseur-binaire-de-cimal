binaire = (input("Écrire en binaire !")) # Permet de saisir une valeur
decimal = 0
puissance = len(binaire) - 1

for result in binaire:
    if result == "1":
        decimal += 2**puissance
    puissance -= 1

print(binaire, "en décimal correspond à", decimal) # Affiche le résultat de la conversion