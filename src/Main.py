
from Modulo_funciones import *
from Acciones.dinamita import *
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create("localhost")



#Para limpiar la terminal minimamente
print("\n") 
mc.postToChat(" ")
mc.postToChat(" ")
# Paramos 2 segundos para poder abrir con tranquilidad el Minecraft
time.sleep(2)

# Ejemplo: Conexión al juego
mc.postToChat("Informacion Basica")
pos = mc.player.getTilePos()

# Entidades y lectura del char
players_ids = mc.getPlayerEntityIds()
print(len(players_ids), " entidad/es disponible/s.")
number = len(players_ids)
mc.postToChat( "%s Entidad/es en el server" %number)

for id in players_ids:
    mc.postToChat("Entidad : %s" %id)

print("") #Para limpiar la terminal minimamente


# Test del insult Bot
lista = ["BOBO", "ZOQUETE", "GILIPOLLAS", "INEPTO", "MONONEURONAL", "RETRASADO"]

for insult in lista:
    add_insulto(insult)

insult_bot(2)


mc.postToChat("Acciones disponibles [0-5]")
mc.postToChat("0- Test")
mc.postToChat("1- Idea (TNT) --> Falta Programas")
mc.postToChat("2- Idea (Chat insultos con valor aleatorio) --> Falta Programas")
mc.postToChat("3- Falta por definir")
mc.postToChat("4- Falta por definir")
mc.postToChat("5- Falta por definir")
mc.postToChat("10- Parar Script")

chatPost = 0
fin = False
while fin == False:
    
    for chatPost in mc.events.pollChatPosts():
        
        if chatPost.message.lower() == "0":
            mc.postToChat("Test")
            chatPost = 0 # Reseteamos el chatpost
            
        elif chatPost.message.lower() == "1":
            mc.postToChat("Dinamita")
            explosion_TNT()
            chatPost = 0 # Reseteamos el chatpost
            
        elif chatPost.message.lower() == "2":
            mc.postToChat("--Falta Por definir--")
            chatPost = 0 # Reseteamos el chatpost
            
        elif chatPost.message.lower() == "3":
            mc.postToChat("--Falta Por definir--")
            chatPost = 0 # Reseteamos el chatpost
            
        elif chatPost.message.lower() == "4":
            mc.postToChat("--Falta Por definir--")
            chatPost = 0 # Reseteamos el chatpost
                        
        elif chatPost.message.lower() == "5":
            mc.postToChat("--Falta Por definir--")
            chatPost = 0 # Reseteamos el chatpost
                              
                              
        elif chatPost.message.lower() == '10':
            mc.postToChat("Salida del Bot")
            chatPost = 0 # Reseteamos el chatpost
            fin = True
