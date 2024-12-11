
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("localhost")

# Ejemplo: Conexión al juego
mc.postToChat("Hello Minecraft World")
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)
