from fastapi import FastAPI,Request
import uvicorn
from dao.EventosDAO import EventosDAO
from dao.database import Conexion
from models.EventosModel import vEventos,Salida,Eventos,EventoSalida

app = FastAPI()

@app.on_event("startup")
def startup():
    conexion=Conexion()
    session=conexion.getSession()
    app.session=session
    print("Conexión a la base de datos establecida")

@app.get("/")
async def inicio():
    return "Bienvenido a la api rest de eventos"

@app.post("/eventos",summary="Crear un nuevo evento",response_model=Salida)
async def crear_evento(evento:Eventos, request:Request):
    eDAO=EventosDAO(request.app.session)
    return eDAO.agregar(evento)

@app.put("/eventos/")
async def modificarEvento():
    return {"mensaje": "Editando un evento"}

@app.get("/eventos",response_model=list[vEventos],tags=["Eventos"],summary="Consultar de eventos")
async def consultarEventos(request:Request)-> list[vEventos]:
    eDAO = EventosDAO(request.app.session)
    return eDAO.consultar()

@app.get("/eventos/{idEvento:int}",tags=["Eventos"],summary="Consultar evento por su ID",response_model=EventoSalida)
async def consultarIndividual(idEvento: int, request:Request):
    eDAO = EventosDAO(request.app.session)
    return eDAO.consultarPorId(idEvento)

@app.delete("/eventos/")
async def eliminarEvento():
    return {"mensaje": "Eliminando un evento"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
    