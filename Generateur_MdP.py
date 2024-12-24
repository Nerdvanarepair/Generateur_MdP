# -*-coding:utf-8-*  #-On Oublie pas ça si il y a des accents dans le texte (linux)
from Melangeur import * #-On Apporte les packages dont on a besoin (ici et au dessous ils sont perso)
from exit import *

#Ici il y a le coeur du programme, cad :

#-Les Valeurs dont on va se servir
Caracteres = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"\
"P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g"\
"h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"\
"z","&~","\"","#","'","{","(","[","-","|","_","@",")","]","°","^","¨"\
"$","£","%","*","!","/","<",">","1","2","3","4","5","6","7","8","9","0"
i, Nmbr_Cara, MdP = int(0), 1, ""

while True: #-La premiere boucle qui englobe tout
    while True: #La deuxieme boucle dans laquelle il y a :
        Nmbr_Cara = input("Combien de caractères veux-tu ? ") #La question à l'user
        try: #La boucle pour tester si un nombre ou un chiffre a bien été entré
            Nmbr_Cara = int(Nmbr_Cara) #La ligne de test
            break #Si elle est valide on arrete et on continue
        except: #Sinon
            print(""" Un Nombre ou un chiffre wesh, t'es con.ne ?!""") #On indique à l'user qu'il a fait de la merde et on recommence

    MdP = Tirage(Caracteres, i, Nmbr_Cara, MdP) #-On attache la valeur MdP au résultat de la fonction Tirage (on oublie pas les veleurs)
    print(MdP) #-On affiche le mot de passe (pour pouvoir le copier sinon ça sert à rien tout le reste)
    finir() #-On termine la boucle en appelant la fonction finir (sinon ça fait une boucle infini trou de bal)
