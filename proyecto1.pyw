import pygame, random, os
from tkinter import *



def gameover():
    global fotogo
    global aceptar

    gameover=Toplevel()
    gameover.geometry(("500x200+550+300"))
    gameover.title("GAME OVER :(")
    gameover.attributes("-topmost", True)
    gameover.iconbitmap("logo.ico")
    
    fotogo=PhotoImage(file="gameover.gif")
    fondogo=Label(gameover, image=fotogo)
    fondogo.place(x=0, y=0)

    aceptar=PhotoImage(file="aceptar.gif")
    
    class quitButton(Button):
        pygame.quit()
        def __init__(self, parent):
            Button.__init__(self, parent)
            self['image'] = aceptar
            self['command'] = parent.destroy
            self.place(x=215, y=110)
    
    quitButton(gameover)
    
def congratulations():
    global fotocon
    global aceptar

    congrats=Toplevel()
    congrats.geometry(("500x200+550+300"))
    congrats.title("FELICITACIONES")
    congrats.attributes("-topmost", True)
    congrats.iconbitmap("logo.ico")  

    fotocon=PhotoImage(file="congratulations.gif")
    fondocon=Label(congrats, image=fotocon)
    fondocon.place(x=0, y=0)

    aceptar=PhotoImage(file="aceptar.gif")
    
    class quitButton(Button):
        pygame.quit()
        def __init__(self, parent):
            Button.__init__(self, parent)
            self['image'] = aceptar
            self['command'] = parent.destroy
            self.place(x=215, y=110)
    
    quitButton(congrats)

    
#-----------------------------------------CAMBIOS-----------------------------------------#
def castigo1():
    global ventanitainc1
    global medic
    global mediclado
    ventanitainc1.destroy()
    mediclado=50
    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic2.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()
    nivel1()
    
def recompensa1():
    global ventanitacor1
    global medic
    global mediclado
    ventanitacor1.destroy()
    mediclado=75
    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()
    nivel1()

def castigo2():
    global ventanitainc2
    global medicina
    global radiopildora
    global life
    ventanitainc2.destroy()
    life=3
    radiopildora=10
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora2.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()
            
    nivel2()
            
def recompensa2():
    global ventanitacor2
    global medicina
    global life
    global radiopildora
    ventanitacor2.destroy()

    life=4
    radiopildora=20
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()
    nivel2()
  
def castigo3():
    global ventanitainc3
    global medicina
    global radiopildora
    ventanitainc3.destroy()
    radiopildora=10
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora2.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()
            
    nivel3()
            
def recompensa3():
    global ventanitacor3
    global medicina

    ventanitacor3.destroy()

    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora3.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()
    
    nivel3()

def castigo4():
    global ventanitainc4
    global medic
    global mediclado
    ventanitainc4.destroy()
    mediclado=50
    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic2.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()
            
    nivel4()
            
def recompensa4():
    global ventanitacor4
    global medic
    global mediclado

    ventanitacor4.destroy()

    mediclado=100
    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic3.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()
    
    nivel4()
    
def castigo5():
    global ventanitainc5
    global medicina
    global radiopildora
    ventanitainc5.destroy()

    radiopildora=10
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora2.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()
            
    nivel5()
            
def recompensa5():
    global ventanitacor5
    global medicina
    global radiopildora

    ventanitacor5.destroy()

    radiopildora=35
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora3.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()
    
    nivel5()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PREGUNTA 1<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

def incorrecta1():
    global ventana1
    global ventanitainc1
    global resinc1
    global aceptar
    ventana1.withdraw()
    ventanitainc1=Toplevel()
    ventanitainc1.attributes("-topmost", True)
    ventanitainc1.geometry(("380x189+550+300"))
    ventanitainc1.title("RESULTADO")
    ventanitainc1.iconbitmap("logo.ico")

    
    resinc1=PhotoImage(file="castigo1.gif")
    fondoresinc1=Label(ventanitainc1, image=resinc1)
    fondoresinc1.pack()
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoninc=Button(ventanitainc1, image=aceptar, command=castigo1)
    botoninc.place(x=155, y=160)  

