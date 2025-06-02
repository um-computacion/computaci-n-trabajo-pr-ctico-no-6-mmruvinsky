from paciente import Paciente
from turno import Turno
from receta import Receta


class HistoriaClinica:

    def __init__(self, paciente, turno: list[Turno], receta: list[Receta]):
        self.paciente = paciente
        self.turno = turno
        self.receta = receta

    def agregar_turno(self, nuevo_turno):
        self.turno.append(nuevo_turno)

    def agregar_receta(self, nueva_receta):
        self.receta.append(nueva_receta)

    def obtener_turnos(self) -> list:
        return self.turno
    
    def __str__(self) -> str:
        return f"Historia Clínica:  Paciente: {self.paciente}, Turno: {self.turno}, Receta: {self.receta}"



        



