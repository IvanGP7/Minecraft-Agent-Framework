# Minecraft Python Interaction with mcpi

## Objetivo
El propósito de esta práctica es interactuar con el mundo de **Minecraft** utilizando el plugin **RaspberryJuice** y la biblioteca **mcpi** en Python. A través de este entorno, controlaremos y modificaremos el juego directamente desde el código.

## Pasos para la instalación y configuración:

1. Asegurar que el servidor esté instalado de: https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-PC
2. Instalaciones necesarias desde consola bash: 
    pip install mcpi            --> Para hacer uso de las funciones del Minecraft
    pip install python-dotenv   --> Para asginar variables de entorno en un archivo .env
    pip install openai==0.28    --> Para hacer uso de la versión correcta del ChatGPT
3. Crear archivo .env en la carpeta src con la siguiente linea de codigo para conectar con la API del chatgpt:
    OPENAI_API_KEY="sk-..."

4. Tener el Minecraft instalado
5. Abrir minecraft con la versión 1.12 (Recomendación resolución 1024x768)
6. Añadir un servidor en Minecraft en el apartado de multijugador con ip "localhost"
7. Abrir la carpeta del servidor acceder a Server/ y ejecutar server.exe
8. Entrar dentro del servidor desde el minecraft
9. Ejecutar la Pracica desde el archivo Main.py

Guia para librería mcpi:
https://www.stuffaboutcode.com/p/minecraft-api-reference.html


