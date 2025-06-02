from src.paciente import Paciente
from src.medico import Medico
import datetime

class Turno:

    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime.datetime):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora

    def obtener_detalles(self) -> str:
        return (f"Turno:\n"
                f"Paciente: {self.paciente.nombre}, DNI: {self.paciente.obtener_dni()}, "
                f"Fecha Nacimiento: {self.paciente.fecha_nacimiento}\n"
                f"Médico: {self.medico.nombre}, Matrícula: {self.medico.obtener_matricula()}, "
                f"Especialidad: {self.medico.especialidad}\n"
                f"Fecha y Hora del Turno: {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}")
    
    def obtener_fecha_hora(self) -> datetime.datetime:
        return self.fecha_hora
    
    def __str__(self) -> str:
        return self.obtener_detalles()
    
    
    

    