from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def inicio():
    return "Bienvenido a la api rest de eventos"

@app.post("/eventos")
async def crear_evento():
    return {"mensaje": "Creando un evento"}

@app.put("/eventos/")
async def modificarEvento():
    return {"mensaje": "Editando un evento"}

@app.get("/eventos/")
async def consultarEvento():
    return {"mensaje": "Consultado un eventos"}
@app.get("/evento/")
async def consultarEvento():
    return {"mensaje": "Consultando un evento "}

@app.get("/eventos/{idEvento:int}")
async def consultarIndividual(idEvento: int):
    return {"mensaje": f"Consultando un evento con id {idEvento}"}

@app.delete("/eventos/")
async def eliminarEvento():
    return {"mensaje": "Eliminando un evento"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
    