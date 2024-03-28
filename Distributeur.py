rep = input("Voulez-vous acheter une autre boisson o/n ?")
rep = "o"
while rep == "o":
    stock_soda = 3
    stock_orangeade = 5
    stock_eau = 0

    print("Veuillez sélectionner une boisson :")
    print("1. Soda")
    print("2. Orangeade")
    print("3. Eau")
    choix = int(input())

    if choix == 1:
        if stock_soda > 0:
            print("A votre santé, voici votre Soda!")
            stock_soda -= 1
        else:
            print("Sold out! Faites un autre choix...")
    elif choix == 2:
        if stock_orangeade > 0:
            print("A votre santé, voici votre orangeade!")
            stock_orangeade -= 1
        else:
            print("Sold out! Faites un autre choix...")
    elif choix == 3:
        if stock_eau > 0:
            print("A votre santé, voici votre eau!")
            stock_eau -= 1
        else:
            print("Sold out! Faites un autre choix...")
    else:
        print("Erreur, boisson non-disponible...")
    rep = input("Voulez-vous acheter une autre boisson o/n ?")