import csv
import os

class Sauvegardes:
    def __init__(self):        
        self.nom_fichier = 'sauvegardes.csv'
        
        #Vérifie si le fichier existe
        if not os.path.isfile(self.nom_fichier):
            # Crée le fichier et écrit les en-têtes
            with open(self.nom_fichier, mode='w', newline='') as fichier_csv:
                writer = csv.writer(fichier_csv)
                writer.writerow(['Cookies Recoltees', 'Solde Restant'])
        
        self.getRecords()

    def save(self, pieces_recoltees, solde_restant):
        # Ouvre le fichier en mode ajout ('a')
        with open(self.nom_fichier, mode='a', newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            
            # Ajoute les nouvelles données
            writer.writerow([pieces_recoltees, solde_restant])
    
    def getRecords(self):
        #Ouvre le fichier en mode lecture
        with open(self.nom_fichier, mode='r', newline='') as fichier_csv:
            reader = csv.DictReader(fichier_csv)
            
            max_pieces_recoltees = 0
            max_solde_restant = 0
            
            for row in reader:
                pieces_recoltees = int(row['Cookies Recoltees'])
                solde_restant = int(row['Solde Restant'])
                
                if pieces_recoltees > max_pieces_recoltees:
                    max_pieces_recoltees = pieces_recoltees
                
                if solde_restant > max_solde_restant:
                    max_solde_restant = solde_restant
            
            self.cookiesRecord, self.soldeRecord = max_pieces_recoltees, max_solde_restant