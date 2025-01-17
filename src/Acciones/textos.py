import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create("localhost")

def print_Menu_Acciones():
    mc.postToChat(" ")
    mc.postToChat("Acciones disponibles [0-5]")
    mc.postToChat("0- Test")
    mc.postToChat("1- Crear Dinamita")
    mc.postToChat("2- Chat Insultos --> Falta Programar")
    mc.postToChat("3- Falta por definir")
    mc.postToChat("4- Falta por definir")
    mc.postToChat("5- Falta por definir")
    mc.postToChat("10- Parar Script")

def informacion_basica():
    
    mc.postToChat(" ")
    mc.postToChat("Informacion Basica")

    # Entidades y lectura del char
    players_ids = mc.getPlayerEntityIds()
    print(len(players_ids), " entidad/es disponible/s.")
    number = len(players_ids)
    mc.postToChat( "%s Entidad/es en el server" %number)

    for id in players_ids:
        mc.postToChat("Entidad : %s" %id)