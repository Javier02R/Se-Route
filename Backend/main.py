from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from fuzzywuzzy import process

app = FastAPI()

# Configuración de CORS
origins = ["http://localhost", "http://localhost:8100"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar la base de conocimientos desde el archivo JSON 
with open('base_conocimiento.json', 'r', encoding='utf-8') as file:
    base_conocimiento = json.load(file)

# Función para buscar la mejor coincidencia en la base de conocimientos
def buscar_solucion(pregunta: str):
    preguntas = [problema["pregunta"] for problema in base_conocimiento["problemas"]]
    pregunta_cercana, _ = process.extractOne(pregunta, preguntas)
    for problema in base_conocimiento["problemas"]:
        if problema["pregunta"] == pregunta_cercana:
            return problema["solucion"]
    return None

@app.get("/tab1/{pregunta}")
def obtener_solucion(pregunta: str):
    # Buscar la solución para la pregunta en la base de conocimientos
    solucion = buscar_solucion(pregunta)

    # Si no se encuentra una solución, lanzar una excepción 404 (Not Found)
    if solucion is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    # Devolver la solución en formato JSON
    return {"solucion": solucion}