def correcta1():
    global ventana1
    global ventanitacor1
    global rescor1
    global aceptar
    ventana1.withdraw()
    ventanitacor1=Toplevel()
    ventanitacor1.attributes("-topmost", True)
    ventanitacor1.title("RESULTADO")
    ventanitacor1.geometry(("380x189+550+300"))
    ventanitacor1.iconbitmap("logo.ico")
    ventanitacor1.config(bg="green")
    
    rescor1=PhotoImage(file="recompensa1.gif")
    fondorescor1=Label(ventanitacor1, image=rescor1)
    fondorescor1.pack()

    aceptar=PhotoImage(file="aceptar.gif")
    botoncor=Button(ventanitacor1,  image=aceptar, command=recompensa1)
    botoncor.place(x=155, y=160)
      
def pregunta1():
    global ventana1    
    #######VENTANA####
    ventana1=Tk()
    ventana1.attributes("-topmost", True)
    ventana1.title("Pregunta 1")
    ventana1.iconbitmap("logo.ico")
    ventana1.geometry("750x350+0+0")
    ventana1.config(bg="white")
    ventana1.resizable(0,0)
    
    ######FONDO######
    pregunta1=PhotoImage(file="Pregunta1.gif")
    fondopregunta1=Label(ventana1, image=pregunta1)
    fondopregunta1.place(x=0, y=0)
    
    ######BOTONES######
    
    imageopcion1a=PhotoImage(file="opc1a.gif")
    opcion1a=Button(ventana1, command=incorrecta1, image=imageopcion1a)
    opcion1a.place(x=50,y=225)
    
    imageopcion1b=PhotoImage(file="opc1b.gif")
    opcion1b=Button(ventana1, command=incorrecta1, image=imageopcion1b)
    opcion1b.place(x=215,y=225)
    
    imageopcion1c=PhotoImage(file="opc1c.gif")
    opcion1c=Button(ventana1,command=correcta1, image=imageopcion1c)
    opcion1c.place(x=380,y=225)
    
    imageopcion1d=PhotoImage(file="opc1d.gif")
    opcion1d=Button(ventana1, command=incorrecta1, image=imageopcion1d)
    opcion1d.place(x=545,y=225)
    
    ventana1.mainloop()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PREGUNTA 2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

def incorrecta2():
    global ventana2
    global ventanitainc2
    global resinc2
    global aceptar
    ventana2.withdraw()
    ventanitainc2=Toplevel(ventana2)
    ventanitainc2.attributes("-topmost", True)
    ventanitainc2.title("RESULTADO")
    ventanitainc2.geometry(("380x189+550+300"))
    ventanitainc2.iconbitmap("logo.ico")
    ventanitainc2.config(bg="green")
    
    resinc2=PhotoImage(file="castigo2.gif")
    fondoresinc2=Label(ventanitainc2, image=resinc2)
    fondoresinc2.pack()
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoninc=Button(ventanitainc2,  image=aceptar, command=castigo2)
    botoninc.place(x=155, y=160)
    
def correcta2():
    global ventana2
    global ventanitacor2
    global aceptar
    global rescor2
    ventana2.withdraw()
    ventanitacor2=Toplevel(ventana2)
    ventanitacor2.title("RESULTADO")
    ventanitacor2.geometry(("380x189+550+300"))
    ventanitacor2.iconbitmap("logo.ico")
    ventanitacor2.config(bg="green")
    
    rescor2=PhotoImage(file="recompensa2.gif")
    fondorescor2=Label(ventanitacor2, image=rescor2)
    fondorescor2.pack()
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoncor=Button(ventanitacor2, image=aceptar, command=recompensa2)
    botoncor.place(x=155, y=160)
      
