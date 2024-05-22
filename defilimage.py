import tkinter as tk


class fenetre(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('test')
        
        #self.attributes('-fullscreen', True)
        self.bind('<Escape>',lambda e: self.destroy())
        
        self.caneva = tk.Canvas(self, width=300, height=300)
        self.caneva.grid()
        
        self.img = tk.PhotoImage(master = self.caneva, file='test.png')
        self.image = self.caneva.create_image(150, 150, image=self.img) 
        self.x = 0
        
        self.bind("<Right>", self.avancer)
        self.bind("<Left>", self.reculer)
    
    def avancer(self, event):
        self.x -= 3
        self.caneva.move(self.image, -8, 0)
    
    def reculer(self, event):
        self.x += 3
        self.caneva.move(self.image, +8, 0)
        

fenetre().mainloop()