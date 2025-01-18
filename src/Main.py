
from Acciones.insult_bot import *
from Acciones.textos import *
from Acciones.dinamita import *
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create("localhost")



#Para limpiar la terminal minimamente
print("\n") 
mc.postToChat(" ")

# Paramos 2 segundos para poder abrir con tranquilidad el Minecraft
time.sleep(1)


# Printar informacion básica del servidor
informacion_basica()

# Printar el Menu principal de actividades
print_Menu_Acciones()

chatPost = 0
fin = False
while fin == False:
    
    for chatPost in mc.events.pollChatPosts():
        
        if chatPost.message.lower() == "0":
            mc.postToChat("Test")
            
                        
        elif chatPost.message.lower() == "1":
            mc.postToChat("Dinamita")
            explosion_TNT()
            
        elif chatPost.message.lower() == "2":
            mc.postToChat("Insultos")
            insult_bot()
                          
        elif chatPost.message.lower() == "3":
            mc.postToChat("--Falta Por definir--")
                          
        elif chatPost.message.lower() == "4":
            mc.postToChat("--Falta Por definir--")
                                      
        elif chatPost.message.lower() == "5":
            mc.postToChat("--Falta Por definir--")                                            
                              
        elif chatPost.message.lower() == '10':
            mc.postToChat("Salida del Bot")
            fin = True
            break

        mc.events.clearAll() # Limpiamos la lista para no acumular registros
        print_Menu_Acciones() 
        
