from random import *

def Tirage(Caracteres, i, Nmbr_Cara, Mdp):
    Alea_Liste = []
    while i < Nmbr_Cara:
        Alea_Liste.append(choice(Caracteres))
        i += 1
    
    Alea = "".join(Alea_Liste)
    return Alea
