
"""
age = 23
nom = "romeo"
print(age, nom)
print(" i an strong in agent AI")
"""


"""
n = -7 
if n <= 0:
    print("Negative")
elif n >= 0:
    print("Positive")
else:
    print("Zero")

"""


"""
total = 0
for i in range(1, 101):
    total = total + i
print(total)

"""

"""
stock = {"pomme": 3, "banane": 5, "cerise": 2}
for key in stock.items():
    print(key)

"""

"""
Phrase = "Le chat et le chien"


def count_world(nombre):
    mots = nombre.lower().split()
    dict = {}
    for mot in mots:
        dict[mot] = dict.get(mot, 0) + 1
    return dict
print(count_world(Phrase))

"""

"""
def compteur(texte):
    mots = texte.lower().split()
    dico = {}
    for mot in mots:
        if mot in dico:
            dico[mot] = dico[mot] + 1
        else:
            dico[mot] = 1
    return dico
print(compteur(Phrase))

"""

"""

def divis(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Zero diviser par zero Impossible"
print(divis(10, 0))
print(divis(10, 2))
"""

"""
nombre = [1,2,3,4,5,6,7,8,9,10]
carre = [n ** 2 for n in nombre if n % 2 == 0]
print("Carrer de n = ", carre)
"""

class compte_Bancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial
        self.historique = []
        pass
    def deposit(self, montant):
        self.solde += montant
        self.historique.append(f"Depot de {montant}")
        pass
    def retraire(self, montant):
        if montant > self.solde:
            print("Montant insuffisant")
        else:
            self.solde -= montant
        self.historique.append(f"Retraire de {montant}")
        pass
    def affiche(self):
        print("sold :", self.solde)
        pass
    def Historie(self):
        print("___HISTORIQUE DES OPERAATION___")
        for ope in self.historique:
            print("-", ope)


compte = compte_Bancaire(0)
compte.deposit(500)
compte.retraire(30)
compte.affiche()
compte.retraire(46)
compte.Historie()