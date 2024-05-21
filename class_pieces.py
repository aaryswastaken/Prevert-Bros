import tkinter as tk
from class_objet import Objet

class Pieces(tk.Tk, Objet):
    __slots__=["canvas","compteur"]
    def __init__(self):
        super().__init__()
        self.x_centre_piece = x_centre
        self.y_centre_piece = y_centre
        self.compteur =0
        self.creer_widgets()
        #self.disparition_piece()
    
    
    def creer_widgets(self):
        #ATTENTION INTRODUIRE LE VERITABLE FOND COMME BACKGROUND PLUTOT QUE LA LIGNE SUIVANTE 
        self.canvas = tk.Canvas(self, background= "white")
        self.canvas.create_oval((10, 10), (30, 30), fill="yellow", width=1, outline="black")
        self.canvas.create_oval((25, 26), (24, 26), fill="brown")
        self.canvas.create_oval((18, 18), (16, 16), fill="brown")
        self.canvas.create_oval((22, 12), (23, 13), fill="brown")
        self.canvas.create_oval((14, 25), (13, 27), fill="brown")
        self.canvas.create_oval((22, 21), (23, 22), fill="brown")
        self.canvas.pack()
    
    """    
    def disparition_piece(self):#OU EST CE QUIL FAUT LA METTRE: DANS LE CONTROLEUR ? EN CODE? DANS LAFFIHCAGE?
        #APPELER LA POSITION DU PLAYER
        # JE SAIS PAS COMMENT ON FAIT 
        
        xpossible=(self.x_centre_piece -15, self.x_centre_piece+15)
        ypossible = (self.x_centre_piece -15, self.x_centre_piece+15)
        if x_perso in xpossible and y_perso in ypossible:
            self.canvas.destroy()
            self.compteur+=1
    """        
            
        






piece=Pieces()
piece.mainloop()

#disparition qd xplayer et y player  = x et y pieces