def pregunta2():
    global ventana2   
    #######VENTANA####
    ventana2=Toplevel()
    ventana2.title("Pregunta 2")
    ventana2.iconbitmap("logo.ico")
    ventana2.geometry("750x350+0+0")
    ventana2.config(bg="white")
    ventana2.resizable(0,0)
    
    ######FONDO######
    pregunta2=PhotoImage(file="Pregunta2.gif")
    fondopregunta2=Label(ventana2, image=pregunta2)
    fondopregunta2.place(x=0, y=0)
    
    ######BOTONES######
    
    imageopcion2a=PhotoImage(file="opc2a.gif")
    opcion2a=Button(ventana2, command=incorrecta2, image=imageopcion2a)
    opcion2a.place(x=50,y=225)
    
    imageopcion2b=PhotoImage(file="opc2b.gif")
    opcion2b=Button(ventana2, command=incorrecta2, image=imageopcion2b)
    opcion2b.place(x=215,y=225)
    
    imageopcion2c=PhotoImage(file="opc2c.gif")
    opcion2c=Button(ventana2,command=correcta2, image=imageopcion2c)
    opcion2c.place(x=380,y=225)
    
    imageopcion2d=PhotoImage(file="opc2d.gif")
    opcion2d=Button(ventana2, command=incorrecta2, image=imageopcion2d)
    opcion2d.place(x=545,y=225)
    
    ventana2.mainloop()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PREGUNTA 3<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    
def incorrecta3():
    global ventana3
    global ventanitainc3
    global resinc3
    global aceptar
    ventana3.withdraw()
    ventanitainc3=Toplevel(ventana3)
    ventanitainc3.title("RESULTADO")
    ventanitainc3.geometry(("380x189+550+300"))
    ventanitainc3.iconbitmap("logo.ico")
    ventanitainc3.config(bg="green")

    resinc3=PhotoImage(file="castigo3.gif")
    fondoresinc3=Label(ventanitainc3, image=resinc3)
    fondoresinc3.place(x=0, y=0)
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoninc=Button(ventanitainc3, image=aceptar, command=castigo3)
    botoninc.place(x=155, y=160)
    
def correcta3():
    global ventana3
    global ventanitacor3
    global aceptar
    global rescor3
    ventana3.withdraw()
    ventanitacor3=Toplevel(ventana3)
    ventanitacor3.title("RESULTADO")
    ventanitacor3.geometry(("380x189+550+300"))
    ventanitacor3.iconbitmap("logo.ico")
    ventanitacor3.config(bg="green")
    
    rescor3=PhotoImage(file="recompensa3.gif")
    fondorescor3=Label(ventanitacor3, image=rescor3)
    fondorescor3.place(x=0, y=0)
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoncor=Button(ventanitacor3, image=aceptar, command=recompensa3)
    botoncor.place(x=155, y=160)
      
def pregunta3():
    global ventana3   
    #######VENTANA####
    ventana3=Toplevel()
    ventana3.title("Pregunta 3")
    ventana3.iconbitmap("logo.ico")
    ventana3.geometry("750x350+0+0")
    ventana3.config(bg="white")
    ventana3.resizable(0,0)
    
    ######FONDO######
    pregunta3=PhotoImage(file="Pregunta3.gif")
    fondopregunta3=Label(ventana3, image=pregunta3)
    fondopregunta3.place(x=0, y=0)
    
    ######BOTONES######
    
    imageopcion3a=PhotoImage(file="opc3a.gif")
    opcion3a=Button(ventana3, command=correcta3, image=imageopcion3a)
    opcion3a.place(x=50,y=225)
    
    imageopcion3b=PhotoImage(file="opc3b.gif")
    opcion3b=Button(ventana3, command=incorrecta3, image=imageopcion3b)
    opcion3b.place(x=215,y=225)
    
    imageopcion3c=PhotoImage(file="opc3c.gif")
    opcion3c=Button(ventana3,command=incorrecta3, image=imageopcion3c)
    opcion3c.place(x=380,y=225)
    
    imageopcion3d=PhotoImage(file="opc3d.gif")
    opcion3d=Button(ventana3, command=incorrecta3, image=imageopcion3d)
    opcion3d.place(x=545,y=225)
    
    ventana3.mainloop()

   
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PREGUNTA 4<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    
def incorrecta4():
    global ventana4
    global ventanitainc4
    global resinc4
    global aceptar
    ventana4.withdraw()
    ventanitainc4=Toplevel(ventana4)
    ventanitainc4.title("RESULTADO")
    ventanitainc4.geometry(("380x189+550+300"))
    ventanitainc4.iconbitmap("logo.ico")
    ventanitainc4.config(bg="green")

    resinc4=PhotoImage(file="castigo4.gif")
    fondoresinc4=Label(ventanitainc4, image=resinc4)
    fondoresinc4.place(x=0, y=0)
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoninc=Button(ventanitainc4, image=aceptar, command=castigo4)
    botoninc.place(x=155, y=160)
    
