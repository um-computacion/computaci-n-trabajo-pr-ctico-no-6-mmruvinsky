from paciente import Paciente
from medico import Medico
from turno import Turno
from historiaclinica import HistoriaClinica
from receta import Receta
import datetime

class Clinica:
    
    def __init__(self):

        self.__pacientes = {}        
        self.__medicos = {}        
        self.__turnos = []           
        self.__historias_clinicas = {} 

#PACIENTES

    def agregar_paciente(self, paciente: Paciente):
        self.__pacientes[paciente._dni] = paciente

#MEDICOS

    def agregar_medico(self, medico: Medico):
        self.__medicos[medico.matricula] = medico

#TURNOS

    def agendar_turno(self, dni: str, matriculo: str, fecha_hora: datetime):
        self.__turnos[turno]

    

    
