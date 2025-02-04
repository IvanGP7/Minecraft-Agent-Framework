import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create("localhost")

atributos_mc_player = dir(mc.player)

for atributo in atributos_mc_player:
    valor = getattr(mc.player, atributo, None)
    if valor is not None:
        if(atributo == "setTilePos"):
            print(f"Atributo: {atributo} -> Tipo: {type(valor)} -> Subatributos: {dir(valor)}")

