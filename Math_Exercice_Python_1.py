class ProgressBar:
    '''
    Progress bar
    '''
    def __init__ (self, valmax, maxbar, title):
        if valmax == 0:  valmax = 1
        if maxbar > 200: maxbar = 200
        self.valmax = valmax
        self.maxbar = maxbar
        self.title  = title
    
    def update(self, val):
        import sys
        # process
        perc  = round((float(val) / float(self.valmax)) * 100)
        scale = 100.0 / float(self.maxbar)
        bar   = int(perc / scale)
  
        # render 
        out = '\r %20s [%s%s] %3d %%' % (self.title, '=' * bar, ' ' * (self.maxbar - bar), perc)
        sys.stdout.write(out)
        sys.stdout.flush()

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
def calculNombre(min, max, nombreAddition) :
    a = 0
    for i in range (3) :
        a = a + pickRandomNumber(min, max)
    return a

# Répete le l'opération calculNombre() un nombre de fois defini par l'utilisateur et stock chaque résultat dans une liste.
def getNumberByLoop(loopNumber, min, max, nombreAddition) :
    result = []

    Bar = ProgressBar(loopNumber, 60, 'Calcul en cours ...')
    for i in range (loopNumber) :
        result.append(calculNombre(min, max, nombreAddition))
        Bar.update(i)
    
        
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
        
        # Initialisation du nombre fois d'addition de nombre
        nombreAddition = int(input("Entrez le nombre de tirage par iteration : "))

        # Vérification que le maximum soit superieur au minimum ou minimum + ou = à 0
        if((valueOfMinMaxCorrect(c, s)) or (c < 0)):
            break
        print("Le nombre saisie doit-être positif et le chiffre minimum positif ou null !")
    
    listNumber = getNumberByLoop(a, c, s, nombreAddition)
    
    nombreDappartion = checkHowManyNumberRepeatInTheList(b, listNumber)
    
    print("\nLe chiffre " + str(b) + " apparait " + str(nombreDappartion) + " fois")
    

# Invoquation de la fonction main()
main()
    
