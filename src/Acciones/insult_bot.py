
from Acciones.lectura_chat import *
from Acciones.textos import menu_insult
import mcpi.minecraft as minecraft
import random


mc = minecraft.Minecraft.create("localhost")

lista_insultos = ["BOBO", "ZOQUETE", "GILIPOLLAS", "INEPTO", "MONONEURONAL", "RETRASADO"]

# Función para añadir un insulto a la lista global
def add_insulto(insulto):
    if insulto not in lista_insultos:
        lista_insultos.append(insulto)
        mc.postToChat("Se ha incluido a la lista: %s" %str(insulto))
        print(str(insulto) + " Se ha añadido a la lista de insultos global.")
        return 0 # Insulto añadido correctamente
    else:
        mc.postToChat("Este insulto ya existe en la lista")
        print(str(insulto) + " Ya existe dentro de la lista.")
        return 1 # Insulto ya existente

# Función para Escribir por chat un insulto a través de un índice.
def print_insult(indice):
    if indice <= len(lista_insultos):
        mc.postToChat(lista_insultos[indice-1])
        return 0
    else:
        print("Se ha intentado escribir el insulto " + str(indice) + ", cuando solo tenemos " + str(len(lista_insultos)) + " elementos en la lista.")
        return 1

def print_lista_insultos():
    i=0
    for posicion in lista_insultos:
        mc.postToChat("%s" %lista_insultos[i])
        i += 1
    return i # Devuelve el numero de insultos impresos 


#
# Leer chat para almacenar insulto
# insultar a (mostrar lista de entidades y que elija)
# Decidir que insulto o si hacerlo aleatorio
#
def insult_bot():
    
    trobat = False
    while trobat == False:
        
        menu_insult()
        valor = int(Lectura_chat())
        
        if valor == 1:
            mc.postToChat("Escribe tu insulto:")
            insulto = str(Lectura_chat())
            add_insulto(insulto)
        
        if valor == 2:
            indice = random.randint(1, len(lista_insultos))
            print_insult(indice)
            
        if valor == 3:
            print_lista_insultos()
        
        if valor == 4:
            trobat = True
        
        