def correcta4():
    global ventana4
    global ventanitacor4
    global aceptar
    global rescor4
    ventana4.withdraw()
    ventanitacor4=Toplevel(ventana4)
    ventanitacor4.title("RESULTADO")
    ventanitacor4.geometry(("380x189+550+300"))
    ventanitacor4.iconbitmap("logo.ico")
    ventanitacor4.config(bg="green")
    
    rescor4=PhotoImage(file="recompensa4.gif")
    fondorescor4=Label(ventanitacor4, image=rescor4)
    fondorescor4.place(x=0, y=0)
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoncor=Button(ventanitacor4, image=aceptar, command=recompensa4)
    botoncor.place(x=155, y=160)
      
def pregunta4():
    global ventana4
    #######VENTANA####
    ventana4=Toplevel()
    ventana4.title("Pregunta 4")
    ventana4.iconbitmap("logo.ico")
    ventana4.geometry("750x350+0+0")
    ventana4.config(bg="white")
    ventana4.resizable(0,0)
    
    ######FONDO######
    pregunta4=PhotoImage(file="Pregunta4.gif")
    fondopregunta4=Label(ventana4, image=pregunta4)
    fondopregunta4.place(x=0, y=0)
    
    ######BOTONES######
    
    imageopcion4a=PhotoImage(file="opc4a.gif")
    opcion4a=Button(ventana4, command=correcta4, image=imageopcion4a)
    opcion4a.place(x=50,y=225)
    
    imageopcion4b=PhotoImage(file="opc4b.gif")
    opcion4b=Button(ventana4, command=incorrecta4, image=imageopcion4b)
    opcion4b.place(x=215,y=225)
    
    imageopcion4c=PhotoImage(file="opc4c.gif")
    opcion4c=Button(ventana4,command=incorrecta4, image=imageopcion4c)
    opcion4c.place(x=380,y=225)
    
    imageopcion4d=PhotoImage(file="opc4d.gif")
    opcion4d=Button(ventana4, command=correcta4, image=imageopcion4d)
    opcion4d.place(x=545,y=225)
    
    ventana4.mainloop()

    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PREGUNTA 5<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    
def incorrecta5():
    global ventana5
    global ventanitainc5
    global resinc5
    global aceptar
    ventana5.withdraw()
    ventanitainc5=Toplevel(ventana5)
    ventanitainc5.title("RESULTADO")
    ventanitainc5.geometry(("380x189+550+300"))
    ventanitainc5.iconbitmap("logo.ico")
    ventanitainc5.config(bg="green")

    resinc5=PhotoImage(file="castigo5.gif")
    fondoresinc5=Label(ventanitainc5, image=resinc5)
    fondoresinc5.place(x=0, y=0)
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoninc=Button(ventanitainc5, image=aceptar, command=castigo5)
    botoninc.place(x=155, y=160)

