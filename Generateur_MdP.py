# -*-coding:utf-8-*
from Melangeur import *
from exit import *

Caracteres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","&","~","\"","#","'","{","(","[","-","|","_","@",")","]","°","^","¨","$","£","%","*","!","/","<",">","1","2","3","4","5","6","7","8","9","0"]
i, Nmbr_Cara, MdP = int(0), 1, ""

while True:
    while True:
        Nmbr_Cara = input("Combien de caractères veux-tu ? ")
        try:
            Nmbr_Cara = int(Nmbr_Cara)
            break
        except:
            print(""" Un Nombre ou un chiffre !!""")

    MdP = Tirage(Caracteres, i, Nmbr_Cara, MdP)
    print(MdP)
    finir()
