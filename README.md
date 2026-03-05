# Microservicio de Reservas – FastAPI

Microservicio web para la gestión básica de reservas de salas académicas, desarrollado con FastAPI y validación de datos usando Pydantic.  
Las reservas se almacenan temporalmente en memoria y se intercambian en formato JSON.

---

## Requisitos

- Python 3.10 o superior
- Git

---

## Instalación

Clonar el repositorio y crear el entorno virtual:

```bash
git clone https://github.com/usuario/reservas-fastapi.git
cd reservas-fastapi
python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
