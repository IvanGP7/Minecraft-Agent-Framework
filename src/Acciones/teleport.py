from Acciones.lectura_chat import *
import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create("localhost")

def cambiar_posicion(x, y, z):

    if hasattr(mc.player, "setTilePos"):  
        metodo = getattr(mc.player, "setTilePos")  
        metodo(x, y, z)  
        mc.postToChat(f"Jugador movido a: ({x}, {y}, {z})")
    else:
        print("Error: No se pudo encontrar el método 'setTilePos' en mc.player")



def teleport():
    mc.postToChat("Escribe las coordenadas del teleport.")
    mc.postToChat("X:")
    x = int(Lectura_chat())
    time.sleep(0.2)
    mc.postToChat("Y:")
    y = int(Lectura_chat())
    time.sleep(0.2)
    mc.postToChat("Z:")
    z = int(Lectura_chat())
    time.sleep(0.2)
    cambiar_posicion(x, y, z)