def correcta5():
    global ventana5
    global ventanitacor5
    global aceptar
    global rescor5
    
    ventana5.withdraw()
    ventanitacor5=Toplevel(ventana5)
    ventanitacor5.title("RESULTADO")
    ventanitacor5.geometry(("380x189+550+300"))
    ventanitacor5.iconbitmap("logo.ico")
    ventanitacor5.config(bg="green")
    
    rescor5=PhotoImage(file="recompensa5.gif")
    fondorescor5=Label(ventanitacor5, image=rescor5)
    fondorescor5.place(x=0, y=0)
    
    aceptar=PhotoImage(file="aceptar.gif")
    botoncor=Button(ventanitacor5, image=aceptar, command=recompensa5)
    botoncor.place(x=155, y=160)
      
def pregunta5():
    global ventana5
    #######VENTANA####
    ventana5=Toplevel()
    ventana5.title("Pregunta 5")
    ventana5.iconbitmap("logo.ico")
    ventana5.geometry("750x350+0+0")
    ventana5.config(bg="white")
    ventana5.resizable(0,0)
    
    ######FONDO######
    pregunta5=PhotoImage(file="Pregunta5.gif")
    fondopregunta5=Label(ventana5, image=pregunta5)
    fondopregunta5.place(x=0, y=0)
    
    ######BOTONES######

    imageopcion5a=PhotoImage(file="opc5a.gif")
    opcion5a=Button(ventana5, command=correcta5, image=imageopcion5a)
    opcion5a.place(x=215,y=225)
    
    imageopcion5b=PhotoImage(file="opc5b.gif")
    opcion5b=Button(ventana5,command=incorrecta5, image=imageopcion5b)
    opcion5b.place(x=380,y=225)
    
    
    ventana5.mainloop()
   
#------------------------------------------VIRUS------------------------------------------#
Negro = (0,0,0)
Blanco = (255,255,255)
#---------------------------------------VIRUS  ROJO---------------------------------------#

class virus1(pygame.sprite.Sprite):
    def __init__(selfi):
        super().__init__()
        selfi.image = pygame.image.load("virus1.png").convert()
        selfi.image.set_colorkey(Blanco)
        selfi.rect=selfi.image.get_rect()
        
#--------------------------------------VIRUS NARANJA--------------------------------------#
        
class virus2(pygame.sprite.Sprite):
    def __init__(selfi):
        super().__init__()
        selfi.image = pygame.image.load("virus2.png").convert()
        selfi.image.set_colorkey(Blanco)
        selfi.rect=selfi.image.get_rect()

#-------------------------------------VIRUS  AMARILLO-------------------------------------#

class virus3(pygame.sprite.Sprite):
    def __init__(selfi):
        super().__init__()
        selfi.image = pygame.image.load("virus3.png").convert()
        selfi.image.set_colorkey(Blanco)
        selfi.rect=selfi.image.get_rect()
        
#---------------------------------------VIRUS VERDE---------------------------------------#

class virus4(pygame.sprite.Sprite):
    def __init__(selfi):
        super().__init__()
        selfi.image = pygame.image.load("virus4.png").convert()
        selfi.image.set_colorkey(Blanco)
        selfi.rect=selfi.image.get_rect()
        
#---------------------------------------VIRUS  AZUL---------------------------------------#

class virus5(pygame.sprite.Sprite):
    def __init__(selfi):
        super().__init__()
        selfi.image = pygame.image.load("virus5.png").convert()
        selfi.image.set_colorkey(Blanco)
        selfi.rect=selfi.image.get_rect()

#-------------------------------------BORRAR PANTALLA-------------------------------------#
def vamosBorrar():
  if os.name == "posix":
     os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
     os.system ("cls")
     
#-----------------------------------------NIVEL 1-----------------------------------------#

