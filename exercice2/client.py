
from exercice1.compteBancaire import CompteBancaire
class Client:
     def __init__(self,identifiant,nom):
          self.identifiant = identifiant
          self.nom = nom
          self.compte=CompteBancaire(self.nom)


     def afficher(self):
          print(f"Client ID: {self.identifiant}, Nom: {self.nom}, Solde du compte: {self.compte.get_solde()}")


#test
if __name__=="__main__":
     client1 = Client(1, "Assiya")
     client1.afficher()
     client1.compte.deposer(1000)
     client1.compte.retirer(200)
     client1.afficher()
