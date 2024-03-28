LIMITE_MAX = 3

stocks = [3, 0, 2]
noms = ["Eau", "Soda", "Orangeade"]

totalStock = sum(stocks)

choix = 0

while totalStock > 0 and choix != 4:
    print("Choisissez une boisson.")
    for i in range(LIMITE_MAX):
        print(noms[i] + " : " + str(i+1))
    print("FINIR : 4")
    choix = int(input())

    if choix != 4:
        if stocks[choix-1] > 0:
            print("Voici votre " + noms[choix-1] + " , santé!")
            stocks[choix-1] -= 1
        else:
            print("Plus de "+ noms[choix-1])

    totalStock = sum(stocks)

print("Merci d'utiliser distributeur 3000!")
