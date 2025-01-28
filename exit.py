# -*-coding:utf-8-*

def finir():
    while True:
        user_input = input("Voulez-vous continuer ? oui/non : ")
        if user_input.lower() in ["oui", "o"]:
            print("""Quand il y en plus, il y en encore !""")
            break
        elif user_input.lower() in ["non", "n"]:
            print("""Bon Bah j'me ramasse... :'(""")
            exit()
        else:
            print("""C'est pas compliqué, OUI ou NON, même un.e flemmard.e j'lui ai mis o ou n..""")
