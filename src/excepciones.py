from paciente import Paciente
from medico import Medico
from turno import Turno
from receta import Receta
from historiaclinica import HistoriaClinica

class ExcepcionTurnoNoDisponible(Exception):
    def __init__(self, turno: Turno, paciente: Paciente):
        self.turno = turno
        self.paciente = paciente
        print