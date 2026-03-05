from pydantic import BaseModel
from datetime import date, time

class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    personas: int
    estado: str
    