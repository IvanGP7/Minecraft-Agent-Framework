from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

print(os.getenv("OPENAI_API_KEY"))