def nivel1():
    global medic
    global mediclado
    global life
    a=1
    vamosBorrar()

    life=3
    posicionbolax=380
    posicionbolay=400

    posicionvirus1y=1
    velocidadx=0
    velocidady=0
        

    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    for i in range(10):
        x=1
        if i==0:
            x+=123
            while x<800:
                if x<245:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                elif 491>x>245:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=246
                elif 614>x>491:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=200
            posicionvirus1y+=31
        elif i==1:
            x+=61.5
            while x<800:
                if x<305:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                elif 428>x>305:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=123
                elif 735>x>428:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=500
            posicionvirus1y+=31
        elif i==2 or i==3:
            while x<800:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            posicionvirus1y+=31
        elif i==4:
            x+=61.5
            while x<800:
                if x<735:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=200
            posicionvirus1y+=31
        elif i==5:
            x+=123
            while x<800:
                if x<674:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=200
            posicionvirus1y+=31
        elif i==6:
            x+=184.5
            while x<800:
                if x<610:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=300
            posicionvirus1y+=31
        elif i==7:
            x+=246
            while x<800:
                if x<520:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=500
            posicionvirus1y+=31
        elif i==8:
            x+=307.5
            while x<800:
                if x<450:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=700
            posicionvirus1y+=31
        elif i==9:
            x+=369
            while x<800:
                if x<400:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=800
            posicionvirus1y+=31
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)
    fluid=True
    fondo = pygame.image.load("Fondo.png").convert()
    while fluid:
        
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-mediclado
        rect2=rect+mediclado
        
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False
            if i.type==pygame.MOUSEBUTTONDOWN:
              if a==1:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                musicafondo = 'musicafondo.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(musicafondo)
                pygame.mixer.music.play(-1)
                a+=1
                
        ventana.blit(fondo,[0,0])
                #objetos
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500
        medicina.rect.x=posicionbolax-20
        medicina.rect.y=posicionbolay-20
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==790:
            velocidadx*= -1
        elif posicionbolax==10:
            velocidadx*= -1
            
        if posicionbolay==590:
            posicionbolay = 300
            life-=1
        elif posicionbolay==10:
            velocidady*= -1
            
        todosObjetos.draw(ventana)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-20,posicionbolay+20),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+20,posicionbolay+20),0)
        if punto3.colliderect(medic) or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1
        if life==0 or len(virusLista)==0:
            fluid=False
            
        pygame.display.flip()

    pygame.quit()
    if life!=0 and len(virusLista)==0:
        pregunta2()
    elif life==0 and len(virusLista)!=0:
        gameover()
    elif life!=0 and len(virusLista)!=0:
        gameover()
    
    
#-----------------------------------------NIVEL 2-----------------------------------------#
    
def nivel2():
    global medic
    global medicina
    global radiopildora
    global life
    
    
    a=1
    
    vamosBorrar()
        
    posicionbolax=400-radiopildora
    posicionbolay=400

    posicionvirus1y=1
    velocidadx=0
    velocidady=0

    
    mediclado=75
    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()

    
    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    for i in range(6):
        x=1
        if i==0:
            while x<800:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31
        elif i==1:
            x=61.5
            while x<737:
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==2:
            x=123
            while x<676:
                bloque=virus3()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==3:
            x=184
            while x<614:
                bloque=virus4()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==4:
            x=246
            while x<553:
                bloque=virus5()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==5:
            x=307.5
            while x<492:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)

    fluid=True
    fondo=pygame.image.load("Fondo.png").convert()
    while fluid:
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-mediclado
        rect2=rect+mediclado
    
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False
            if i.type==pygame.MOUSEBUTTONDOWN:
              if a==1:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                musicafondo = 'musicafondo.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(musicafondo)
                pygame.mixer.music.play(-1)
                a+=1
        
        ventana.blit(fondo,[0,0])
                
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500
        medicina.rect.x=posicionbolax-radiopildora
        medicina.rect.y=posicionbolay-radiopildora
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==800-radiopildora:
            velocidadx*= -1
        elif posicionbolax<=radiopildora:
            velocidadx *= -1
        
        if posicionbolay==600-radiopildora:
            posicionbolay = 300
            life-=1
        elif posicionbolay<=radiopildora:
            velocidady *= -1
        
        todosObjetos.draw(ventana)
        punto1=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay-radiopildora),0)
        punto2=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay-radiopildora),0)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay+radiopildora),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay+radiopildora),0)
        if punto3.colliderect(medic) or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1
        if life==0 or len(virusLista)==0:
            fluid=False        

        pygame.display.flip()

    pygame.quit()
    if life!=0 and len(virusLista)==0:
        pregunta3()
    elif life==0 and len(virusLista)!=0:
        gameover()
    elif life!=0 and len(virusLista)!=0:
        gameover()

