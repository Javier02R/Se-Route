# Sistema Experto

## Descripción
Sistema Experto que tiene como objetivo asistir a los usuarios que presentan problemas de conexión al utilizar su router, ya sea por 
mala configuración, equipo defectuoso u otra eventualidad. El funcionamiento de este software se basa en el consumo de una base de conocimiento definida en un archivo json, utilizando fastapi para hacer una conexión entre los datos de la base y las preguntas que realiza el usuario.


## Tabs
- Tab1 (Inicio): Descripcion de la app, boton de enlace a al sistema experto.
- Tab2 (Consultar): Caja para hacer las preguntas al SE y posteriormente obtener respuesta.

## Herramientas utilizadas
- Python + Fastapi: Para creacion de la api
- Ionic + Angular: Interfaz de usuario

## Capturas de Pantalla
![Tab - Cuentas](/cuenta.png)
![Tab - Transferencias](/transferencia.png)
![Tab - Transferencias](/soporte.png)

## Características
- Recibe y responde preguntas.
- Utiliza FuzzyWuzzy para encontrar similtudes difusas entre cadenas.

## Instalación
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Node.js y npm instalado.
3. Ejecuta `npm install` para instalar las dependencias.
4. Crea el entorno virtual para fastapi.
5. Instala Fastapi y Uvicorn.

## Uso
- Ejecuta `ionic serve` para iniciar la aplicación en tu navegador.
- Ejecuta `uvicorn main:app --reload` para iniciar el servidor de la api

