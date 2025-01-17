import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create("localhost")

def dinamita(size):
    pos = mc.player.getTilePos()
    if size < 10:   #seguridad absoluta
        for i in range(0, size):
            for j in range(0, size):
                for k in range(0, size):
                    mc.setBlock(pos.x + 7 + size + k, pos.y + j, pos.z+ i, block.TNT.id, 1)  # Encender la TNT

def explosion_TNT():
    
    mc.postToChat("Elige un numero las dimensiones de la dinamita")
    
    chatPost = 0
    print(chatPost)
    mc.events.pollChatPosts().clear()
    
    salida = False
    while salida == False:
        
        for chatPost in mc.events.pollChatPosts():
            num_bloques_tnt = int(chatPost.message.lower())
            print("Numero de TNTs: ", num_bloques_tnt)
            if(num_bloques_tnt > 0 and num_bloques_tnt < 11):
                dinamita(num_bloques_tnt)
                salida = True
                chatPost = "0"
                
            if(num_bloques_tnt > 10):
                mc.postToChat("Donde vas matado haciendo una dinamita de (%s)^3 Melon" %num_bloques_tnt)
                salida = True
                chatPost = "0"
            
        
        
        