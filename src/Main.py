
from Modulo_funciones import *
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create("localhost")

#Para limpiar la terminal minimamente
print("\n") 
mc.postToChat(" ")
# Paramos 2 segundos para poder abrir con tranquilidad el Minecraft
time.sleep(2)

# Ejemplo: Conexión al juego
mc.postToChat("Hello Minecraft World")
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)

# Test del insult Bot
lista = ["BOBO", "ZOQUETE", "GILIPOLLAS", "INEPTO", "MONONEURONAL", "RETRASADO"]

for insult in lista:
    add_insulto(insult)

insult_bot(2)

print() #Para limpiar la terminal minimamente

# Test de la TNT

mc.setBlock(pos.x + 3, pos.y+1, pos.z, block.TNT.id, 1)  # Encender la TNT
mc.setBlock(pos.x + 3, pos.y+1, pos.z+1, block.TNT.id, 1)  # Encender la TNT


# Entidades y lectura del char

players_ids = mc.getPlayerEntityIds()
print(len(players_ids), " entidad/es disponible/s.")
number = len(players_ids)
mc.postToChat(  "%s Entidad/es en el server" %number)

for id in players_ids:
    mc.postToChat("Entidad : %s" %id)

fin = False
chatPost = "0"

mc.postToChat("Acciones disponibles 0-10")
mc.postToChat("0- Test")
mc.postToChat("1- Idea (TNT) --> Falta Programas")
mc.postToChat("2- Idea (Chat insultos con valor aleatorio) --> Falta Programas")
mc.postToChat("3- Falta por definir")
mc.postToChat("4- Falta por definir")
mc.postToChat("5- Falta por definir")
mc.postToChat("6- Falta por definir")
mc.postToChat("7- Falta por definir")
mc.postToChat("8- Falta por definir")
mc.postToChat("9- Falta por definir")
mc.postToChat("10- Falta por definir")
mc.postToChat("69- Parar Script")

while fin == False:
    
    for chatPost in mc.events.pollChatPosts():
        if chatPost.message.lower() == "0":
            mc.postToChat("Test")
            
        elif chatPost.message.lower() == "1":
            mc.postToChat("Dinamita")
            
        elif chatPost.message.lower() == "2":
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == "3":
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == "4":
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == "5":
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == "6":
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == '7':
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == '8':
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == '9':
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == '10':
            mc.postToChat("--Falta Por definir--")
            
        elif chatPost.message.lower() == '69':
            mc.postToChat("Final")
            fin = True