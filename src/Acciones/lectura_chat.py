import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("localhost")


def Lectura_chat():

    chatPost = "0"
    mc.events.pollChatPosts().clear()

    salida = False
    while salida == False:
        
        for chatPost in mc.events.pollChatPosts():
            decision = chatPost.message.lower()
            salida = True
            chatPost = "0"
    
    return decision