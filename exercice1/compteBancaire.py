class CompteBancaire:
     #constructeur
     def __init__(self, titulaire, solde=0):
          self._titulaire = titulaire
          self.__solde = solde
     #la methode deposer :ajouter un montant au solde
     def deposer(self, montant):
          if montant > 0:
               self.__solde += montant
               print(f"Déposé: {montant}. Nouveau solde: {self.__solde}")
          else:
               print("Le montant à déposer doit être positif.")
     #la methode retirer : soustraire un montant du solde
     def retirer(self, montant):
          if 0 < montant <= self.__solde:
               self.__solde -= montant
               print(f"Retiré: {montant}. Nouveau solde: {self.__solde}")
          else:
               print("Montant de retrait invalide ou solde insuffisant.")
     #la methode afficher : afficher le solde du compte
     def afficher(self):
          print(f"Titulaire: {self._titulaire}, Solde: {self.__solde}")
     # recuperer le solde du compte
     def get_solde(self):
          return self.__solde
     @property
     def solde(self):
          return self.__solde
     def __str__(self):
          return f"CompteBancaire(Titulaire: {self._titulaire}, Solde: {self.__solde})"



#test 

if __name__=="__main__":
     compte1 = CompteBancaire("Assiya", 1000)
     compte1.afficher()
     compte1.deposer(500)
     
     compte1.retirer(200)
     compte1.retirer(2000)  
     compte1.deposer(-100)

     
     print(compte1)  