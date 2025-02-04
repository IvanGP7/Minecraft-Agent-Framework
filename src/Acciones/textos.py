import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create("localhost")

def print_Menu_Acciones():
    time.sleep(0.2)
    mc.postToChat(" ")
    mc.postToChat("Acciones disponibles [0-5]")
    mc.postToChat("0- Test")
    mc.postToChat("1- Crear Dinamita")
    mc.postToChat("2- Chat Insultos")
    mc.postToChat("3- Conexion con chatGPT")
    mc.postToChat("4- Falta por Crear")
    mc.postToChat("5- Teleport")
    mc.postToChat("10- Parar Script")
    return 0

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
    return 0
    
def menu_insult():
    time.sleep(0.2)
    mc.postToChat(" ")
    mc.postToChat("Elige una opcion:")
    mc.postToChat("1- Incluir un insulto a la lista")
    mc.postToChat("2- Ser insultado")
    mc.postToChat("3- Ver lista de insultos")
    mc.postToChat("4- Imprimir insutos de longitud")
    mc.postToChat("5- Imprimir lista en minuscuas")
    mc.postToChat("6- Salir")
    return 0