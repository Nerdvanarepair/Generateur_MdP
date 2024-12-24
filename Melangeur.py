from random import * #-On Appel les packages pres fait de py dont on a besoin

def Tirage(Caracteres, i, Nmbr_Cara, Mdp): #-On Definit le nom de la fonction en appelant les valeurs dont elle aura besoin
    Alea = "" #-On Vient créer la valeur qui va contenir le MdP
    while i < Nmbr_Cara: #-On fait une boucle en indiquant que le nombre de cara du MdP ne doit pas dépasser i
        Alea += choice(Caracteres) #-On ajoute à Alea les Caras "choisi" par la fonction py un a un sans les ecraser
        i += 1 #-On oublie pas d'ajouter à i (sinon il y a une boucle infini)
        
    return Alea #-Pour Finir on retourne la valeur alea dans le programme principal
