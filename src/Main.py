
from Acciones.insult_bot import *
from Acciones.textos import *
from Acciones.dinamita import *
from Acciones.chatgpt import *
from Acciones.lectura_chat import *
from Acciones.teleport import *

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

salida = False

while salida == False:
    decision = Lectura_chat()

    if decision == "0":
        mc.postToChat("Test")
        print_Menu_Acciones()
        
                    
    elif decision == "1":
        mc.postToChat("Dinamita")
        explosion_TNT()
        print_Menu_Acciones()
        
    elif decision == "2":
        mc.postToChat("Insultos")
        insult_bot()
        print_Menu_Acciones()
                        
    elif decision == "3":
        mc.postToChat("ChatGPT")
        ChatGPT()
        print_Menu_Acciones()
                        
    elif decision == "4":
        mc.postToChat("--Falta Por Crear--")
        print_Menu_Acciones()
                                    
    elif decision == "5":
        mc.postToChat("Teletransporte")
        teleport()
        print_Menu_Acciones()                                             
                            
    elif decision == "10":
        mc.postToChat("Salida del Bot")
        salida = True
        break


        
        
