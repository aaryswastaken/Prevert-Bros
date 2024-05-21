import tkinter as tk

'''
il faut utiliser after et non sleep '''

class Solde:
    __slots__=['solde_initial']
    
    def __init__(self):
        self.solde_initial = 10

    
    def decompte(self):
        self.solde_initial -=1
        if self.solde_initial ==0:
             print("GAME OVER !")


class Solde_af(tk.Tk):
    def __init__(self, solde):
        super().__init__()
        self.solde=solde
        self.label_solde = tk.Label(self, text=f"Solde : {self.solde.solde_initial}")
        self.label_solde.pack()
        self.afficher()
        
        
    def afficher(self):
        self.solde.decompte()
        self.label_solde['text'] = f"Solde : {self.solde.solde_initial}"
        self.label_solde.pack()
        if self.solde.solde_initial >0:
            self.after(1000, self.afficher)
        else:
            self.label_solde =tk.Label(self, text= "GAME OVER !!!!!")
            self.label_solde.pack()
            #self.after(1500, self.destroy())
      
    
f = Solde_af(Solde())
f.mainloop()

