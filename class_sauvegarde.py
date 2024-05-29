import csv
from class_solde import Solde
from class_pieces import Pieces

#/!\ CLASSE ISSUE DE SOLDE ET DE PIECES

class Sauvegarde(Solde, Pieces):
    """
    Classe sauvegarde qui permet d'enregistrer dans un fichier csv, le solde restant et le nombre de pièces récoltées par le joueur à la fin du jeu
    """
    __slots__ = ['nom_fichier']
    
    def __init__(self, nom_fichier):
        super().__init__()
        self.nom_fichier = nom_fichier
        self.solde =Solde.solde_restant
        self.pieces= Pieces.compteur
        
    def creation_fichier(self):
        """
        créer un fichier csv avec la première ligne vide 
        """
        with open(nom_fichier,'w') as fichier_sauvegarde:
            writer = csv.writer(fichier_sauvegarde)
            writer.writerow([])

#à lancer dans un autre fichier associé à la fin du jeu
    def enregistrement_sauvegarde(self):
        """
        enregistre le score et le nombre de pièces dans le fichier
        """
        with open(nom_fichier,'w') as fichier_sauvegarde:
            writer = csv.writer(fichier_sauvegarde)
            writer.writerow([self.solde, self.pieces])
        
        
        

nom_fichier= 'sauvegarde.tkt'
