# Minecraft Python Interaction with mcpi

## Objetivo
El propósito de esta práctica es interactuar con el mundo de **Minecraft** utilizando la biblioteca **mcpi** en Python. A través de este entorno, controlaremos y modificaremos el juego directamente desde el código creando un Framework complentamente funcional.

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

4. Tener el Minecraft instalado
5. Abrir minecraft con la versión 1.12 (Recomendación resolución 1024x768)
6. Añadir un servidor en Minecraft en el apartado de multijugador con ip "localhost"
7. Abrir la carpeta del servidor acceder a Server/ y ejecutar server.exe
8. Entrar dentro del servidor desde el minecraft
9. Ejecutar la Pracica desde el archivo Main.py


## Control sobre el Código

Para Tener un control sobre el código creado tenemos unos test que son los archivos:
- Interactive_Test.py  (Test interactivo con el usuario para probar impresiones por chat y la lectura de este) 
- Unit_Test.py         (Test sobre funciones atomáticas sin necesidad de interacción directa del usario)


Para controlar el código que tenemos y que ejecutamos podemos hacer un Coverage con:
(Solo la primera vez)
    ```bash
    pip install coverage 
Coverage:
    ```bash
    cd ../Minecraft-Agent-Framework/src
    ```bash
    coverage run -m unittest Unit_Test.py
    ```bash
    coverage report

## Recomendación

Guia para librería mcpi:
https://www.stuffaboutcode.com/p/minecraft-api-reference.html

