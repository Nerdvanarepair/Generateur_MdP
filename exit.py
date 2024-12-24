# -*-coding:utf-8-*  #-Encore Une fois quand il y a du texte...

def finir(): #-On Defini le nom de la fonction (pas besoin d'argument il ferme le programme)
    while True: #-Boucle infini ici aussi
        user_input = input("Voulez-vous continuer ? oui/non : ")
        if user_input.lower() in ["oui", "o"]:  #-On reduit ici la chaine saisi par l'user et on le compar à oui ou o simple
            print("""Quand il y en plus, il y en encore !""")
            break  #-On arrete le programme et on repart sur le code principal
        elif user_input.lower() in ["non", "n"]:
            print("""Bon Bah j'me ramasse... :'(""")
            exit() #-Ferme le programme
        else:
            print("""C'est pas compliqué, OUI ou NON, même un.e flemmard.e j'lui ai mis o ou n..""") #-Pour Les GROS.SSES CONS.NNES