#-----------------------------------------NIVEL 3-----------------------------------------#
    
def nivel3():
    global medicina
    a=1

    vamosBorrar()
    
    posicionbolax=400-radiopildora
    posicionbolay=400

    life=3
    posicionvirus1y=1
    velocidadx=0
    velocidady=0
    
    
    class medic(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("medic.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect = self.image.get_rect()

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    for i in range(7):
        if i==0 or i==6:
            x=1
            while x<800:
                bloque=virus5()
                bloque.rect.x=x
                bloque.rect.y=posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            posicionvirus1y+=31
        elif i==3:
            x=1
            while x<800:
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                if x==308.5:
                    x+=123
                else:
                    x+=61.5
            posicionvirus1y+=31
        elif i==2 or i==4:
            x=1
            while x<800:
                bloque=virus3()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                if x==247:
                    x+=246
                else:
                    x+=61.5
            posicionvirus1y+=31
        elif i==1 or i==5:
            x=1
            while x<800:
                bloque=virus4()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                if x==185.5:
                    x+=369
                else:
                    x+=61.5
            posicionvirus1y+=31
    
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)

    fluid=True
    fondo=pygame.image.load("Fondo.png").convert()
    while fluid:
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-75
        rect2=rect+75
    
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False
            if i.type==pygame.MOUSEBUTTONDOWN:
              if a==1:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                musicafondo = 'musicafondo.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(musicafondo)
                pygame.mixer.music.play(-1)
                a+=1
            
        ventana.blit(fondo,[0,0])
        
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500    
        medicina.rect.x=posicionbolax-radiopildora
        medicina.rect.y=posicionbolay-radiopildora
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==800-radiopildora:
            velocidadx*= -1
        elif posicionbolax==radiopildora:
            velocidadx*= -1
        
        if posicionbolay==600-radiopildora:
            posicionbolay = 300
            life-=1
        elif posicionbolay==radiopildora:
            velocidady*= -1
        
        todosObjetos.draw(ventana)
        punto1=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay-radiopildora),0)
        punto2=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay-radiopildora),0)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay+radiopildora),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay+radiopildora),0)
        if punto3.colliderect(medic) or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1

        if life==0 or len(virusLista)==0:
            fluid=False
        pygame.display.flip()

    pygame.quit()
    if life!=0 and len(virusLista)==0:
        pregunta4()
    elif life==0 and len(virusLista)!=0:
        gameover()
    elif life!=0 and len(virusLista)!=0:
        gameover()

#-----------------------------------------NIVEL 4-----------------------------------------#
    
