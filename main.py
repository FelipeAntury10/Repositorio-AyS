from fastapi import FastAPI
from models import Reserva

app = FastAPI()
reservas = []

@app.post("/reservas")
def crear_reserva(reserva: Reserva):
    reservas.append(reserva)
    return reserva

@app.get("/reservas")
def listar_reservas():
    return reservas

