from fastapi import FastAPI, HTTPException

app = FastAPI()

# Diccionario de preguntas y soluciones (esto podría ser reemplazado por una base de datos)
soluciones_por_pregunta = {
    "No puedo conectarme a Internet": "1. Verifica que el cable esté conectado correctamente.\n2. Reinicia el router y el módem.",
    "Mi conexión es lenta": "1. Verifica la velocidad de tu conexión.\n2. Considera cambiar a una conexión por cable en lugar de inalámbrica.",
    # ... Agrega más preguntas y soluciones según sea necesario
}

@app.get("/preguntas/{pregunta}")
def obtener_solucion(pregunta: str):
    # Buscar la solución para la pregunta en el diccionario
    solucion = soluciones_por_pregunta.get(pregunta)

    # Si no se encuentra una solución, lanzar una excepción 404 (Not Found)
    if solucion is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    # Devolver la solución en formato JSON
    return {"solucion": solucion}
