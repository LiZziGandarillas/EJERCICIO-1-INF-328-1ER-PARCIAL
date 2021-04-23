from __future__ import annotations


class Facade:

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def OperacionFacade(self) -> str:
        results = []
        results.append("\nFIN FACHADA \n----------- \n")
        print("INICIO FACHADA\n-------------- ")
        results.append(self._subsystem1.operacionEst())
        if (self._subsystem1.operacionMateria()) == "l":            
            results.append(self._subsystem2.operacionLab())  
        else:
            results.append(self._subsystem2.operacionTeo())          
        return "".join(results)



class Subsystem1:
   
    def operacionMateria(self) -> str:
       print("\nIngrese el tipo de materia laboratorio o teorica (l/t):",end=" ")
       dato = input().lower()
       if dato == "l":
           return "l"
       else:
           return "t"
    def operacionEst(self) -> str:
         nombre = input("Ingrese el nombre del estudiante: ")
         return "El estudiante " + nombre


class Subsystem2:
    
    def operacionLab(self) -> str:
        notaFinal = 0
        print("La materia cuenta con auxiliatura(s/n):", end=" ");
        aux = input().lower()
        notaAux = 0
        if (aux == "s"):
            notaAux = int(input("Ingrese cuanto vale la auxiliatura: "))
        numTot = int(input("Ingrese el numero de laboratorios: "))
        notaLab = int(input("Ingrese la nota que vale un laboratorio: "))
        nota= int(notaLab*numTot)
        notaEst = 0
        print()
        for i in range(0,numTot):
            notaEst=notaLab+1
            while notaEst>notaLab:
                notaEst= int(input("Ingrese la nota obtenida en el " + str(i+1) + "º laboratorio: "))
                if(notaEst>notaLab):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaEst
        notaAuxEst = 0
        if (aux == "s"):
            notaAuxEst = notaAux + 1
            while (notaAuxEst > notaAux):
                notaAuxEst = int(input("Ingrese la nota de auxiliatura: "))
                if (notaAuxEst > notaAux):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaAuxEst
        print("\nNOTA FINAL DE LABORATORIO: ", notaFinal)
        if notaFinal > nota/2:
           return " APROBO"
        else:
           return " REPROBO"

    def operacionTeo(self) -> str:
        notaFinal = 0
        print("La materia cuenta con auxiliatura(s/n):", end=" ");
        aux = input().lower()
        notaAux = 0
        if (aux == "s"):
            notaAux = int(input("Ingrese cuanto vale la auxiliatura: "))
        numTot = int(input("Ingrese el numero de parciales: "))
        nota = 0
        notaEst = 0
        notaTeo = [0 for x in range(numTot)]
        for i in range (0,numTot):
           notaTeo[i] = int(input("Ingrese por cuanta nota evaluara el "+ str(i+1) +"º parcial: "))
           nota += notaTeo[i]
        print()
        for i in range(0,numTot):
            notaEst=notaTeo[i]+1
            while notaEst>notaTeo[i]:
                notaEst= int(input("Ingrese nota obtenida en el " + str(i+1) + "º parcial: "))
                if(notaEst>notaTeo[i]):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaEst
        notaAuxEst = 0
        if (aux == "s"):
            notaAuxEst = notaAux + 1
            while (notaAuxEst > notaAux):
                notaAuxEst = int(input("Ingrese la nota de auxiliatura: "))
                if (notaAuxEst > notaAux):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaAuxEst
        print("\nNOTA FINAL:", notaFinal)
        if notaFinal > nota/2:
           return " APROBO"
        else:
           return " REPROBO"


def client_code(facade: Facade) -> None:
   

    print(facade.OperacionFacade(), end="")


if __name__ == "__main__":

    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
