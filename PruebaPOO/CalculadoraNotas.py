class CalcularNotas:

    def __init__(self, notas):
        self.notas = notas

    def promedioNotas(self):
        sumatoria = 0

        for nota in self.notas:
            sumatoria = sumatoria + nota

        print(f"La nota promedio es {sumatoria/len(self.notas)}")
    
    def nota_mas_alta(self):

        nota_alta = 0

        for nota in self.notas:
            if nota > nota_alta:
                nota_alta = nota
        
        print(f"La nota mas alta es: {nota_alta}")
    
    def nota_mas_baja(self):

        nota_baja = 5

        for nota in self.notas:
            if nota < nota_baja:
                nota_baja = nota
        
        print(f"La nota mas baja es: {nota_baja}")