from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
  

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"{self.implementation.operation_implementation()}")    
    

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        nombre = input("Ingrese el nombre del estudiante: ")
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
            return "El estudiante "+ nombre + " APROBO"
        else:
            return "El estudiante " + nombre + " REPROBO"


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        nombre = input("Ingrese el nombre del estudiante: ")
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
                return "El estudiante "+ nombre + " APROBO"
        else:
                return "El estudiante " + nombre + " REPROBO"  

def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")



if __name__ == "__main__":
    print("\nIngrese el tipo de materia laboratorio o teorica (l/t):",end=" ")
    dato = input().lower()
    if dato == "l":
        implementation = ConcreteImplementationA()
    else:
        implementation = ConcreteImplementationB()
    abstraction = Abstraction(implementation)
    client_code(abstraction)