def nivel4():
    global medic
    global mediclado
    a=1
    vamosBorrar()
    
    posicionbolax=380
    posicionbolay=400

    life=3

    posicionvirus1y=1
    velocidadx=0
    velocidady=0
    
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    x=170
    while x<600:        
            bloque=virus2()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

    posicionvirus1y+=31
    for i in range(2):
        x=110
        while x<614:
                
            bloque=virus2()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        posicionvirus1y+=31
        
    for i in range(2):
        x=110
        while x<233:
            
            bloque=virus2()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        for i in range(2):
            x=355
            while x<410:
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

        for i in range(2):
            x=540
            while x<602:
            
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
    
        posicionvirus1y+=31

    for i in range(2):
        x=110
        while x<614:
                
            bloque=virus2()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        posicionvirus1y+=31

    x=171
    while x<550:
            bloque=virus2()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

    posicionvirus1y+=31

    x=232
    while x<500:
            bloque=virus2()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

    posicionvirus1y+=31

    for i in range(2):
        x=232
        while x<290:            
            bloque=virus2()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        for i in range(4):
            x=355
            while x<410:                    
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

        for i in range(4):
            x=478
            while x<535:            
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
    
        posicionvirus1y+=31

    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)

    fluid=True
    fondo=pygame.image.load("Fondo.png").convert()
    while fluid:
            rectangulox=pygame.mouse.get_pos()   
            rect=rectangulox[0]
            rect1=rect-mediclado
            rect2=rect+mediclado

            for i in pygame.event.get(): 
                    if i.type==pygame.QUIT:
                            fluid=False
                            
                    if i.type==pygame.MOUSEBUTTONDOWN:
                      if a==1:
                        velocidadx=random.choice((-1,1))
                        velocidady=random.choice((-1,1))
                        musicafondo = 'musicafondo.mp3'
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load(musicafondo)
                        pygame.mixer.music.play(-1)
                        a+=1
                    
            ventana.blit(fondo,[0,0])
                
            if rect1>=0 and rect2<=800:
                    medic.rect.x=rect1

            medic.rect.y=500
            medicina.rect.x=posicionbolax-20
            medicina.rect.y=posicionbolay-20
            posicionbolax+=velocidadx
            posicionbolay+=velocidady
            if posicionbolax==800:
                    velocidadx*= -1
            elif posicionbolax==10:
                    velocidadx*= -1

            if posicionbolay==600:
                    posicionbolay = 300
                    life-=1
            elif posicionbolay==10:
                    velocidady*= -1

            todosObjetos.draw(ventana)
                
            punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-20,posicionbolay+20),0)
            punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+20,posicionbolay+20),0)
            if punto3.colliderect(medic) or punto4.colliderect(medic):
                    velocidady*= -1

            if pygame.sprite.spritecollide(medicina, virusLista , True):
                    velocidady*= -1

            if life==0 or len(virusLista)==0:
                    fluid=False

            pygame.display.flip()

    pygame.quit()
    if life!=0 and len(virusLista)==0:
        pregunta5()
    elif life==0 and len(virusLista)!=0:
        gameover()
    elif life!=0 and len(virusLista)!=0:
        gameover()

#-----------------------------------------NIVEL 5-----------------------------------------#
    
def nivel5():
    global medicina
    global radiopildora
    a=1

    vamosBorrar()

    life=3

    posicionbolax=400-radiopildora
    posicionbolay=400

    posicionvirus1y=1
    velocidadx=0
    velocidady=0

    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()
                              

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()


    for i in range(5):
        x=1
        
        while x<800:
            if i==0:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==1:
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==2:
                bloque=virus3()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==3:
                bloque=virus4()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==4:
                bloque=virus5()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5


        posicionvirus1y+=31
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)


    fluid=True
    fondo = pygame.image.load("Fondo.png").convert()

    while fluid:
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-75
        rect2=rect+75
    
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False

            if i.type==pygame.MOUSEBUTTONDOWN:
              if a==1:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                musicafondo = 'musicafondo.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(musicafondo)
                pygame.mixer.music.play(-1)
                a+=1
                
        ventana.blit(fondo,[0,0])
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500
        medicina.rect.x=posicionbolax-radiopildora
        medicina.rect.y=posicionbolay-radiopildora
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==800-radiopildora:
            velocidadx*= -1
        elif posicionbolax==radiopildora:
            velocidadx*= -1
        
        if posicionbolay==600-radiopildora:
            posicionbolay = 300
            life-=1
        elif posicionbolay==radiopildora:
            velocidady*= -1
        
        todosObjetos.draw(ventana)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay+radiopildora),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay+radiopildora),0)
            
         
        if punto3.colliderect(medic)or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1

        if life==0 or len(virusLista)==0:
            fluid=False                

        pygame.display.flip()
    if life!=0 and len(virusLista)==0:
        congratulations()
    elif life==0 and len(virusLista)!=0:
        gameover()
    elif life!=0 and len(virusLista)!=0:
        gameover()
          
pregunta1()






            

    
