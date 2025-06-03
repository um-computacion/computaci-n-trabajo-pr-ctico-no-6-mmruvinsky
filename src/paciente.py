import re

class Paciente:
    
    def __init__(self, nombre: str, _dni: str, fecha_nacimiento: str):

        if not self._validar_fecha(fecha_nacimiento):
            raise ValueError("Formato de fecha inválido. Debe ser dd/mm/aaaa")
        
        self.nombre = nombre
        self._dni = _dni
        self.fecha_nacimiento = fecha_nacimiento

        def _validar_fecha(self, fecha: str) -> bool:
        #Expresión regular para dd/mm/aaaa
            patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
            return bool(re.match(patron, fecha))
        
        def obtener_dni(self) -> str:
            return self._dni    
        
        def __str__(self) -> str:
            return f"Paciente: {self.nombre}, DNI: {self._dni}, Fecha Nacimiento: {self.fecha_nacimiento}"
        

