import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("localhost")

lista_insultos = ["BOBO", "ZOQUETE", "GILIPOLLAS", "INEPTO", "MONONEURONAL", "RETRASADO"]

# Función para añadir un insulto a la lista global
def add_insulto(insulto):
    if insulto not in lista_insultos:
        lista_insultos.append(insulto)
        print(str(insulto) + " Se ha añadido a la lista de insultos global.")

# Función para Escribir por chat un insulto a través de un índice.
def print_insult(indice):
    if indice <= len(lista_insultos):
        mc.postToChat(lista_insultos[indice-1])
    else:
        print("Se ha intentado escribir el insulto " + str(indice) + ", cuando solo tenemos " + str(len(lista_insultos)) + " elementos en la lista.")


#
# Leer chat para almacenar insulto
# insultar a (mostrar lista de entidades y que elija)
# Decidir que insulto o si hacerlo aleatorio
#
def insult_bot():
    
    mc.postToChat("Elige opciones del bot de insultos")
    
    chatPost = 0
    mc.events.pollChatPosts().clear()

    salida = False
    while salida == False:
        
        for chatPost in mc.events.pollChatPosts():
            decision = int(chatPost.message.lower())