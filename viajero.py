from tkinter import *
from numpy import *


def mostrar_resultado():
    if ciudad.get() == "arad" or ciudad.get() == "Arad":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Arad.configure(text="")

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=170)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=190)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=210)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=230)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=250)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=270)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=290)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=310)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=330)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=350)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=370)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=390)

    if ciudad.get() == "zerind" or ciudad.get() == "Zerind":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Zerind.configure(text="")

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=170)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=190)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=210)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=230)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=250)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=270)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=290)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=310)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=330)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=350)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=370)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=390)

    if ciudad.get() == "oradea" or ciudad.get() == "Oradea":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Oradea.configure(text="")

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=170)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=190)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=210)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=230)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=250)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=270)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=290)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=310)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=330)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=350)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=370)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=390)

    if ciudad.get() == "sibiu" or ciudad.get() == "Sibiu":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Sibiu.configure(text="")
        
        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=170)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=190)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=210)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=230)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=250)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=270)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=290)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=310)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=330)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=350)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=370)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=390)

    if ciudad.get() == "fagaras" or ciudad.get() == "Fagaras":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")
        
        Fagaras.configure(text="")

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=170)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=190)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=210)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=230)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=250)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=270)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=290)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=310)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=330)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=350)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=370)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=390)

    if ciudad.get() == "bucharest" or ciudad.get() == "Bucharest":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Bucharest.configure(text="")

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=170)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=190)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=210)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=230)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=250)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=270)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=290)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=310)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=330)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=350)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=370)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=390)

    if ciudad.get() == "pitesti" or ciudad.get() == "Pitesti":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Pitesti.configure(text="")

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=170)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=190)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=210)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=230)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=250)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=270)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=290)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=310)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=330)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=350)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=370)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=390)

    if ciudad.get() == "rimnicu vilcea" or ciudad.get() == "Rimnicu Vilcea":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Rimmicu_vilcea.configure(text="")

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=170)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=190)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=210)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=230)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=250)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=270)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=290)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=310)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=330)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=350)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=370)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=390)

    if ciudad.get() == "craiova" or ciudad.get() == "Craiova":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Craiova.configure(text="")

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=170)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=190)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=210)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=230)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=250)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=270)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=290)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=310)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=330)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=350)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=370)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=390)

    if ciudad.get() == "drobeta" or ciudad.get() == "Drobeta":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Drobeta.configure(text="")

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=170)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=190)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=210)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=230)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=250)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=270)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=290)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=310)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=330)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=350)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=370)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=390)

    if ciudad.get() == "mehadia" or ciudad.get() == "Mehadia":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Mehadia.configure(text="")

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=170)

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=190)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=210)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=230)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=250)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=270)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=290)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=310)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=330)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=350)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=370)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=390)

    if ciudad.get() == "lugoj" or ciudad.get() == "Lugoj":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Lugoj.configure(text="")

        Timisoara.configure(text="Timisoara")
        Timisoara.place(x=900, y=170)

        Arad.configure(text="Arad")
        Arad.place(x=900, y=190)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=210)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=230)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=250)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=270)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=290)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=310)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=330)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=350)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=370)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=390)

    if ciudad.get() == "timisoara" or ciudad.get() == "Timisoara":
        label.configure(text="El recorrido de punto de partida desde \n" +
                        ciudad.get() + " hacia el mismo punto es:")

        Timisoara.configure(text="")

        Arad.configure(text="Arad")
        Arad.place(x=900, y=170)

        Zerind.configure(text="Zerind")
        Zerind.place(x=900, y=190)

        Oradea.configure(text="Oradea")
        Oradea.place(x=900, y=210)

        Sibiu.configure(text="Sibiu")
        Sibiu.place(x=900, y=230)

        Fagaras.configure(text="Fagaras")
        Fagaras.place(x=900, y=250)

        Bucharest.configure(text="Bucharest")
        Bucharest.place(x=900, y=270)

        Pitesti.configure(text="Pitesti")
        Pitesti.place(x=900, y=290)

        Rimmicu_vilcea.configure(text="Rimnicu Vilcea")
        Rimmicu_vilcea.place(x=900, y=310)

        Craiova.configure(text="Craiova")
        Craiova.place(x=900, y=330)

        Drobeta.configure(text="Drobeta")
        Drobeta.place(x=900, y=350)

        Mehadia.configure(text="Mehadia")
        Mehadia.place(x=900, y=370)

        Lugoj.configure(text="Lugoj")
        Lugoj.place(x=900, y=390)

    if ciudad.get() == "":
        label.configure(text="Ingrese el nombre de una ciudad.")
        Zerind.configure(text="")
        Oradea.configure(text="")
        Sibiu.configure(text="")
        Fagaras.configure(text="")
        Bucharest.configure(text="")
        Pitesti.configure(text="")
        Rimmicu_vilcea.configure(text="")
        Craiova.configure(text="")
        Drobeta.configure(text="")
        Mehadia.configure(text="")
        Lugoj.configure(text="")
        Timisoara.configure(text="")
        Arad.configure(text="")


ventana = Tk()
ventana.geometry("1200x680")
ventana.title("Grafo")

label = Label(ventana, text="")
label.place(x=900, y=110)

Arad = Label(ventana, text="")

Zerind = Label(ventana, text="")

Oradea = Label(ventana, text="")

Sibiu = Label(ventana, text="")

Fagaras = Label(ventana, text="")

Bucharest = Label(ventana, text="")

Pitesti = Label(ventana, text="")

Rimmicu_vilcea = Label(ventana, text="")

Craiova = Label(ventana, text="")

Drobeta = Label(ventana, text="")

Mehadia = Label(ventana, text="")

Lugoj = Label(ventana, text="")

Timisoara = Label(ventana, text="")

imagen = PhotoImage(file="viajero.png")
Label(ventana, image=imagen).place(x=0, y=0)
Label(ventana, text="Ingresa la ciudad de punto de partida:").place(x=900, y=20)

ciudad = Entry(ventana)
ciudad.place(x=900, y=50)


Button(ventana, text="Ingresar", command=mostrar_resultado).place(x=900, y=80)


ventana.mainloop()
