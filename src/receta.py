from paciente import Paciente
from medico import Medico
import datetime

class Receta:

    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str], fecha: datetime.datetime):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.medicamentos = medicamentos

    def __str__(self) -> str:
        return f"Receta: Paciente: {self.paciente}, Médico: {self.medico}, Fecha Nacimiento: {self.fecha_nacimiento}"
