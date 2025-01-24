# Minecraft Python Interaction with mcpi

## Objetivo
Desarrollar un framework en Minecraft, ejecutado en un servidor localhost, que permita implementar y gestionar funcionalidades interactivas utilizando Python y la librería MCPI. El objetivo principal es integrar características dinámicas que mejoren la experiencia dentro del juego, incluyendo:
1.	Creación de un conjunto de dinamitas para realizar explosiones de forma controlada en el entorno de Minecraft.
2.	Gestión de una lista de almacenamiento de insultos, proporcionando una funcionalidad para registrar y consultar elementos en tiempo real desde el juego.
3.	Implementación de una API conectada con ChatGPT, permitiendo realizar consultas y recibir respuestas directamente en el chat del juego.

Adicionalmente, el framework hace uso de funciones clave como la impresión de menús interactivos en el chat y la lectura en tiempo real de las interacciones de los jugadores, fomentando una integración intuitiva entre el usuario y las herramientas desarrolladas.

## Pasos para la instalación y configuración:

1. Asegurar que el servidor esté instalado de:
    ```bash
    git clone https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-PC

2. Instalaciones necesarias desde consola bash: 
    - Para hacer uso de las funciones del Minecraft
        ```bash
        pip install mcpi
    - Para asginar variables de entorno en un archivo .env
        ```bash
        pip install python-dotenv
    - Para hacer uso de la versión correcta del ChatGPT
        ```bash
        pip install openai==0.28

3. Crear archivo .env en la carpeta src con la siguiente linea de codigo para conectar con la API del chatgpt, añadiendo la API_Key Personal:
    OPENAI_API_KEY="sk-..."

4. Tener el Minecraft instalado.
5. Abrir Minecraft con la versión 1.12 (Recomendación resolución 1024x768).
6. Añadir un servidor en Minecraft en el apartado de Multijugador con ip "localhost".
7. Abrir la carpeta del servidor acceder a Server/ y ejecutar server.exe.
8. Entrar dentro del servidor recientemente creado desde Minecraft.
9. Ejecutar el archivo Main.py para implementar el Framework.


## Control sobre el Código

Para Tener un control sobre el código creado tenemos unos test que son los archivos:
- Interactive_Test.py  (Test interactivo con el usuario para probar impresiones por chat y la lectura de este) 
- Unit_Test.py         (Test sobre funciones atomáticas sin necesidad de interacción directa del usario)


Para controlar el código que tenemos y que ejecutamos podemos hacer un Coverage con:
- Instalación del Coverage 
    ```bash
    pip install coverage 
- Ejecución del Coverage:
    - Situarnos en la carpeta donde se encuentra proyecto.
        ```bash
        cd ../Minecraft-Agent-Framework/src
    - Ejecutamos el Coverage en el Unit_Test.
        ```bash
        coverage run -m unittest Unit_Test.py
    - Revisamos el reporte proporcionado.
        ```bash
        coverage report

## Creación de un nuevo agente 

Como este poryecto trata de ser un Framework hay que tener en cuenta que podemos añadir nuevos agentes o implementaciones de manera sencilla
y comoda para el un usuario cualquiera.

Ejemplo de nuevo agente:
- Crear un nuevo archivo (teletransporte.py) en la carpeta Acciones, que es donde tenemos todos los Agentes.
    #### **Contenido del Agente (teletransporte.py):**
    ```python
    import mcpi.minecraft as minecraft
    import mcpi.block as block
    import random

    mc = minecraft.Minecraft.create("localhost")


    def teleport():
    pos = mc.player.getTilePos()
        mc.player.setPos(random.randint((pos.x-10000), (pos.x+10000)), pos.y, random.randint((pos.z-10000), (pos.z+10000)))
        
- Añadir la función al archivo Main.py: 
    #### **Contenido del Main.py:**
    ```python
    from Acciones.teletransporte import *

- Añadir en el archivo Main.py la llamada a la función del nuevo Agente dentro del bucle que interactura con el jugador: 
    #### **Contenido del Main.py:**
    ```python
    elif decision == "4":
        mc.postToChat("Teletransporte")
        teleport()
        print_Menu_Acciones()

## Recomendación

Guia para usar la librería mcpi para añadir mas Agentes al Framework:
https://www.stuffaboutcode.com/p/minecraft-api-reference.html
https://pimylifeup.com/minecraft-pi-edition-api-reference/


