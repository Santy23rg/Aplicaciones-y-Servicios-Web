from fastapi import FastAPI

app = FastAPI()
# Ruta raíz
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Ruta de saludo
@app.get("/saludo/{nombre}")

async def get_saludo(nombre: str):
    return {"message": f"Hola, {nombre}!"}

# Ruta participante
participantes = []
@app.post("/participantes")

async def create_participante(nombre: str) -> dict:
    participante = {"id":len(participantes)+1, "nombre": nombre}
    participantes.append(participante)
    return participante

# Cambios de prueba David
participantes = []
@app.post("/participantes")

async def create_participante(nombre: str) -> dict:
    participante = {"id":len(participantes)+1, "nombre": nombre}
    participantes.append(participante)
    return participante
