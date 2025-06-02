class Medico:
    
    def __init__(self, nombre: str, matricula: str, especialidad: str):
        self.nombre = nombre
        self.matricula = matricula
        self.especialidad = especialidad

    def obtener_matricula(self):
        return self.matricula

    def __str__(self) -> str:
        return f"Medico: {self.nombre}, Matricula: {self.matricula}, Especialidad: {self.especialidad}"
