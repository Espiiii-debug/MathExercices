from math import *
from random import randint

# Retourne True si la valeur minimun et inferieur a la valeur maximum
def valueOfMinMaxCorrect(min, max) :
    return (min < max)

# Renvoi un nombre aléatoire en fonction du minimum et du maximum
def pickRandomNumber(min, max) :
    randomNumber = randint(min, max)
    return randomNumber

# Additionne 3 nombres aléatoires
def calculNombre(min, max) :
    a = 0
    for i in range (3) :
        a = a + pickRandomNumber(min, max)
    return a

# Répete le l'opération calculNombre() un nombre de fois defini par l'utilisateur et stock chaque résultat dans une liste.
def getNumberByLoop(loopNumber, min, max) :
    result = []
    for i in range (loopNumber) :
        result.append(calculNombre(min, max))
    
        
    return result

# Compte le nombre de fois qu'apparait un nombre dans une liste
def checkHowManyNumberRepeatInTheList(numberSearch, numberList) :
    return numberList.count(numberSearch)

# Fonction principale
def main() :

    while(True):

        # Initialisation du nombre d'itération à réaliser
        a = int(input("Bonjour, entrez le nombre d'iteration que vous voulez réaliser : "))

        # Vérification que la variable donné soit positive
        if((a > 0)) :
            break
        print("Le nombre saisie doit-être positif !")

    
    while(True):

        # Initialisation du nombre nombre à compter dans la liste
        b = int(input("Quel nombre cherchez vous la fréquence d'apparition ? nombre : "))
        
        # Vérification que la variable donné soit positive
        if((b >= 0)):
            break
        print("Le nombre saisie doit-être positif ou null !")
    
    
    while(True):

        # Initialisation du nombre minimu pouvant être tiré
        c = int(input("Entrez le nombre minimum pouvant être tiré : "))
        
        # Initialisation du nombre maximum pouvant être tiré
        s = int(input("Entrez le nombre maximum pouvant être tiré : "))
        
        # Vérification que le maximum soit superieur au minimum ou minimum + ou = à 0
        if((valueOfMinMaxCorrect(c, s)) or min < 0):
            break
        print("Le nombre saisie doit-être positif et le chiffre minimum positif ou null !")
    
    listNumber = getNumberByLoop(a, c, s)
    
    nombreDappartion = checkHowManyNumberRepeatInTheList(b, listNumber)
    
    print("Le chiffre " + str(b) + " apparait " + str(nombreDappartion) + " fois")

# Invoquation de la fonction main()
main()
    
