import numpy as np
import random 
from tkinter import *
from tkinter import ttk

global mat_Dist
global initial_City

mat_Dist = np.array([[0,8,4,15],[8,0,7,9],[4,7,0,10],[15,9,10,0]])
#initial_City = int(input('Ciudad inicial(0,1,2,3): '))
#num_Iteraciones = int(input('Ingresa número de interaciones: '))

raiz=Tk()
raiz.title ("Metro CDMX")
raiz.resizable(0,0)
#raiz.iconbitmap("metro_logotipo.ico")  
raiz.config(bg="light blue")

def boton_buscar():
    txtrespuesta.delete('1.0', END)
    initial_City = int(cuadroinicio.get())
    num_Iteraciones = int(cuadrofin.get())
    def camino_Inicio():
      global mat_Dist
      global initial_City
      copy_mat_Dist = mat_Dist.copy() # matriz a seguir
      ruta_Inicial = [initial_City]
      sig_Ciudad = initial_City
      a = 0
      while len(ruta_Inicial) < len(mat_Dist[0,:]):
        copy_mat_Dist[sig_Ciudad,:] = 0
        r = np.where(copy_mat_Dist[:,sig_Ciudad]>0) #busca ciudades disponibles
        sig_Ciudad = random.choice(r[0])
        ruta_Inicial.append(sig_Ciudad)
      ruta_Inicial.append(initial_City)
      print(ruta_Inicial)
      return ruta_Inicial
    
    def intercambia(num_Iteraciones,ruta_Inicial):
      nueva_Ruta = ruta_Inicial.copy()
      mejor_Ruta = ruta_Inicial.copy()
      print(ruta_Inicial)
      for i in range(num_Iteraciones):
        anterior_Ruta = nueva_Ruta.copy() 
        elemento1 = random.randint(1,len(nueva_Ruta)-2)
        r = list(range(1,elemento1)) + list(range(elemento1+1,len(nueva_Ruta)-1))
        elemento2 = random.choice(r)
        nueva_Ruta[elemento1], nueva_Ruta[elemento2] = nueva_Ruta[elemento2], nueva_Ruta[elemento1] 
        if evalua_Ruta(anterior_Ruta,nueva_Ruta):
          mejor_Ruta = nueva_Ruta.copy()
        print(mejor_Ruta)
        return mejor_Ruta
        
    def evalua_Ruta(anterior_Ruta,nueva_Ruta):
      global mat_Dist
      suma_Ranterior = 0
      suma_Rnueva = 0
      for i in range(len(anterior_Ruta)-1):
        suma_Ranterior += mat_Dist[anterior_Ruta[i],anterior_Ruta[i+1]]
        suma_Rnueva += mat_Dist[nueva_Ruta[i],nueva_Ruta[i+1]]
      print(suma_Rnueva)
      return suma_Rnueva < suma_Ranterior

    ruta_Inicial = camino_Inicio()
    best = intercambia(num_Iteraciones,ruta_Inicial)
    #print("Viaja en la línea A del metro")
    txtrespuesta.insert(INSERT,best)
    txtrespuesta.insert(END,"")
# ------------------------- TERMINA BOTON --------------------------------

#FRAME DEL TITULO 
frameT=Frame(raiz,width="400",height="80")
frameT.pack()
frameT.config(bg="light blue")


#FRAME DE LA IMAGEN 
frameM=Frame(raiz,width="500",height="350")
frameM.pack(side="left")
frameM.config(bg="light blue")

#FRAME DE LA BUSQUEDA 
frameS=Frame(raiz,width="500",height="600")
frameS.pack(side="right", anchor="n")
frameS.config(bg="light blue")

###########################################################
#IMAGEN DEL METRO 
imagenM=PhotoImage(file="viajero.png")
labelM=Label(frameM,image=imagenM)
labelM.place(x=20,y=1)

# TEXTO DEL TITULO 
labelT=Label(frameT,text="Viajero vendedor",font=("Arial Narrow",25))
labelT.place(x=50,y=25)
labelT.config(bg="light blue")

# TEXTO DEL RESPUESTA 
labelA=Label(frameS,text="¿A dónde quieres ir?",font=("Arial Narrow",15))
labelA.place(x=120,y=20)
labelA.config(bg="light blue")
#----------------- TEXTO DE RESPUESTA--------------------------
labelA=Label(frameS,text="RUTA A SEGUIR",font=("Arial Narrow",10))
labelA.place(x=50,y=200)
labelA.config(bg="light blue")

texto=StringVar()
txtrespuesta=Text(frameS,width=40,height=14)#,state=DISABLED)
txtrespuesta.place(x=50,y=245)
txtrespuesta.config(bg="white")
#----------------- TEXTO DE INICIO -----------------------------
cuadroinicio=ttk.Combobox(frameS)#,state="readonly")
cuadroinicio["values"]=[0,1,2,3]
cuadroinicio.place(x=110,y=100)

labelinicio=Label(frameS,text="INICIO:",font=("Arial Narrow",10))
labelinicio.place(x=45,y=100)
labelinicio.config(bg="light blue")
#----------------- TEXTO DE FIN -----------------------------
cuadrofin=ttk.Combobox(frameS)#,state="readonly")
#cuadrofin["values"]=[0,1,2,3]
cuadrofin.place(x=240,y=140)

labelfin=Label(frameS,text="Número de iteraciones: ",font=("Arial Narrow",10))
labelfin.place(x=45,y=140)
labelfin.config(bg="light blue")
#------------------ BOTON-------------------------------------
Bbuscar=Button(frameS,text="Buscar",command=boton_buscar)
Bbuscar.place(x=350,y=100)
Bbuscar.config(bg="white")


raiz.mainloop()