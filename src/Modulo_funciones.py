import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create("localhost")

lista_insultos = []

# Función para añadir un insulto a la lista global
def add_insulto(insulto):
    if insulto not in lista_insultos:
        lista_insultos.append(insulto)
        print(str(insulto) + " Se ha añadido a la lista de insultos global.")

# Función para Escribir por chat un insulto a través de un índice.
def insult_bot(indice):
    if indice <= len(lista_insultos):
        mc.postToChat(lista_insultos[indice-1])
    else:
        print("Se ha intentado escribir el insulto " + str(indice) + ", cuando solo tenemos " + str(len(lista_insultos)) + " elementos en la lista.")