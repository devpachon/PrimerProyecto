class Estudiante:

    def __init__(self, nombre, apellido, identificacion, notas):
        
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.notas = notas

    def asistir_clase(self, fecha, asistencia):

        if asistencia:
            print(f"el estudiante {self.nombre} asistio a la clase del {fecha} ")
        else:
            print("No asisti a clase")

    def enviar_tarea(self, tarea):

        envio = input("Desea enviar la tarea:\n SI\n NO: ").upper()
        print (f"La tarea {tarea} fue...")
        if envio == "SI":
            return "Enviada para revisar"
        else:
            return "No enviada"