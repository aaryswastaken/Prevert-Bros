import tkinter as tk

class Solde:
    """
    Classe qui permet le décompte du temps / solde restant au joueur pour terminer le niveau

    Attributs : solde_initial (int)
    """
    __slots__=['solde_initial']
    
    def __init__(self):
        self.solde_initial = 200

    
    def decompte(self):
        """
        Décrementation du solde de 1, lorsqu'il atteint 0, afficher Game Over 
        """
        self.solde_initial -=1
        if self.solde_initial ==0:
             print("GAME OVER !")

#à mettre dans l'affichage 
class Solde_af(tk.Tk):
    """
    Classe pour afficher le solde dans une interface Tkinter.

    Attribute:
        solde : Instance de la classe Solde.
        label_solde 
    """
    def __init__(self, solde):
        super().__init__()
        self.solde=solde
        self.label_solde = tk.Label(self, text=f"Solde : {self.solde.solde_initial}")
        self.label_solde.pack()
        self.afficher()
        
        
    def afficher(self):
        """
        Met à jour l'affichage du solde qui diminue toutes les 1,5 sec, lorsque le solde affiche 0, "Game Over" apparaît
        """
        self.solde.decompte()
        self.label_solde['text'] = f"Solde : {self.solde.solde_initial}"
        self.label_solde.pack()
        if self.solde.solde_initial >0:
            self.after(1500, self.afficher)
        else:
            self.label_solde =tk.Label(self, text= "GAME OVER !!!!!")
            self.label_solde.pack()
            #self.after(1500, self.destroy())
      
    
f = Solde_af(Solde())
f.mainloop()

